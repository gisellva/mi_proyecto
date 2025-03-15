from django.urls import path
from .views import UsuarioList, UsuarioDetail

urlpatterns = [
    path('usuarios/', UsuarioList.as_view(), name='usuarios-list'),
    path('usuarios/<int:pk>/', UsuarioDetail.as_view(), name='usuarios-detail'),
]
