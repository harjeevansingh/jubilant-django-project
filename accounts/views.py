from django.shortcuts import render


def home(request):
    return render(request, 'accounts/home.html')


def contact_us(request):
    return render(request, 'accounts/contact_us.html')
