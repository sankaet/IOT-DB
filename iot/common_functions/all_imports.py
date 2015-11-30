from pymongo import MongoClient
from bson import ObjectId
from bson.json_util import dumps
from json import loads

client = MongoClient('localhost', 27017)

IOT_DB = client.iot_db
IOT_SCHEMAS = IOT_DB.iot_schemas
IOT_DATA = IOT_DB.iot_data