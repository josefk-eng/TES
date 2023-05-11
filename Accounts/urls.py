from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.login, name="login"),
    path("forgot", views.forgot_password, name="forgot"),
    path("code/<int:id>", views.enter_code, name="code"),
    path("reset/<int:id>", views.reset_password, name="reset"),
    path("change", views.change, name="change"),
    path("logout", views.logout_view, name="logout"),
]
