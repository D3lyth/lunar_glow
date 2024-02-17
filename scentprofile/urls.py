from django.urls import path, include
from . import views
from .views import scent_selection_view

urlpatterns = [
    path('', views.scent_profile_choices, name='scentprofile'),
    # path('scentprofile/', views.scent_selection_view, name='scentselection'),
    path('scentprofile/<str:scent_profile>/', views.scent_selection_view, name='scentselection'),


]
