from django.shortcuts import render
from .models import Post
from sabibatbet_login.models import User

# Create your views here.

response = {}
def index(request):
    user = User.objects.filter(id=request.session['user_login']).first()
    response['company_id'] = user.company
    response['posts'] = Post.objects.filter(company_id=user.company)
    html = 'forum.html'
    return render(request, html, response)

def add_post(request):
    if(request.method == POST):
        post = Post(company_id=response['company_id'],content=response['content'])
        post.save()
        return HttpResponseRedirect('/forum/')
