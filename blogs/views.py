from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from blogs.forms import BlogForm
from blogs.models import Blog


class BlogListView(ListView):
    model = Blog
    extra_context = {'title': 'Blogs'}


class BlogCreateView(CreateView):
    model = Blog
    form_class = BlogForm
    extra_context = {'title': 'Create blog'}
    success_url = reverse_lazy('blogs:blog_list')


class BlogUpdateView(UpdateView):
    model = Blog
    form_class = BlogForm
    extra_context = {'title': 'Update blog'}
    success_url = reverse_lazy('blogs:blog_list')


class BlogDeleteView(DeleteView):
    model = Blog
    extra_context = {'title': 'Delete blog'}
    success_url = reverse_lazy('blogs:blog_list')


class BlogDetailView(DetailView):
    model = Blog
    extra_context = {'title': 'Blog'}

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.view_count += 1

        if obj.view_count == 100:
            subject = 'Congratulations on reaching 100 views!'
            message = f"""Hello\n\nCongratulations on your blog post reaching 100 views!\n\n
            Keep up the good work!\n\nBest regards,\nYour Website Team"""
            recipient_email = 'purechromas@gmail.com'

            send_mail(subject=subject, message=message, from_email=None, recipient_list=[recipient_email])

        obj.save()
        return obj
