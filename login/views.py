from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect, HttpResponse
import requests
from customs.sms import send_sms
from django.http import JsonResponse
from django.shortcuts import render_to_response, render
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login(request):
	response_json={}
	try:
		if(request.method=='POST'):
			fcm=str(request.POST.get('fcm'))
			name=str(request.POST.get('name'))
			mobile=str(request.POST.get('mobile'))
			otp=random.randint(100000,999999)
			msg='Hope you have a good health.You One Time Password is '+str(otp)
			send_sms(mobile,msg)
			print 'Otp Sent'
			try:
				otp_list=otp_data.objects.get(mobile=str(mobile))
		 		setattr(otp_list,'otp',int(otp))
		 		setattr(otp_list,'flag',False)
		 		setattr(otp_list,'fcm',fcm)
		 		otp_list.save()
				print 'old user'
				print 'User Details Updated'
		
			except Exception,e:
		 		otp_data.objects.create(mobile=str(mobile),otp=int(otp))
		 		user_data.objects.create(
					name=name,
					email=email,
					mobile=str(mobile)
					)
				print 'User Created'
				print e
			response_json['success']=True
			response_json['message']="Otp Sent Successfully"	
	except Exception, e:
		response_json['success']=False
		response_json['message']='Unable to send otp at this time'

	print str(response_json)
	return JsonResponse(response_json)

@csrf_exempt
def verify(request):
	response_json={}
	try:
		mobile=str(request.POST.get("mobile"))
		otp=str(request.POST.get("otp"))

		otp_list=otp_data.objects.get(mobile=mobile)
		if otp_list.otp == int(otp):
			setattr(otp_list,'flag',True)
			access_token= jwt.encode({'mobile':str(mobile)}, '999123', algorithm='HS256')
			otp_list.save()
			response_json['access_token']=str(access_token)
			print 'Access Token Created'
			response_json['success']=True
			response_json['message']='Successful'
		else:
			response_json['success']=False
			response_json['message']='Invalid Otp'
	except Exception,e:
		response_json['success']=False
		response_json['message']='Invalid Mobile Number'
		print e
	print str(response_json)
	return JsonResponse(response_json)
















# def fcm_call(request):
# 	device = FCM.objects.all().first()
# 	device.send_message("Title", "Message")
# Create your views here.
