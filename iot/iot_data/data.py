from iot.common_functions import *

'''

Data for schema

{
	'_id':ObjectId,
	'schema_id':ObjectId
	other data values
}

'''

def get_all(schema_id):
	data = IOT_DATA.find({'schema_id':ObjectId(schema_id)})
	dehydrated_data = []
	for d in data:
		dehydrated_data.append(dehydrate(d))
	return dehydrated_data
	
def get(_id):
	data = IOT_DATA.find_one({'_id':ObjectId(_id)})
	return dehydrate(data)

def post(payload):
	payload['schema_id'] = ObjectId(schema_id)
	IOT_DATA.insert_one(payload)
	return dehydrate(payload)

def put(payload):
	_id = payload['_id']
	payload.pop('_id',None)
	payload['schema_id'] = ObjectId(schema_id)
	IOT_DATA.replace_one({'_id':ObjectId(_id)},payload)
	return get(_id)

def dehydrate(data):
	data = loads(dumps(data))
	data['_id'] = data['_id']['$oid']
	data['schema_id'] = data['schema_id']['$oid']
	return schema


