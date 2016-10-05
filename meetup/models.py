from django.db import models
from django.contrib.auth.models import User
from profiles.models import UserProfile
# Create your models here.
#~ 
class Group(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now=True)
    def __unicode__(self):
	return self.name
	
class GroupUserDetails(models.Model):
    group = models.ForeignKey(Group)
    user = models.ForeignKey(UserProfile)
    joined = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    def __unicode__(self):
	return self.group.name 

MEETING_STATUSES = (('1','yet to happen'),('2','happened'),('3','postponed'),('4','cancelled'))
class Meeting(models.Model):
    title = models.CharField(max_length=250)
    group = models.ForeignKey(Group)    
    agenda = models.TextField(blank=True,null=True)
    fees = models.CharField(max_length=5)
    scheduled = models.DateTimeField(blank=True,null=True)
    venue = models.CharField(max_length=200)
    status = models.CharField(max_length=50,choices=MEETING_STATUSES,null=True,blank=True)
    def __unicode__(self):
	return self.title
#~ 
