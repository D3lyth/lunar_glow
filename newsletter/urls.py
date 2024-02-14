from django.urls import path, include
from . import views

urlpatterns = [
    path('newsletter/', views.sign_up, name='newsletter'),

]
