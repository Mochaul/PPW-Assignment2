from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Tanggapan
from sabibatbet_forum.models import Post
from sabibatbet_login.models import User

# Create your views here.
def index(request):
    if request.method == "POST":
      company_id = "-1"
      if 'user_login' in request.session:
        user = User.objects.filter(id=request.session['user_login']).first()
        company_id = user.company
      post = Post.objects.filter(id=request.POST["post_id"]).first()
      tanggapan = Tanggapan(post_id=post, name=company_id, content=request.POST["content"])
      tanggapan.save()
      return HttpResponseRedirect('/sabibatbet_login/')
