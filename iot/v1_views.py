from django.http import HttpResponse
from django.test import RequestFactory
from django.core import serializers
from django.shortcuts import render_to_response
import json
import traceback
import requests
from iot.models import *
from iot import iot_data
from iot import iot_schemas
from iot import common_functions
# Create your views here.

TRACEBACK_ENABLED = True

def exception_wrapper(func):
	def func_wrapper(*args, **kwargs):
		try:
			return HttpResponse(func(*args, **kwargs),content_type="application/json")
		except Exception as e:
			tb = traceback.format_exc()
			response = {
			'success':False,
			'error':{
					'str':str(e),
					'type':type(e).__name__
					}
			}
			if TRACEBACK_ENABLED: response['error']['traceback'] = tb
			response = json.dumps(response)
			return HttpResponse(response,content_type="application/json",status=400)
	return func_wrapper

class IncorrectMethod(Exception):
	pass

class InvalidClient(Exception):
	pass

@exception_wrapper
def schemas(request):
	if request.method not in ['GET','POST']:
		raise IncorrectMethod('{0} method not allowed'.format(request.method))
	if not common_functions.auth_client(request):
		raise InvalidClient('Invalid client credentials supplied')
	if request.method == 'GET':
		response = json.dumps(iot_schemas.get_all(request.client.id))
	elif request.method == 'POST':
		payload = json.loads(request.body)
		payload['client'] = request.client.id
		response = json.dumps(iot_schemas.post(payload))

	return HttpResponse(response,content_type="application/json")

@exception_wrapper
def schema_by_id(request,schema_id):
	if request.method not in ['GET','PUT']:
		raise IncorrectMethod('{0} method not allowed'.format(request.method))
	if not common_functions.auth_client(request):
		raise InvalidClient('Invalid client credentials supplied')
	if request.method == 'GET':
		response = json.dumps(iot_schemas.get(schema_id))
	elif request.method == 'PUT':
		payload = json.loads(request.body)
		payload['_id'] = schema_id
		payload['client'] = request.client.id
		response = json.dumps(iot_schemas.put(payload))

	return HttpResponse(response,content_type="application/json")

@exception_wrapper
def data(request,schema_id):
	if request.method not in ['GET','POST']:
		raise IncorrectMethod('{0} method not allowed'.format(request.method))
	if not common_functions.auth_client(request):
		raise InvalidClient('Invalid client credentials supplied')
	if request.method == 'GET':
		response = json.dumps(iot_data.get_all(schema_id,request.client.id))
	elif request.method == 'POST':
		payload = json.loads(request.body)
		sample_payload = iot_schemas.get(schema_id)
		sample_payload['schema_id'] = schema_id
		sample_payload.pop('_id',None)
		payload['client'] = request.client.id
		payload['schema_id'] = schema_id
		payload = common_functions.fixPayload(sample_payload,payload,request)
		response = json.dumps(iot_data.post(payload))

	return HttpResponse(response,content_type="application/json")

@exception_wrapper
def data_by_id(request,schema_id,data_id):
	if request.method not in ['GET','PUT']:
		raise IncorrectMethod('{0} method not allowed'.format(request.method))
	if not common_functions.auth_client(request):
		raise InvalidClient('Invalid client credentials supplied')
	if request.method == 'GET':
		response = json.dumps(iot_data.get(data_id,schema_id,request.client.id))
	elif request.method == 'PUT':
		payload = json.loads(request.body)
		sample_payload = iot_schemas.get(schema_id)
		sample_payload['schema_id'] = schema_id
		payload['client'] = request.client.id
		payload['schema_id'] = schema_id
		payload['_id'] = data_id
		payload = common_functions.fixPayload(sample_payload,payload,request)
		response = json.dumps(iot_data.put(payload))

	return HttpResponse(response,content_type="application/json")