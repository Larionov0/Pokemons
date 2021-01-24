from django.urls import path
from . import views

app_name = 'Pokemons'
urlpatterns = [
    path('main/', views.main_page, name='main'),
    path('add_pokemon/<int:pokemon_id>', views.add_pokemon, name='add_pokemon'),
    path('remove_pokemon/<int:pokemon_id>', views.remove_pokemon, name='remove_pokemon'),
    path('find_pokemon/', views.find_pokemon, name='find_pokemon')
]
