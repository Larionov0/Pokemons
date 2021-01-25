from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *


@login_required(login_url='/auth_sys/login')
def main_page(request):
    context = create_context(request)
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


@login_required(login_url='/auth_sys/login')
def find_pokemon(request):
    if request.POST:
        pokemon_name = request.POST.get('pokemon_name')
        pokemon = Pokemon.find_pokemon_by_name(pokemon_name)
        context = create_context(request)
        if not pokemon:
            context['message'] = 'Покемон не найден :('
        else:
            request.user.userprofile.pokemons.add(pokemon)
        return render(request, 'main_page.html', context)


def create_context(request):
    context = {}
    profile = request.user.userprofile
    context['pokemons'] = profile.pokemons.all()
    context['other_pokemons'] = Pokemon.get_or_create_other_pokemons(profile)
    context['username'] = request.user.username
    return context
