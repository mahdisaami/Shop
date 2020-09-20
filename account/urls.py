from django.urls import path

from account.views import RegisterUserView, LoginUserView, LogoutUserView, RetrieveUserView

urlpatterns = [
    path('register', RegisterUserView.as_view(template_name='user/register.html'), name='register'),
    path('login', LoginUserView.as_view(template_name='user/login.html'), name='login'),
    path('logout', LogoutUserView.as_view(), name='logout'),
    path('profile/<str:username>', RetrieveUserView.as_view(), name='retrieve'),
]