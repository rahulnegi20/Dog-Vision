from django.contrib import admin
from .models import Info
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(Info, ImageAdmin)    