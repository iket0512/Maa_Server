from django.shortcuts import render
from .models import map_data
from django.http import HttpResponseRedirect, HttpResponse
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def map_view(request):
	response_json={}
	try:
		if(request.method=='GET'):
			response_json["success"]=True
			response_json["map_detail"]=[]
			for o in map_data.objects.all():
				temp_json={}
				temp_json["latitude"]=str(o.latitude)
				temp_json["longitude"]=str(o.longitude)
				temp_json["name"]=str(o.name)
				temp_json["mobile"]=str(o.mobile)
				response_json["map_detail"].append(temp_json)

	except Exception,e:
		response_json["success"]=False
		response_json["message"]="data not found"
		
	return JsonResponse(response_json)	

# Create your views here.
