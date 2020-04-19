

from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone

# Create your models here.
class feedsModel(models.Model):
	title=models.CharField(max_length=200)
	description=models.TextField(blank=True)#it means having blank memeo is totally fine
	#created=models.DateTimeField(auto_now_add=True,blank=True,Default=False)#it means that it fixes time of its creation and it couldnot be changed
	#once it is set it cannot be changed
	user_new=models.ForeignKey(User,on_delete=models.CASCADE)
	#user = models.OneToOneField(User, on_delete=models.CASCADE,blank)
	image=models.ImageField(upload_to='media/images/',blank=True)
	upvote = models.IntegerField(default=0,blank=True)
	upvoter= models.TextField(blank=True)
	#foreig key stores the relationship between this todo and user
	#any object that is saved in database has id ie unique value for that object
	#now what foreignKey does is it takes id of user and saves here
	def __str__(self):
		return self.title
		#this function show name of title in admin page

