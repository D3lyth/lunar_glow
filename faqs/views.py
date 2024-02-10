from django.shortcuts import render
from .models import FAQ

def faq_list(request):
    faqs = FAQ.objects.all()  # Assuming you have a FAQ model
    return render(request, 'faqs/faqs.html', {'faqs': faqs})
