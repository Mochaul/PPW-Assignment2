from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from .models import User
# Create your views here.
response = {}

def index(request):
	html = 'sabibatbet_login/home.html'
	return render(request, html, response)

@csrf_exempt 
def add_session(request):
	if request.method == 'POST':
		name = request.POST['name']
		id = request.POST['id']
		company =request.POST['companyID']
		request.session['user_login']= id
		request.session['name'] = name
		try:
			user = User.objects.get(id = id)
		except Exception as e:
			user = User()
			user.id = id
			user.name = name
			user.company = company
			user.save()
		return HttpResponseRedirect(reverse('sabibatbet-login:index'))

def remove_session(request):
	request.session.flush()
	return HttpResponseRedirect(reverse('sabibatbet-login:index'))