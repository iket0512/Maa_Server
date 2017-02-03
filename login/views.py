from django.shortcuts import render
from .models import *


def fcm_call(request):
	device = FCM.objects.all().first()
	device.send_message("Title", "Message")
# Create your views here.
