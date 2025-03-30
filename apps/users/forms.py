# from django import forms
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth import get_user_model

# User = get_user_model()

# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, label="First Name")
    last_name = forms.CharField(max_length=30, required=True, label="Last Name")

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")

class CustomAuthenticationForm(AuthenticationForm):
    pass
