from django.db import models
import requests


class Pokemon(models.Model):
    name = models.CharField(max_length=20)


    @property
    def skills(self):
        return

    @classmethod
    def get_or_create_other_pokemons(cls, userprofile, n=10):
        all_pokemons = cls.objects.all()
        user_pokemons = userprofile.pokemons.all()
        other_pokemons = list(filter(lambda pokemon: pokemon not in user_pokemons, all_pokemons))
        loaded_pokemons_ids = list(map(lambda pokemon: pokemon.id, all_pokemons))
        i = 1
        while len(other_pokemons) < n:
            if i not in loaded_pokemons_ids:
                try:
                    new_pokemon = cls.create_pokemon_from_json(
                        requests.get(f'https://pokeapi.co/api/v2/pokemon/{i}').json()
                    )
                    other_pokemons.append(new_pokemon)
                except:
                    break
            i += 1
        return other_pokemons

    @classmethod
    def create_pokemon_from_json(cls, pokemon_json: dict):
        return cls.objects.create(id=pokemon_json['id'], name=pokemon_json['name'])

    def __str__(self):
        return f"Pokemon {self.name}"
