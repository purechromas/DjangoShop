from django.urls import path

from users.apps import UsersConfig
from users.views import RegistrationView, LoginView, verification_view, registration_success, LogoutView, ProfileView, \
    reset_password

app_name = UsersConfig.name

urlpatterns = [
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('registration_success/', registration_success, name='registration_success'),
    path('login/', LoginView.as_view(), name='login'),
    path('verification/<int:pk>', verification_view, name='verification'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('reset_password/', reset_password, name='reset_password'),
]
