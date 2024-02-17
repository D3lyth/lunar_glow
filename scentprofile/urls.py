from django.urls import path, include
from . import views
from .views import scent_selection_view

urlpatterns = [
    path('', views.scent_profile_choices, name='scentprofile'),
    path('scentprofile/<int:scentprofile_id>/', views.scent_selection_view, name='scentselection'),
]