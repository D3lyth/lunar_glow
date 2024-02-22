from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.scent_profile_choices, name='scentprofile'),
]
