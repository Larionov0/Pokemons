from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pokemons/', include('Pokemons.urls')),
    path('auth/', include('auth_sys.urls')),
    path('', RedirectView.as_view(url='/pokemons/main', permanent=True)),
    path('api/v1/', include('APIv1.urls'))
]
