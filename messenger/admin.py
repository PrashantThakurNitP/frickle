

# Register your models here.
from django.contrib import admin
from .models import messageModel
# Register your models here.
#it says to add readonly field created to admin
admin.site.register(messageModel)