from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$',views.contextfunc),
    url(r'^bright_ideas$',views.bright_ideas),
    url(r'^ideatyped$',views.addideatodb),
    url(r'^logout$',views.logout),
    url(r'^put_likes_indatabase/(?P<x_id>\d+)$',views.likesindatabase),
    url(r'^namelink$',views.contextfunctwo),
    url(r'^namelink/(?P<uzerid>\d+)$',views.namelink),
    url(r'^wholikes$',views.wholikes),



]
