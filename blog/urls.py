
#Here we're importing Django's function 
#url and all of our views from blog application
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]
#As you can see, we're now assigning a view 
#called post_list to ^$ URL.