from django.urls import path
from .import views

urlpatterns = [
   # path('admin/', admin.site.urls),
   
   

    #todo
    path('sendmessage/',views.sendmessage,name="sendmessage"),
    #path('receivedmessage/',views.receivedmessage,name="receivedmessage"),
    #path('sentmessage/',views.sentmessage,name="sentmessage"),
    path('viewmessage/',views.viewmessage,name="viewmessage"),
    #path('viewmessage/',views.viewmessage,name="viewmessagehome"),
    #path('',views.home,name='home_todo'),
    #path('todo/<int:todo_pk>',views.viewtodo,name="viewtodo"),
    #path('todo/<int:todo_pk>/complete',views.completetodo,name="completetodo"),
    #path('todo/<int:todo_pk>/delete',views.deletetodo,name="deletetodo"),
]