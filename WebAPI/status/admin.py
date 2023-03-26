import imp
from django.contrib import admin
from .models import Status

class StatusAdmin(admin.ModelAdmin):
    list_display=['user','content','image']
    class Meta:
        model=Status
        
admin.site.register(Status,StatusAdmin)
# Register your models here.
