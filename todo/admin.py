from django.contrib import admin
from .models import Todo
# Register your models here.
class TodoAdmin(admin.ModelAdmin):
	readonly_fields=('created',)#it says to add readonly field created to admin
admin.site.register(Todo,TodoAdmin)
