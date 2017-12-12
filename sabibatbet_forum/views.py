from django.shortcuts import render

# Create your views here.

response = {}
def index(request):
    html = 'forum.html'
    return render(request, html, response)
