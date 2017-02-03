from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import requests	
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def welcome(request):
	if(request.method=='GET'):
		response_body={}
		try:
			response_body['success']=True
			response_body['message']="Welcome data"
			response_body['image_url']=request.scheme+'://'+request.get_host()+'/media/welcome/welcome.png'
		except Exception,e:
			response_body['success']=True
			response_body['message']="Error"

		return JsonResponse(response_body)