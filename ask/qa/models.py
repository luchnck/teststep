from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Question(models.model)
	title = models.CharField(max_length=255)
	text = models.TextField()
	added_at = models.DateTimeField()
	rating = models.IntegerField()
	author = models.CharField(max_length=255)
	likes = models.ForeignKey(Likes, on_delete=models.CASCADE)
	
	def __unicode__(self)
		return self.title

	def get_absolute_url(self)
		return 'question/%s/' % self.pk
	
	class Meta:
		db_table = "questions"
		ordering = ['-creation_date']

