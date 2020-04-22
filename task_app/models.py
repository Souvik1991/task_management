# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Projects(models.Model):
	name = models.CharField(max_length=250)
	description = models.TextField(default="")
	start_date = models.DateField(default=datetime.now)
	end_date = models.DateField(default=datetime.now)
	avatar = models.ImageField(blank=False, null=False, upload_to='static/')

	class Meta:
		db_table = 'projects'

	def __str__(self):
		return "%s" % (self.name)


class Tasks(models.Model):
	project = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='tasks')
	name = models.CharField(max_length=250)
	description = models.TextField(default="")
	start_date = models.DateField(default=datetime.now)
	end_date = models.DateField(default=datetime.now)
	asigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
	parent_task = models.BigIntegerField(default=0)

	class Meta:
		db_table = 'tasks'

	def __str__(self):
		return "%s - %s" % (self.project, self.name)