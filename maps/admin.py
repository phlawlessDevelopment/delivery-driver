from django.contrib import admin
from .models import Settings,Address
# Register your models here.

admin.site.register((Settings,Address))