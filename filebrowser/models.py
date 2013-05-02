# This file is a silly hack to get the filebrowser browse view to appear 
# in django's admin index

from django.db import models

class Browse(models.Model):  

    class Meta:
        verbose_name_plural = "Browse"
