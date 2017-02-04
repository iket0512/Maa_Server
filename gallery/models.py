from __future__ import unicode_literals

from django.db import models

# Create your models here.
class gallery_data(models.Model):
	gid=models.IntegerField(primary_key=True)
	type_data=models.IntegerField(default=0)
	address=models.CharField(max_length=160)
	name=models.CharField(max_length=160)