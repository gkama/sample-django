from django.urls import path
from persona import views

urlpatterns = [
    path('persona', views.persona, name='persona'),
]