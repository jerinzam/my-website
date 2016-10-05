from django.shortcuts import render,render_to_response
from django.template import RequestContext
from profiles.models import *
from meetup.models import *
# Create your views here.


def meetups_home(request):
    group = GroupUserDetails.objects.get(user=request.user,active=True)
    meetings = Meeting.objects.filter(group=group)
    return render_to_response("base.html",{},context_instance=RequestContext(request)) 
