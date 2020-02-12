from django.urls import path
from sample_app import views

urlpatterns = [
    path('', views.sample_app, name='sample_app'),
]