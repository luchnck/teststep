from django.db import models

from qa.models import Question,Answer

from django.contrib.auth.models import User

from datetime import datetime

user = User(username='luchnck',email='luchnck@yandex.ru', password='123456')
user.save()
user = User(username='max',email='luchnck@yandex.ru', password='123456')
user.save()

questions = [
	["first","how much is the fish",datetime.now(),0,0,User.objects.get(username="luchnck")],
	["second","WTF 0_o ???", datetime.now(),0,0,User.objects.get(username="max")],
	["third","what is the time now??", datetime.now(),0,0,User.objects.get(username="max")],
	["forth","htw much is the fish",datetime.now(),0,0,User.objects.get(username="luchnck")],
	["fifth","WTF 0_o ???", datetime.now(),0,0,User.objects.get(username="max")],
	["sixth","what is the time now??", datetime.now(),0,0,User.objects.get(username="max")],
	["seventh","how much is the fish",datetime.now(),0,0,User.objects.get(username="luchnck")],
	["eghth","WTF 0_o ???", datetime.now(),0,0,User.objects.get(username="max")],
	["ninegth","what is the time now??", datetime.now(),0,0,User.objects.get(username="max")],
	["tenth","how much is the fish",datetime.now(),0,0,User.objects.get(username="luchnck")],
	["eleven","WTF 0_o ???", datetime.now(),0,0,User.objects.get(username="max")],
	["tvelve","what is the time now??", datetime.now(),0,0,User.objects.get(username="max")],		
	["forteen","how much is the fish",datetime.now(),0,0,User.objects.get(username="luchnck")],
	["sixteenth","WTF 0_o ???", datetime.now(),0,0,User.objects.get(username="max")],
	["eigtheenth","what is the time now??", datetime.now(),0,0,User.objects.get(username="max")],		
			
	]

for question in questions:
	title,text,added_at,rating,likes,author = question
	question=Question(title=title,text=text,added_at=added_at,rating=rating,author=author)
	question.save()

answers = [
	["dorogo",datetime.now(),Question.objects.get(title="first"),User.objects.get(username="max")],
	["togo!togo",datetime.now(),Question.objects.get(title="second"),User.objects.get(username="luchnck")],
	["13:00 o clock!!", datetime.now(),Question.objects.get(title="second"),User.objects.get(username="luchnck")],
	]

for answer in answers:
	text,added_at,question,author = answer
	answer=Answer(text=text,added_at=added_at,question=question,author=author)
	answer.save()


