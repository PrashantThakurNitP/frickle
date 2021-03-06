"""fricle URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from posts import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path("feeds/",views.feeds,name="feeds"),
    path("",views.home,name="home"),
    path("signupuser",views.signupuser,name="signupuser"),
    path('logoutuser/',views.logoutuser,name="logoutuser"),
    path('loginuser/',views.loginuser,name="loginuser"),
    path('addpost/',views.addpost,name="addpost"),
    path('upvote/<int:id1>/<str:up>/',views.upvote,name="upvote"),  #changed in upvote fn in views.py and feeds.html in upvote link
    path('delete/<int:id1>/',views.delete,name="delete"), 
    path('todo/', include('todo.urls')),
    path('messenger/', include('messenger.urls')),

    #path('addpost/',views.addpost,name="addpost"),
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

