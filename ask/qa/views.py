from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import Context, Template
from models import Question,Answer
from django.core.paginator import Paginator
from django.http import Http404

def test(request, *args, **kwargs):
	return HttpResponse('OK')

def latest(request, *args, **kwargs):
	questions = Question.objects.all().order_by('-added_at')
	paginator = Paginator(questions,10)
	page = request.GET.get('page',1)
	paginator.baseurl = '?page='
	page = paginator.page(page)
	c = {
		"paginator" : paginator,
		"page" : page,
		"questions" : page.object_list,
		}
	return render_to_response('latest.html', c)

def most_related(request, *args, **kwargs):
	questions = Question.objects.all().order_by('-rating')
	paginator = Paginator(questions,10)
	page = request.GET.get('page',1)
	paginator.baseurl = "/popular/?page="
	page = paginator.page(page)
	c = {	
		"paginator" : paginator,
		"page" : page,
		"questions" : page.object_list,
		}	
	return render_to_response('related.html', c)

def single(request, *args, **kwargs):
	questionId = int(kwargs['questionId'])
	try:
		question = Question.objects.get(pk=questionId)
	except Question.DoesNotExist:
		raise Http404
	answers = Answer.objects.filter(question=question)
	c = {	
		"question" : question,
		"answers" : answers,
		}	
	return render_to_response('single.html', c)


# Create your views here.
