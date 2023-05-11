from django.shortcuts import render, redirect


# Create your views here.
def admin(request):
    context = {}
    if request.user.is_authenticated:
        return render(request, "admin_home.html", context)
    return redirect("login")
