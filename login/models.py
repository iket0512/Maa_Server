from __future__ import unicode_literals

from django.db import models

# Create your models here.

class FCM(models.Model):
	fcm=models.CharField(default="0",max_length=120,null=False,blank=False)
	
