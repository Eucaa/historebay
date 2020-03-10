from django import forms
from django.contrib.auth.models import User  # Import for creation registration form.
from django.contrib.auth.forms import UserCreationForm  # Import for creation registration form.
from django.core.exceptions import ValidationError


class UserLoginForm(forms.Form):  # Registered in views.py
    """Form is used to log users in"""

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)  # This will tell Django that we want to render a normal text input box but we wanted to be of type password.


class UserRegistrationForm(UserCreationForm):  # Registered in views.py
    """Form to register a new user"""

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)

    class Meta:  # This inner (meta)class will provide info about the form. They can be used (amongst other feats) in Django to specify fields dat will be exposed in sending an email.
        model = User
        fields = ['email', 'username', 'password1', 'password2']

    def clean_email(self):  # function to check whether an email and/ or username already exists in the database.
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exculde(username=username):
            raise forms.ValidationError("Email address must be unique")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password1 or not password2:
            raise ValidationError("Please confirm your password")

        if password1 != password2:
            raise ValidationError("Password must match")

        return password2
