from iot.models import Client

def auth_client(request):
	try:
		client_id = request.META['HTTP_X_IOT_CLIENT'].split('|')[0]
		client_secret = request.META['HTTP_X_IOT_CLIENT'].split('|')[1]
		client = Client.objects.get(client_id=client_id,client_secret=client_secret)
		request.client = client
		return True
	except:
		return False