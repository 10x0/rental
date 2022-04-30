from random import choices
from secrets import choice
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from users.models import User
from django.contrib.auth import authenticate



class RegistrationForm(UserCreationForm):

    ROLE_CHOICES = (
        ('Rider', 'Rider'),
        ('Provider', 'Provider'),
    )
    email = forms.EmailField(max_length=60, help_text='Add valid email address')
    role = forms.ChoiceField(choices=ROLE_CHOICES,widget=forms.RadioSelect())

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "role"]


class UserAuthenticationForm(forms.ModelForm):

    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password')

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        if not authenticate(username=username, password=password):
            raise forms.ValidationError('Invalid credentials!')

