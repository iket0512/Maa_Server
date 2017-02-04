from __future__ import unicode_literals

from django.db import models

# Create your models here.
class map_data(models.Model):
	latitude=models.DecimalField(max_digits=10,decimal_places=7)
	longitude=models.DecimalField(max_digits=10,decimal_places=7)
	name=models.CharField(max_length=120,blank=False)
	mobile=models.CharField(max_length=10,blank=True,null=True)

	def __unicode__(self):
		return str(self.name)


