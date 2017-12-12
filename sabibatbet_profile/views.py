from django.shortcuts import render

# Create your views here.
response = {}

def index(request):
    html = 'sabibatbet_profile/sabibatbet_profile.html'
    return render(request, html, response)
