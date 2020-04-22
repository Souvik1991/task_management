# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import Http404
from django.conf import settings
# from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
# from rest_framework.exceptions import APIException

from .models import Projects, Tasks
from .serializers import ProjectSerializer, ProjectDetailsSerializer, TaskSerializer, TaskDetailsSerializer, ProjectTaskSerializer

# Create your views here.
class ProjectView(APIView):
	permission_classes = (AllowAny,)
	serializer_class = ProjectSerializer
	# Get all projects
	def get(self, request):
		# print 1
		data = Projects.objects.all()
		serializer = ProjectSerializer(data, many=True)
		return Response(serializer.data)

	# Create new project
	def post(self, request):
		serializer = ProjectSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectDetailsView(APIView):
	permission_classes = (AllowAny,)
	serializer_class = ProjectDetailsSerializer
	
	def get_object(self, project_id):
		try:
			return Projects.objects.get(id=project_id)
		except Publisher.DoesNotExist:
			raise Http404

	# Get details of a project
	def get(self, request, project_id):
		project = self.get_object(project_id)
		serializer = ProjectDetailsSerializer(project)
		return Response(serializer.data)

	# Update project details
	def put(self, request, project_id):
		project = self.get_object(project_id)
		serializer = ProjectDetailsSerializer(project, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	# Delete a project
	def delete(self, request, project_id):
		project = self.get_object(project_id)
		project.delete()
		return Response({"status": True}) 


class TaskView(APIView):
	permission_classes = (AllowAny,)
	serializer_class = TaskSerializer

	def get_project(self, project_id):
		try:
			return Projects.objects.get(id=project_id)
		except Projects.DoesNotExist:
			raise Http404

	# Get all tasks under a project
	def get(self, request, project_id):
		project = self.get_project(project_id)
		data = Tasks.objects.filter(project=project, parent_task=0)
		serializer = ProjectTaskSerializer(data, many=True)
		return Response(serializer.data)

	# Create a task under a project
	def post(self, request, project_id):
		serializer = TaskSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetailsView(APIView):
	permission_classes = (AllowAny,)
	serializer_class = TaskDetailsSerializer

	def get_project(self, project_id):
		try:
			return Projects.objects.get(id=project_id)
		except Projects.DoesNotExist:
			raise Http404

	def get_task(self, project_id, task_id):
		try:
			project = self.get_project(project_id)
			return Tasks.objects.get(project=project, id=task_id)
		except Tasks.DoesNotExist:
			raise Http404

	# Get details of a task
	def get(self, request, project_id, task_id):
		task = self.get_task(project_id, task_id)
		serializer = ProjectTaskSerializer(task)
		return Response(serializer.data)

	# Update data of an exising task
	def put(self, request, project_id, task_id):
		task = self.get_task(project_id, task_id)
		serializer = TaskDetailsSerializer(task, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	# Delete an already present tasks
	def delete(self, request, project_id, task_id):
		task = self.get_task(project_id, task_id)
		task.delete()
		return Response({"status": True}) 

