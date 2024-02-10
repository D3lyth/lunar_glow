from django.shortcuts import render
from .models import FAQ  
from django.urls import reverse 

def all_faqs(request):
    url = reverse('faqs')
    faqs = FAQ.objects.all()  
    return render(request, 'faqs/faqs.html', {'faqs': faqs})

