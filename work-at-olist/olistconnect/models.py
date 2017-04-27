# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Channel(models.Model):

	name = models.CharField(max_length=20)


class Category(models.Model):

	name = models.CharField(max_length=20)
	categoryChannel = models.ForeignKey(
		Channel,
		on_delete = models.CASCADE,
		null=True,
	)


class CategoryPath(models.Model):

	ancestor = models.ForeignKey(
		Category,
		on_delete = models.CASCADE,
		null=True,
		related_name="ancestor",
	)

	descendant = models.ForeignKey(
		Category,
		on_delete = models.CASCADE,
		related_name="descendant",
	)

	def setAncestor(self,Category=None):
		ancestor=Category

	def setDescendant(self,Category):
		descendant=Category
