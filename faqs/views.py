from django.shortcuts import render
from .models import FAQ_QA  
from django.urls import reverse 

def all_faqs(request):
    url = reverse('faqs')
    faqs = FAQ_QA.objects.all()  
    return render(request, 'faqs/faqs.html', {'faqs': faqs})

