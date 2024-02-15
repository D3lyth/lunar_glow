from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.sign_up, name='newsletter'),
    path('thankyou/', views.thank_you, name='thank_you'),

]
