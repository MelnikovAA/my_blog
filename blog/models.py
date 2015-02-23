from django.db import models
from django.contrib.auth.models import *

class Comment(models.Model):
    likes = models.IntegerField() 
    content = models.TextField()
    created = models.DateTimeField()
    article_key = models.ForeignKey('Article')
    
    def __unicode__(self):
        return self.content

    def get_absolute_url(self):
        return "/article/%i/" % self.id


class Article(models.Model):
    title = models.CharField( max_length=255)
    content = models.TextField()
    created = models.DateTimeField()
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name='+')
    
    description = models.CharField(blank=True, max_length=255)
    likes = models.IntegerField()
    
    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/article/%i/" % self.id

