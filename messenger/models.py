from django.db import models

# Create your models here.


from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class messageModel(models.Model):
	#title=models.CharField(max_length=200,blank=True,default="123")
	title=models.TextField(blank=True,null=True)
	#sent=models.TextField(blank=True,null=True)#it means having blank memeo is totally fine
	#created=models.DateTimeField(auto_now_add=True,blank=True,Default=False)#it means that it fixes time of its creation and it couldnot be changed
	#once it is set it cannot be changed
	sender=models.ForeignKey(User,on_delete=models.CASCADE,null=True)#title is sender
	receiver=models.CharField(blank=True,max_length=200)
	date1=models.DateTimeField(null=True,blank=True)
	#name=models

	def __str__(self):
		return self.title
		#this function show name of title in admin page

