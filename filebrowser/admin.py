from django.contrib import admin
from django.conf.urls.defaults import *
from filebrowser import models

class BrowseAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return False  

admin.site.register(models.Browse, BrowseAdmin)
