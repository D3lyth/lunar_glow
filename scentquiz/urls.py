from django.urls import path
from . import views

urlpatterns = [
    path('scentquiz/', views.quiz, name='scentquiz'),
]