from rest_framework import serializers

from .models import Projects, Tasks
from django.contrib.auth.models import User

class ProjectSerializer(serializers.ModelSerializer):
	name = serializers.CharField(required=True, allow_blank=False, max_length=250)
	description = serializers.CharField(required=True, allow_blank=False)
	start_date = serializers.DateField(required=True)
	end_date = serializers.DateField(required=True)
	avatar = serializers.ImageField(allow_empty_file=False, use_url=True)

	def create(self, validated_data):
		"""
		Create a return a new `Project` instance, given the validated data
		"""
		return Projects.objects.create(**validated_data)

	class Meta:
		model = Projects
		fields = "__all__"


class ProjectTaskSerializer(serializers.ModelSerializer):
	subtasks = serializers.SerializerMethodField()

	def get_subtasks(self, task):
		qs = Tasks.objects.filter(parent_task=task.id, project=task.project)
		serializer = ProjectTaskSerializer(instance=qs, many=True)
		return serializer.data

	class Meta:
		model = Tasks
		fields = ("id", "project", "name", "description", "start_date", "end_date", "asigned_to", "subtasks")


class ProjectDetailsSerializer(serializers.ModelSerializer):
	id = serializers.IntegerField(read_only=True)
	name = serializers.CharField(required=True, allow_blank=False, max_length=250)
	description = serializers.CharField(required=True, allow_blank=False)
	start_date = serializers.DateField(required=True)
	end_date = serializers.DateField(required=True)
	avatar = serializers.ImageField(allow_empty_file=True)
	# tasks = ProjectTaskSerializer(many=True, read_only=True)
	tasks = serializers.SerializerMethodField()

	def get_tasks(self, project):
		qs = Tasks.objects.filter(parent_task=0, project=project)
		serializer = ProjectTaskSerializer(instance=qs, many=True)
		return serializer.data

	def update(self, instance, validated_data):
		instance.name = validated_data.get('name')
		instance.description = validated_data.get('description')
		instance.start_date = validated_data.get('start_date')
		instance.end_date = validated_data.get('end_date')
		instance.avatar = validated_data.get('avatar')
		instance.save()
		return instance

	class Meta:
		model = Projects
		fields = ('id', 'name', 'description', 'start_date', 'end_date', 'avatar', 'tasks')


class TaskSerializer(serializers.ModelSerializer):
	project = serializers.PrimaryKeyRelatedField(allow_null=False, queryset=Projects.objects.all())
	name = serializers.CharField(required=True, allow_blank=False, max_length=250)
	description = serializers.CharField(required=True, allow_blank=False)
	start_date = serializers.DateField(required=True)
	end_date = serializers.DateField(required=True)
	asigned_to = serializers.PrimaryKeyRelatedField(allow_null=False, queryset=User.objects.all())
	parent_task = serializers.IntegerField(required=False, default=0)

	def create(self, validated_data):
		"""
		Create a return a new `Project` instance, given the validated data
		"""
		return Tasks.objects.create(**validated_data)

	class Meta:
		model = Tasks
		fields = '__all__'


class TaskDetailsSerializer(serializers.ModelSerializer):
	project = serializers.PrimaryKeyRelatedField(allow_null=False, queryset=Projects.objects.all())
	name = serializers.CharField(required=True, allow_blank=False, max_length=250)
	description = serializers.CharField(required=True, allow_blank=False)
	start_date = serializers.DateField(required=True)
	end_date = serializers.DateField(required=True)
	asigned_to = serializers.PrimaryKeyRelatedField(allow_null=False, queryset=User.objects.all())
	parent_task = serializers.IntegerField(required=False, default=0)

	def update(self, instance, validated_data):
		instance.name = validated_data.get('name')
		instance.description = validated_data.get('description')
		instance.start_date = validated_data.get('start_date')
		instance.end_date = validated_data.get('end_date')
		instance.asigned_to = validated_data.get('asigned_to')
		instance.parent_task = validated_data.get('parent_task')
		instance.save()
		return instance

	class Meta:
		model = Tasks
		fields = '__all__'
