from django import forms
from qa.models import Question,Answer
import re

class AskForm(forms.Form):
	title = forms.CharField(max_length=255)
	text = forms.CharField(widget=forms.Textarea)
	
#	def clean(self):
#		title = self.cleaned_data['title']
#		if (title == string.empty):
#			raise forms.ValidationError(u'title is empty!')
#		return title

	def save(self):
		question = Question(**self.cleaned_data)
		question.author_id = 1
		question.save()
		return question

class AnswerForm(forms.Form):
	text = forms.CharField(widget=forms.Textarea)
	
	def save(self, **kwargs):
		answer = Answer(**self.cleaned_data)
		question_id = re.findall(r'/question/(\d+)/',kwargs['HTTP_REFERER'])
		answer.author_id = 1
		answer.question_id = int(question_id[0]) 
		answer.save()
		return answer
 
