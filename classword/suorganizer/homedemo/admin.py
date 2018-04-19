from django.contrib import admin
from .models import NameModel, ContactModel, team

# Register your models here.

admin.site.register(NameModel)
admin.site.register(ContactModel)
admin.site.register(team)