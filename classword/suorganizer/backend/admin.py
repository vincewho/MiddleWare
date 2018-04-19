from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(TestLab)
admin.site.register(Manufacturer)
admin.site.register(Product)
admin.site.register(TestResult)
