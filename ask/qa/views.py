from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import Context, Template
from models import Question,Answer
from django.core.paginator import Paginator
from forms import AskForm,AnswerForm

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
	if (request.method == "GET"):
		addAnswer = AnswerForm()
	else:
		return HttpResponse("OK")

	try:
		question = Question.objects.get(pk=questionId)
	except Question.DoesNotExist:
		raise Http404
	answers = Answer.objects.filter(question=question)
	c = {	
		"question" : question,
		"answers" : answers,
		"addAnswer" : addAnswer,
		}	
	return render(request,'single.html', c)


def ask(request, *args, **kwargs):
	if (request.method == 'GET'):
		form = AskForm()
	else:
		form = AskForm(request.POST)
		if (form.is_valid()):
			post = form.save()
			url = post.get_absolute_url()
			return HttpResponseRedirect(url)

	return render(request, 'ask.html',{
		"form": form,
		})

def answer(request, *args, **kwargs):
	if (request.method == "GET"):
		return HttpResponseRedirect("/")
	
	answer = AnswerForm(request.POST)
	if answer.is_valid():
		answer = answer.save(HTTP_REFERER = request.META.get('HTTP_REFERER'))
		url = answer.get_absolute_url()
		return HttpResponseRedirect(url)
	else:
		return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# Create your views here.
