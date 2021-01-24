from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pokemons/', include('Pokemons.urls')),
    path('auth/', include('auth_sys.urls'))
]
