from django.forms import ModelForm
from .models import feedsModel

#this class is created so that to provide form for adding todo
class feedsForm(ModelForm):
	#specify what class and what model it would be working with
	class Meta:#specify what class we are working with
		model=feedsModel
		fields=['title','description','image']#these are feature from model that we will set



