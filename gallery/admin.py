from django.contrib import admin
from  .models import *
# Register your models here.

class galleryModelAdmin(admin.ModelAdmin):
	list_display=["gid","type_data","address","name"]

	class Meta:
		model=gallery_data

admin.site.register(gallery_data,galleryModelAdmin)
