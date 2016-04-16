from django.contrib.sessions.models import Session
import datetime

class CheckSessionMiddleware():
	def process_request(self,request):
		try:
			sessid = request.COOKIES.get('sessionid')
			session = Session.objects.get(
				session_key=sessid, 
				expire_date__gt=datetime.datetime.now(),
			)
			request.session = session
			request.user = session.session_data
		except:
			request.session = None
			request.user = None
