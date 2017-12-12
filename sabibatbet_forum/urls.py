from django.conf.urls import url
from .views import index, add_post
#url for app
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^add-post/$', add_post, name='add-post'),
]
