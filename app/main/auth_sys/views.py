from django.shortcuts import redirect, render
from django.contrib import auth
from .models import UserProfile
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm


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


def logout(request):
    auth.logout(request)
    return redirect("auth_sys:login")


class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = '/auth/login/'

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "sign_up.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()

        return super(RegisterFormView, self).form_valid(form)

