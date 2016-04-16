from django import forms
from qa.models import Question,Answer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from pprint import pprint
import re

class AskForm(forms.Form):
	title = forms.CharField(max_length=255)
	text = forms.CharField(widget=forms.Textarea)
	_user = 0 
#	def clean(self):
#		title = self.cleaned_data['title']
#		if (title == string.empty):
#			raise forms.ValidationError(u'title is empty!')
#		return title

	def save(self):
		question = Question(**self.cleaned_data)
		question.author_id = self._user
		question.save()
		return question

class AnswerForm(forms.Form):
	text = forms.CharField(widget=forms.Textarea)
	question = forms.IntegerField()	
	_user = 0

	def save(self, **kwargs):
		answer = Answer(**self.cleaned_data)
#		question_id = re.findall(r'/question/(\d+)/',kwargs['HTTP_REFERER'])
		answer.author_id = self._user
#		answer.question_id = int(question_id[0]) 
		answer.save()
		return answer


class SignupForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)
	email = forms.EmailField()
	
	def clean_username(self):
		user = User.objects.filter(username = self.cleaned_data['username'])
		count = user.count()
		if (count == 0):		
			return self.cleaned_data['username']	 
		else:	
			raise forms.ValidationError(u'%s user already exists!' % self.cleaned_data['username'])

	def save(self, **kwargs):
		username = self.cleaned_data['username']
		password = self.cleaned_data['password']
		email = self.cleaned_data['email']
		user = User.objects.create_user(username,email,password)
		return user


class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget = forms.PasswordInput)
	
