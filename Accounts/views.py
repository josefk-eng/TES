from django.shortcuts import render, redirect
from . import forms
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, get_user_model, logout, forms as auth_form
from django.http import HttpResponseRedirect
from . import managers
from django.utils.timezone import datetime, timedelta
from . import utils
from utils import emailConfigs
import secrets

from rest_framework.decorators import api_view
from .serializers import UserSerializer
from rest_framework.response import Response


# Create your views here.


def login(request):
    if request.user.is_authenticated:
        return redirect("adminHome")
    if request.method == "POST":
        login_form = auth_form.AuthenticationForm(request, data=request.POST)
        if not login_form.is_valid():
            context = {"title": "Login", "form": login_form}
            return render(request, "login.html", context)
        else:
            user = login_form.get_user()
            if user is not None:
                auth_login(request, user)
                messages.success(request, "Logged In Successfully")
                return redirect("adminHome")
            else:
                messages.error(request, "Wrong credentials")
                context = {"title": "Login", "form": login_form}
                return render(request, "login.html", context)
    login_form = forms.Login()
    context = {"title": "Login", "form": login_form}
    return render(request, "login.html", context)


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')


def forgot_password(request):
    form = forms.EnterEmailForm(request.POST or None)
    if request.method == 'POST':
        if not form.is_valid():
            context = {"title": "Forgot Password", "form": form}
            return render(request, "forgot_password.html", context)
        else:
            email = request.POST["email"]
            users = get_user_model().objects.all()
            if email is not None and users.filter(email=email).exists():
                user = users.get(email=email)
                code = secrets.choice(range(10000, 50000))
                user.code = code
                user.save()
                # emailConfigs.sendMail(
                #     subject="Recovery Code",
                #     message=f'Your recovery code is <br> {code}',
                #     rcpt_list=[email, ]
                # )
                return redirect('code', id=user.id)
            else:
                messages.error(request, "Email not found")
                context = {"title": "Forgot Password", "form": form}
                return render(request, "forgot_password.html", context)
    context = {"title": "Forgot Password", "form": form}
    return render(request, "forgot_password.html", context)


def enter_code(request, id):
    users = get_user_model().objects.all()
    email = users.get(id=id).email
    if request.method == 'POST':
        code = request.POST['code']
        code_form = forms.EnterCodeForm(data={"email": email, "code": code})

        if not code_form.is_valid():
            context = {"title": "Enter Code", "form": code_form}
            return render(request, "enter_code.html", context)

        if email is not None and users.filter(email=email).exists():
            user = users.get(email=email)
            current = datetime.now(user.expiry_date.tzinfo)
            if code == str(user.code) and user.expiry_date > current:
                return redirect('reset', id=id)
                # re_form = forms.ResetPasswordForm(email=email)
                # context = {"title": "Reset Password", "form": re_form}
                # return render(request, "reset_password.html", context)
            else:
                messages.error(request, "Invalid or expired code")
                context = {"title": "Enter Code", "form": code_form}
                return render(request, "enter_code.html", context)
        else:
            messages.error(request, "Email not found")
            context = {"title": "Enter Code", "form": code_form}
            return render(request, "enter_code.html", context)
    else:
        code_form = forms.EnterCodeForm(data={"email": email, "code": ''})
        context = {"title": "Enter Code", "form": code_form}
        return render(request, "enter_code.html", context)


def reset_password(request, id):
    users = get_user_model().objects.all()
    user = users.get(id=id)
    re_form = forms.ResetPasswordForm(request.POST or None)
    if request.method == 'POST':
        if not re_form.is_valid():
            context = {"title": "Reset Password", "form": re_form}
            return render(request, "reset_password.html", context)
        password = request.POST["password"]
        confirm = request.POST["confirm"]
        if password is not confirm:
            messages.error(request, "Passwords do not match")
            context = {"title": "Reset Password", "form": re_form}
            return render(request, "reset_password.html", context)
        elif not utils.passwordStrength(password):
            messages.error(request, "Please use a strong password")
            context = {"title": "Reset Password", "form": re_form}
            return render(request, "reset_password.html", context)
        else:
            messages.success(request, "Password has been reset successfully")
            user.password = password
            user.save()
            redirect("login")
    else:
        context = {"title": "Reset Password", "form": re_form}
        return render(request, "reset_password.html", context)


def change(request):
    if request.method == "POST":
        password = request.POST["password"]
        confirm = request.POST["confirm"]

        if password is not confirm:
            messages.error(request, "Passwords do not match")
            context = {"title": "Reset Password"}
            return render(request, "reset_password.html", context)
        elif not utils.passwordStrength(password):
            messages.error(request, "Please use a strong password")
            context = {"title": "Reset Password"}
            return render(request, "reset_password.html", context)
        else:
            messages.success(request, "Password has been reset successfully")
            HttpResponseRedirect("login")
    else:
        context = {"title": "Reset Password"}
        return render(request, "reset_password.html", context)


@api_view(["POST"])
def loginClient(request):
    login_form = auth_form.AuthenticationForm(request, data=request.POST)
    if login_form.is_valid():
        return Response(login_form.data)
    else:
        return Response(login_form.errors)

