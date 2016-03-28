from __future__ import unicode_literals

from django.contrib.auth.models, import User

from django.db import models

# Create your models here.
class Question(models.model):
	title = models.CharField(max_length=255)
	text = models.TextField()
	added_at = models.DateTimeField()
	rating = models.IntegerField()
	author = models.CharField(max_length=255)
	likes = models.ForeignKey(Likes, on_delete = models.CASCADE)
	
	def __unicode__(self)
		return self.title

	def get_absolute_url(self)
		return 'question/%s/' % self.pk
	
	class Meta:
		db_table = "questions"
		ordering = ['-added_at']

class Answer(models.model):
	text = models.TextField()
	added_at = models.DateTimeField()
	question = models.ForeignKey(Question, on_delete = models.DO_NOTHING)
	author = models.ForeignKey(User, on_delete = models.DO_NOTHING)
	
	def __unicode__(self)
		return self.text

	def get_absolute_url(self)
		return "question/%s/#Answer%s" % self.question.pk self.pk

	class Meta:
		db_table = "answers"
		ordering = ['-added_at']

class Likes(models.model):
	question = ForeignKey(Question, on_delete = models.DO_NOTHING)
	users = ForeignKey(User, on_delete = models.DO_NOTHING)

	class Meta:
		db_table = "likes"
		ordering = ['-question']
