from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core import serializers
import json
from .models import Post
from sabibatbet_login.models import User

# Create your views here.

response = {}
def index(request):
    if 'user_login' in request.session:
      user = User.objects.filter(id=request.session['user_login']).first()
      response['company_id'] = user.company
      response['posts'] = serializers.serialize('json',Post.objects.filter(company_id=user.company))
      html = 'forum.html'
      return render(request, html, response)
    else:
      return HttpResponseRedirect(reverse('sabibatbet-login:index'))

def add_post(request):
    if(request.method == "POST"):
        user = User.objects.filter(id=request.session['user_login']).first()
        company_id = user.company
        post = Post(company_id=company_id,content=request.POST['content'])
        post.save()
        return HttpResponseRedirect('/sabibatbet_forum/')
