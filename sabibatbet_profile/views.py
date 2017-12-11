from django.shortcuts import render

# Create your views here.
response = {}

def show_profile(request):
    return render(request, 'sabibatbet_profile.html', response)
