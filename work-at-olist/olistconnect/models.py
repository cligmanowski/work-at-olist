# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.text import slugify

# Create your models here.
class Channel(models.Model):

	name = models.CharField(max_length=20,unique=True)


class Category(models.Model):

	name = models.CharField(max_length=20)
	slug = models.SlugField()
	categoryChannel = models.ForeignKey(
		Channel,
		on_delete = models.CASCADE,
		null=True,
	)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Category, self).save(*args, **kwargs)


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
		null=True,
		related_name="descendant",
	)

	def setAncestor(self,Category=None):
		self.ancestor=Category

	def setDescendant(self,Category):
		self.descendant=Category
