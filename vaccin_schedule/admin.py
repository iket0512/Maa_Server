from django.contrib import admin
from .models import vaccin_data


class vaccinModelAdmin(admin.ModelAdmin):
	list_display=["name","describe","type_vac"]
	
	class Meta:
		model=vaccin_data

admin.site.register(vaccin_data,vaccinModelAdmin)

# Register your models here.
# houbbnxwogdmzabp