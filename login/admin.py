from django.contrib import admin
from .models import *

# Register your models here.


class loginModelAdmin(admin.ModelAdmin):
	list_display=["mobile","fcm","otp","flag"]

	class Meta:
		model=otp_data

admin.site.register(otp_data,loginModelAdmin)