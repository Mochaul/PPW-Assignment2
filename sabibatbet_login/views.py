from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
# Create your views here.
response = {}

def index(request):
	if 'user_login' in request.session:
		response['login'] = True
	else:
		response['login'] = False
	response['author'] = "Kianutama Radianur"
	html = 'sabibatbet_login/home.html'
	return render(request, html, response)


def login_mahasiswa(request):
	response['login'] = False
	html = 'sabibatbet_login/login_mahasiswa.html'

	return render(request, html, response)