from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Record


def home_page(request):
    records = Record.objects.all()

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Has inciado sesión de manera éxitosa")
            return redirect("home")
        else:
            messages.error(request, "Usuario o contraseña incorrectos. Revisa tus datos, e intenta de nuevo.")
            return redirect("home")

    context = {}
    context['records'] = records
    return render(request, "home_page.html", context)


def logout_user(request):
    logout(request)
    messages.success(request, "Has cerrado sesión de manera exitosa")
    return redirect("home")
