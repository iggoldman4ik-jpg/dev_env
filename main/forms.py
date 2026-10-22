from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from main.models import Users

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            "class": "username_field"
        })
        self.fields["password"].widget.attrs.update({
            "class": "password_field"
        })

        self.fields["username"].label = "Имя пользователя"

    class Meta: 
        model=Users

class RegisterForm(UserCreationForm):
    class Meta:
        model=Users
        fields=["username", "password1", "password2"]