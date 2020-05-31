from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from . models import users,active_period


import json

# Create your views here.

class userList(APIView):
    def get(self,request):
        all_users = users.objects.all()
        user_list=[]
        for user in all_users:
            user_activity=active_period.objects.all().filter(user_id=user.user_id)
            activity_list=[]
            for activity in list(user_activity):
                activity_list.append({"start_time": activity.start_time,"end_time": activity.end_time})
            user_list.append({
            "id": user.user_id,
			"real_name": user.real_name,
			"tz": user.tz,
			"activity_periods": activity_list})
            
        return  HttpResponse (json.dumps({"ok":"true","members":user_list}))
