from django.shortcuts import render
from .models import FAQCategory, FAQ_QA

def all_faqs(request):
    # Fetch all FAQ categories
    categories = FAQCategory.objects.all()

    # Fetch all FAQs
    faqs = FAQ_QA.objects.all()

    # Create a dictionary to hold categories and their associated FAQs
    categories_with_faqs = {}

    # Populate the dictionary with categories and their associated FAQs
    for category in categories:
        # Filter FAQs belonging to the current category
        category_faqs = faqs.filter(faq_category=category)
        categories_with_faqs[category] = category_faqs

    # Pass the dictionary to the template context
    context = {
        'categories_with_faqs': categories_with_faqs
    }

    return render(request, 'faqs/faqs.html', context)

