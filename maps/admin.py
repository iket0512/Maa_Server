from django.contrib import admin
from .models import map_data

# Register your models here.

class mapModelAdmin(admin.ModelAdmin):
	list_display=["latitude","longitude","name","mobile"]

	class Meta:
		model=map_data

admin.site.register(map_data,mapModelAdmin)
