from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.core.validators import EmailValidator
from . import models
from django.contrib.auth.forms import AuthenticationForm


class Login(AuthenticationForm):
    # VALIDATION
    username = forms.CharField(
        label="Email/Username",
        widget=forms.TextInput(attrs={"placeholder": ""}),
        required=True,
    )

    class Meta:
        model = models.Staff
        fields = ("username", "password")


class EnterEmailForm(forms.ModelForm):
    # VALIDATION
    email = forms.EmailField(
        label="Enter your email to recover password",
        widget=forms.EmailInput(attrs={"placeholder": ""}),
        required=True,
    )

    class Meta:
        model = models.User
        fields = ("email",)


class EnterCodeForm(forms.ModelForm):

    # VALIDATION
    code = forms.IntegerField(
        label="Enter the code sent to your email",
        widget=forms.NumberInput(attrs={"placeholder": ""}),
        required=True,
    )

    email = forms.EmailField(
        label="",
        widget=forms.EmailInput(attrs={"type": "hidden"}),
        required=True,
    )

    class Meta:
        model = models.User
        fields = ("code", "email")


class ResetPasswordForm(forms.ModelForm):

    password = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={"type": "password"}),
        required=True,
    )

    confirm = forms.CharField(
        label="Confirm Password",
        widget=forms.TextInput(attrs={"type": "password"}),
        required=True,
    )

    class Meta:
        model = models.User
        fields = ("password", "confirm")
