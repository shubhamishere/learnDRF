from django.contrib import admin

# Register your models here.
#my changes starts from here

from home.models import Contact

admin.site.register(Contact)