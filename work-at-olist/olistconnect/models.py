# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Channel(models.Model):
	def __init__(self,name):
		self.name = name

	

class Category(models.Model):
	def __init__(self,name):
		self.name = name;

class CategoryPath(models.Model):

	ancestor = models.ForeignKey(
		"Category",
		on_delete = models.CASCADE,
		null=True,
		related_name="ancestor",
	)

	descendant = models.ForeignKey(
		"Category",
		on_delete = models.CASCADE,
		related_name="descendant",
	)
