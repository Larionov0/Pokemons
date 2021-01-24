from django.db import models
from django.contrib.auth.models import User
from Pokemons.models import Pokemon


class UserProfile(models.Model):
    user = models.OneToOneField(User, models.CASCADE)
    pokemons = models.ManyToManyField(Pokemon, blank=True)

