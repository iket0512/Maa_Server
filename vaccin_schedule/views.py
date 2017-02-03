from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect, HttpResponse
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def vaccin(request):
	response_json={}
	try:
		if(request.method=="GET"):
			response_json["success"]=True
			response_json["before"]=[]

			for o in vaccin_data.objects.all():
				if(int(o.type_vac)==int(0)):
					temp_json={}
					temp_json["name"]=str(o.name)
					temp_json["data"]=str(o.describe)
					response_json["before"].append(temp_json)

			response_json["after"]=[]
			for o in vaccin_data.objects.all():
				if(int(o.type_vac)==int(1)):
					temp_json={}
					temp_json["name"]=str(o.name)
					temp_json["data"]=str(o.describe)
					response_json["after"].append(temp_json)

	except Exception,e:
		response_json["success"]=False
		response_json["message"]="data not found"
		
	return JsonResponse(response_json)	




# Create your views here.

