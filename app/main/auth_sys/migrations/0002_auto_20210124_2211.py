# Generated by Django 3.1.5 on 2021-01-24 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pokemons', '0002_remove_pokemon_link'),
        ('auth_sys', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='pokemons',
            field=models.ManyToManyField(blank=True, to='Pokemons.Pokemon'),
        ),
    ]
