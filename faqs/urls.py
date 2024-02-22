from django.urls import path
from . import views

urlpatterns = [
    path('faqs/', views.all_faqs, name='faqs'),

]
