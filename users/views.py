import random

from django.contrib import messages
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from users.forms import UserRegistrationForm, UserProfileForm, UserLoginForm
from users.models import User


class RegistrationView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/registration_form.html'
    success_url = reverse_lazy('users:registration_success')

    def form_valid(self, form):
        new_user = form.save()
        verification_url = self._generate_verification_url(new_user.pk)
        send_mail(
            subject='Successfully registration.',
            message=f'To activate your account you need to click here: {verification_url}',
            from_email=None,
            recipient_list=[new_user.email]
        )
        return super().form_valid(form)

    def _generate_verification_url(self, user_pk):
        return self.request.build_absolute_uri(
            reverse('users:verification', kwargs={'pk': user_pk}))


def verification_view(request, pk):
    user = get_object_or_404(User, pk=pk)

    if not user.is_verified:
        user.is_verified = True
        user.save()

    return redirect('users:login')


class LoginView(BaseLoginView):
    model = User
    template_name = 'users/login_form.html'
    form_class = UserLoginForm
    success_url = reverse_lazy('categories:category_list')

    def form_valid(self, form):
        user = form.get_user()

        if not user.is_verified:
            messages.error(
                self.request, """Your account is not activated.
                 Please check your email to activate your account.""")
            return self.form_invalid(form)

        return super().form_valid(form)


class LogoutView(BaseLogoutView):
    pass


def registration_success(request):
    return render(request, template_name='users/registration_success.html')


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile_form.html'
    success_url = reverse_lazy('categories:category_list')

    def get_object(self, queryset=None):
        return self.request.user


def reset_password(request):
    user = request.user
    random_passwd = ''.join(str(random.randint(0, 12)) for _ in range(10))
    user = User.objects.get(pk=user.pk)
    user.set_password(random_passwd)
    user.save()

    login_url = reverse_lazy('users:login')
    send_mail(
        subject='New Password',
        message=f'Here is your new password {random_passwd} and here is the url {login_url}',
        from_email=None,
        recipient_list=[user.email]
    )
    return redirect(reverse_lazy('users:login'))
