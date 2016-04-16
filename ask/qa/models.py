from __future__ import unicode_literals

from django.contrib.auth.models import User

from django.contrib.sessions.models import Session

from django.db import models

from datetime import datetime,timedelta

from django.utils.timezone import now

import time

import hashlib

# Create your models here.
class Question(models.Model):
	title = models.CharField(max_length=255)
	text = models.TextField()
	added_at = models.DateTimeField(auto_now_add=True)
	rating = models.IntegerField(default=0)
	likes = models.IntegerField(default=0)
	author = models.ForeignKey(User, on_delete = models.DO_NOTHING)

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return '/question/%s/' % self.pk
	
	class Meta:
		db_table = "questions"
		ordering = ['-added_at']

class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateTimeField(auto_now_add=True)
	question = models.ForeignKey(Question, on_delete = models.DO_NOTHING)
	author = models.ForeignKey(User, on_delete = models.DO_NOTHING)
	
	def __unicode__(self):
		return self.text

	def get_absolute_url(self):
		return "/question/%s/#Answer%s" % (self.question.pk, self.pk)

	class Meta:
		db_table = "answers"
		ordering = ['-added_at']

def do_login(response, user):
	sessionid = hashlib.md5(user.username + ':' + (datetime.now().microsecond).__str__()).hexdigest()
	session = Session.objects.create(session_key = sessionid, session_data = user.pk, expire_date = datetime.now()+timedelta(days=5))
	return session
