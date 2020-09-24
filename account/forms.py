from django.utils.translation import ugettext_lazy as _

from django import forms
from django.contrib.auth import get_user_model, authenticate

from account.models import Profile

User = get_user_model()


class RegistrationForm(forms.Form):
    email = forms.EmailField()
    username = forms.CharField(max_length=32)
    password = forms.CharField(widget=forms.PasswordInput)
    avatar = forms.ImageField(required=False, label='avatar')

    def clean(self):
        if User.objects.filter(username=self.cleaned_data['username']).exists():
            raise forms.ValidationError('Sorry The username exists')

        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError('Sorry The email exists')

        return self.cleaned_data

    def save(self):
        user = User.objects.create_user(
            username=self.cleaned_data['username'], email=self.cleaned_data['email'],
            password=self.cleaned_data['password'])
        profile = Profile.objects.create(user=user, avatar=self.cleaned_data['avatar']
)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=32)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        user = authenticate(**self.cleaned_data)
        if user is None:
            raise forms.ValidationError(_('Sorry Unable to login with provided credentials'))
        self.cleaned_data['user'] = user
        return self.cleaned_data
