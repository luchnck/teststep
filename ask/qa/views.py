from django.shortcuts import render

from django.http import HttpResponse

from django.template import Context, Template

from models import Question

def test(request, *args, **kwargs):
	return HttpResponse('OK')

def latest(request, *args, **kwargs):
	questions = Question.objects.all().order_by('added_at')[:10]
	c = Context({"questions" : questions})
	return render_to_response('qa/latest.html')
	

# Create your views here.
