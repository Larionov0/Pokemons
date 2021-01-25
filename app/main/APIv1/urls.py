from django.urls import path
from . import views

app_name = 'APIv1'
urlpatterns = [
    path('get_users/', views.users)
]

