from django.forms import ModelForm
from .models import messageModel

#this class is created so that to provide form for adding todo
class messageForm(ModelForm):
	#specify what class and what model it would be working with
	class Meta:#specify what class we are working with
		model=messageModel
		fields=['title','receiver']#these are feature from model that we will set



