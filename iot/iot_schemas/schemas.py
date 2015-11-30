from iot.common_functions import *

'''

Schema is the raw DB for data

{
	'_id':ObjectId,
	'client':int,
	other schema fields
}

'''

def get_all(client):
	schemas = IOT_SCHEMAS.find({'client':client})
	dehydrated_schemas = []
	for s in schemas:
		dehydrated_schemas.append(dehydrate(s))
	return dehydrated_schemas
	
def get(_id):
	schema = IOT_SCHEMAS.find_one({'_id':ObjectId(_id)})
	return dehydrate(schema)

def post(payload):
	IOT_SCHEMAS.insert_one(payload)
	return dehydrate(payload)

def put(payload):
	_id = payload['_id']
	payload.pop('_id',None)
	IOT_SCHEMAS.replace_one({'_id':ObjectId(_id),'client':payload['client']},payload)
	return get(_id)

def dehydrate(schema):
	schema = loads(dumps(schema))
	schema['_id'] = schema['_id']['$oid']
	return schema


