from django.shortcuts import render,render_to_response
from django.template import RequestContext
from profiles.models import *
from meetup.models import *
# Create your views here.


def meetups_home(request):
    group = GroupUserDetails.objects.get(user=request.user,active=True)
    meetings = Meeting.objects.filter(group=group)
    return render_to_response("base.html",{},context_instance=RequestContext(request)) 

def meeting_details(request,meetup_id):
    meeting = Meeting.objects.get(id=meetup_id)
    meeting_users = GroupUserDetails.objects.filter(group = meeting.group)
    return render_to_response("base.html",{},context_instance=RequestContext(request))

def join_group(request,group_id):
    group = Group.objects.get(id=group_id)
    group_join = GroupUserDetails(group=group,user=request.user)
    group_join.save()
    return 
 
