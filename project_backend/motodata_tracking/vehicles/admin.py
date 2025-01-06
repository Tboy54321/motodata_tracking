from django.contrib import admin

# Register your models here.
from .models import Vehicle
from .models import Tasks

admin.site.register(Vehicle)
admin.site.register(Tasks)