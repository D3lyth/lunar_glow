from django.shortcuts import render, redirect
from .forms import SubscriberForm

def sign_up(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')
    else:
        form = SubscriberForm()
    return render(request, 'newsletter/sign_up.html', {'form': form})

def thank_you(request):
    return render(request, 'newsletter/thank_you.html')
