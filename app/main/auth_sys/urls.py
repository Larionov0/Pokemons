from django.urls import path
from . import views

app_name = 'auth_sys'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('login_handler/', views.login_handler, name='login_handler'),
    path('register', views.login, name='register'),
    path('logout', views.logout, name='logout')
]
