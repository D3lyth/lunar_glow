from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import ScentProfile, ProductScent
from products.models import Product


def scent_selection_view(request, scentprofile_id):
    # Attempt to retrieve the scent profile from the database
    scent_profile_instance = get_object_or_404(ScentProfile, id=scentprofile_id)
    # Retrieve associated ProductScents for the scent profile
    associated_ProductScents = Product.objects.filter(scent_profile=scent_profile_instance.id)

    context = {
        'scent_profile': scent_profile_instance,
        'ProductScents': associated_ProductScents,
    }

    # Render the template with the retrieved data
    return render(request, 'scentselection.html', context)



def scent_profile_choices(request):
    scentoptions = ScentProfile.objects.all()
    return render(request, 'scentoptions.html', {'scentoptions': scentoptions})


