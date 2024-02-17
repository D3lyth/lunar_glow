from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import ScentProfile, ProductScent


def scent_selection_view(request, scent_profile):
    # Attempt to retrieve the scent profile from the database
    scent_profile_instance = get_object_or_404(ScentProfile, name=scent_profile)
    # Retrieve associated ProductScents for the scent profile
    associated_ProductScents = ProductScent.objects.filter(scentoptions=scent_profile_instance)

    context = {
        'scent_profile': scent_profile,
        'ProductScents': associated_ProductScents,
    }

    # Render the template with the retrieved data
    return render(request, 'scentselection.html', context)



def scent_profile_choices(request):
    scentoptions = ScentProfile.objects.all()
    return render(request, 'scentoptions.html', {'scentoptions': scentoptions})
