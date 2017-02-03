from __future__ import unicode_literals

from django.db import models

class vaccin_data(models.Model):
	name= models.CharField(max_length=120, blank=True, null= True)
	describe=models.CharField(max_length=160, blank=True,null= True)
	date=models.DateTimeField()
	modified= models.DateTimeField(auto_now=True,auto_now_add=False)
	created= models.DateTimeField(auto_now=False,auto_now_add=True)

	def __unicode__(self):
		return str(self.name)
# Create your models here.
