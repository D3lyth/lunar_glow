from django.shortcuts import render, redirect
from .forms import SubscriberForm


def sign_up(request):
    form = SubscriberForm(request.POST or None) 
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('thank_you')

    return render(request, 'newsletter/sign_up.html', {'form': form})


def thank_you(request):
    return render(request, 'newsletter/thank_you.html')
