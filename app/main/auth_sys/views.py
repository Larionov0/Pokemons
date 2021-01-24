from django.shortcuts import redirect, render
from django.contrib import auth
from .models import UserProfile


def login(request):
    if request.user.is_authenticated:
        return redirect('Pokemons:main')

    return render(request, "login.html")


def login_handler(request):
    if request.POST:
        username = request.POST.get("username", '')
        password = request.POST.get("password", '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            if not hasattr(user, 'userprofile'):
                UserProfile.objects.create(user=user)
            return redirect("Pokemons:main")
        else:
            return render(request, "login.html", {
                'login_error': "incorrect authorization data"
            })


def register(request):
    pass
