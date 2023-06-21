from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.admin, name="adminHome"),
    path("login/", include("Accounts.urls")),
    path("api/", include("StoreAPI.urls")),
    path("kisi/", include("kisi.urls"))
]
