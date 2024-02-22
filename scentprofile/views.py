from django.shortcuts import render
from .models import ScentProfile


def scent_profile_choices(request):
    scentoptions = ScentProfile.objects.all()
    return render(
        request, 'scentoptions.html',
        {'scentoptions': scentoptions})
