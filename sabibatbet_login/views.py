from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from .models import User
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

@csrf_exempt 
def add_session(request):
	if request.method == 'POST':
		name = request.POST['name']
		id = request.POST['id']
		request.session['user_login']= id
		request.session['name'] = name
		try:
			user = User.objects.get(id = id)
		except Exception as e:
			user = User()
			user.id = id
			user.name = name
			user.save()
		return HttpResponseRedirect(reverse('sabibatbet-login:index'))

def remove_session(request):
	request.session.flush()
	return HttpResponseRedirect(reverse('sabibatbet-login:index'))


def login_mahasiswa(request):
	response['login'] = False
	html = 'sabibatbet_login/login_mahasiswa.html'

	return render(request, html, response)