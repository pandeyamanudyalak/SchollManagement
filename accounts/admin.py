from django.contrib import admin
from accounts import models

admin.site.register(models.CustomUser)
admin.site.register(models.College)