from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Todo(models.Model):
	title=models.CharField(max_length=100)
	memo=models.TextField(blank=True)#it means having blank memeo is totally fine
	created=models.DateTimeField(auto_now_add=True)#it means that it fixes time of its creation and it couldnot be changed
	#once it is set it cannot be changed
	datecompleted=models.DateTimeField(null=True,blank=True)#it will be filled when someone click complete
	important=models.BooleanField(default=False)#Mark whether it is important or not
	#there can be lot of user and we need to distinguish whether object belong to whom
	#we can do it with foreign relationship
	#ie one to many relationship the term here is foreign key
	#it connects one model with another
	#another model is user model for which we dont write code
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	#foreig key stores the relationship between this todo and user
	#any object that is saved in database has id ie unique value for that object
	#now what foreignKey does is it takes id of user and saves here
	def __str__(self):
		return self.title
		#this function show name of title in admin page