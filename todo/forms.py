from django.forms import ModelForm
from .models import Todo

#this class is created so that to provide form for adding todo
class TodoForm(ModelForm):
	#specify what class and what model it would be working with
	class Meta:#specify what class we are working with
		model=Todo
		fields=['title','memo','important']#these are feature from model that we will set