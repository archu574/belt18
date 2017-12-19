# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..app1.models import User
from ..app2.models import Idea
from django.shortcuts import render,redirect
from django import forms

# Create your views here.
def contextfunc(request):
    user = User.objects.get(id=request.session['id'])
    context = {'user': user, 'users': User.objects.all(),
                'lik': Idea.objects.filter(Liked_bys=user),
                'ideaz':Idea.objects.all()}
    return render(request, 'app2/bright_ideas.html', context)

def bright_ideas(request):
    return render(request,'app2/bright_ideas.html')

def addideatodb(request):
    entry=Idea.objects.addidea(request.POST,request.session['id'])
    return redirect('/dashboard')

def logout(request):
    return redirect('/')

def likesindatabase(request, x_id):
    print "adding a Like relationship"
    id = request.session["id"]
    entry = Idea.objects.joinforlikes(id,x_id)
    return redirect('/dashboard')

def contextfunctwo(request):
    user = User.objects.get(id=request.session['id'])
    context = {'user': user, 'users': User.objects.all(),
                'lik': Idea.objects.filter(Liked_bys=user),
                'ideaz':Idea.objects.all()}
    return render(request, 'app2/display.html', context)

def namelink(request):
    return render(request,'app2/display.html')

def wholikes(request):
    user = User.objects.get(id=request.session['id'])
    context = {'user': user, 'users': User.objects.all(),
                'lik': Idea.objects.filter(Liked_bys=user),
                'ideaz':Idea.objects.all()}
    return render(request,'app2/show.html',context)
