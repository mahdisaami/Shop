from django.contrib import messages
from django.contrib.auth import get_user_model, login, authenticate, logout
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import FormView, DetailView

from account.forms import RegistrationForm, LoginForm
from shopping import settings

User = get_user_model()


class RegisterUserView(FormView):
    form_class = RegistrationForm
    success_url = '/'
    template_name = 'user/register.html'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        form.save()
        messages.success(self.request, f'New account created: {username}')
        return super().form_valid(form)


class LoginUserView(FormView):
    form_class = LoginForm
    success_url = '/'
    template_name = 'user/login.html'

    def form_valid(self, form):
        login(self.request, form.cleaned_data['user'])
        messages.info(self.request, 'Logged in successfully!')
        return super().form_valid(form)


class LogoutUserView(View):
    def get(self, request):
        logout(request)
        messages.info(request, "Logged out successfully!")
        return redirect('/')


class RetrieveUserView(DetailView):
    model = User
    template_name = 'user/profile.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
