"""task_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
	1. Add an import:  from my_app import views
	2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
	1. Add an import:  from other_app.views import Home
	2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
	1. Import the include() function: from django.conf.urls import url, include
	2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from task_app.views import ProjectView, ProjectDetailsView, TaskView, TaskDetailsView, UserList

urlpatterns = [
	url(r'^admin/', admin.site.urls),

	url(r'^api/v1/users/', UserList.as_view(), name='user_list'),

	url(r'^api/v1/project/(?P<project_id>\d+)/', ProjectDetailsView.as_view(), name='project_details'),
	url(r'^api/v1/project/', ProjectView.as_view(), name='project'),
	
	url(r'^api/v1/task/(?P<project_id>\d+)/(?P<task_id>\d+)/', TaskDetailsView.as_view(), name='task_details'),
	url(r'^api/v1/task/(?P<project_id>\d+)/', TaskView.as_view(), name='task'),
]
