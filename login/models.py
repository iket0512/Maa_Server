from __future__ import unicode_literals

from django.db import models

# Create your models here.

class otp_data(models.Model):
	fcm=models.CharField(default="0",max_length=120,null=False,blank=False)
	mobile=models.CharField(max_length=120,default='9174908579', blank=True,null=True)
	otp= models.IntegerField(default=0,null=True)
	flag=models.BooleanField(default=False)
	name=models.CharField(max_length=120,null=True)
	created= models.DateTimeField(auto_now=False,auto_now_add=True)

	def __unicode__(self):
		return str(self.name)
