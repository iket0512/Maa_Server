from __future__ import unicode_literals

from django.db import models

class home_data(models.Model):
	title=models.CharField(max_length=160)
	data=models.CharField(max_length=160)
	
# Create your models here.
