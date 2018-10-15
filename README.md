This version of filebrowser-no-grappelli has been modified by Imaginary Landscape to work with Django 1.11.

Not the prettiest solution but a dummy Browse model and modelAdmin has been added in order to get Filebrowser to appear in the django admin index without overriding templates.


Installation

1. pip install -e git+git@github.com:ImaginaryLandscape/django-filebrowser-no-grappelli.git#egg=filebrowser-no-grappelli

2. Add 'filebrowser' to your INSTALLED_APPS

3. Add this to the top of your urls conf:
url(r'^admin/filebrowser/', include('filebrowser.urls')), 

In order for the dummy admin index Browse link to work, make sure it's above 
url(r'^admin/', include(admin.site.urls)),
