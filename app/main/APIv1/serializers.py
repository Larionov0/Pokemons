from rest_framework import serializers
from auth_sys.models import UserProfile
from Pokemons.models import Pokemon


class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ['id', 'name']


class UserProfileSerializer(serializers.ModelSerializer):
    pokemons = PokemonSerializer(many=True, read_only=True)

    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'pokemons']
