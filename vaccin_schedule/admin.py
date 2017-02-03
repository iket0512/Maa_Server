from django.contrib import admin
from .models import vaccin_data


class vaccinModelAdmin(admin.ModelAdmin):
	list_display=["name"]
	
	class Meta:
		model=vaccin_data

admin.site.register(vaccin_data,vaccinModelAdmin)

# Register your models here.
