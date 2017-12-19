# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..app1.models import User
from django.db import models

# Create your models here.
class IdeaManager(models.Manager):
    def addidea(self,data,id):
        print "this is the ideamanager route"
        user=User.objects.get(id=id)
        ideas=self.create(idea=data['ideatyped'],userid=user)
        ideas.Liked_bys.add(user)
        ideas.save()
        return ideas

    def joinforlikes(self,id,x_id):
        joinedlikez=Idea.objects.get(id=x_id)
        joineduser=User.objects.get(id=id)
        joinedlikez.Liked_bys.add(joineduser)
        joinedlikez.save()


class Idea(models.Model):
    idea = models.TextField(max_length=5000)
    Liked_bys =models.ManyToManyField(User, related_name='liked')
    userid = models.ForeignKey(User, related_name="relation")#this related name is what the connection is named between the user table with this table
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    objects = IdeaManager()
    def counts(self):
        return self.Liked_bys.all().count()
