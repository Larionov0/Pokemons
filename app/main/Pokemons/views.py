from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *


@login_required(login_url='/auth_sys/login')
def main_page(request):
    context = {}
    profile = request.user.userprofile
    context['pokemons'] = profile.pokemons.all()
    context['other_pokemons'] = Pokemon.get_or_create_other_pokemons(profile)
    return render(request, 'main_page.html', context)


@login_required(login_url='/auth_sys/login')
def add_pokemon(request, pokemon_id):
    profile = request.user.userprofile
    try:
        profile.pokemons.add(Pokemon.objects.get(id=pokemon_id))
    except:
        pass
    return redirect('Pokemons:main')


@login_required(login_url='/auth_sys/login')
def remove_pokemon(request, pokemon_id):
    profile = request.user.userprofile
    try:
        profile.pokemons.remove(Pokemon.objects.get(id=pokemon_id))
    except:
        pass
    return redirect('Pokemons:main')
