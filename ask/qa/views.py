from django.shortcuts import render, render_to_response

from django.http import HttpResponse

from django.template import Context, Template

from models import Question

def test(request, *args, **kwargs):
	return HttpResponse('OK')

def latest(request, *args, **kwargs):
	questions = Question.objects.all().order_by('added_at')[:10]
	c = {
		"questions" : questions,
		}
	return render_to_response('latest.html', c)
	

# Create your views here.
