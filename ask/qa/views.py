from django.shortcuts import render, render_to_response

from django.http import HttpResponse

from django.template import Context, Template

from models import Question

from django.core.paginator import Paginator

def test(request, *args, **kwargs):
	return HttpResponse('OK')

def latest(request, *args, **kwargs):
	questions = Question.objects.all().order_by('added_at')[:100]
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
	

# Create your views here.
