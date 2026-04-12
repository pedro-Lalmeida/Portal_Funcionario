from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('perfil/', views.PerfilView.as_view(), name='perfil'),
    path('painel/', views.PainelView.as_view(), name='painel'),   
]