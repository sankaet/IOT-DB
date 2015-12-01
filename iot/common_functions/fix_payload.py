'''

Here the payload is type casted. Optional and required values

'''

import traceback

def fixPayload(sample_payload,data,request):
  try:
    #typecast
    fixed_payload = formatPayload(data,sample_payload)
    #check if required fields are present
    formatPayload(sample_payload,data)
    return fixed_payload
  except Exception as e:
    raise Exception(e)

def formatPayload(payload,sample_payload):
  try:
    if not type(payload) == dict:
      raise Exception('PayloadError: Payload not formatted correctly')
    payload = formatDict(payload,sample_payload)
    return payload
  except KeyError as e:
    raise Exception('KeyError: {0}. Explanation: Adding/Removing this key should resolve this error.'.format(e))
  except ValueError as e:
    raise Exception('ValueError: {0}. Explanation: The supplied data type is incorrect. Please check the docs to make sure that you are sending the value in the correct type.'.format(e))
  except Exception as e:
    error = traceback.format_exc()
    raise Exception('PayloadError: {0}. sample_payload: {1}'.format(error,str(sample_payload)))



def formatList(payload,sample_payload):
  i = 0
  for type_sec_payload in payload:
    if type(type_sec_payload) == list:
      payload[i] = formatList(payload[i],sample_payload[0])
    elif type(type_sec_payload) == dict:
      payload[i] = formatDict(payload[i],sample_payload[0])
    else:
      payload[i] = formatStd(payload[i],sample_payload[0])
    i=i+1
  return payload

def formatDict(payload,sample_payload):
  for key in payload.keys():
    if type(sample_payload[key]) == list:
      payload[key] = formatList(payload[key],sample_payload[key])
    elif type(sample_payload[key]) == dict:
      payload[key] = formatDict(payload[key],sample_payload[key])
    else:
      payload[key] = formatStd(payload[key],sample_payload[key])
  return payload

def formatStd(payload,sample_payload):
  expected_type = type(sample_payload)
  payload = expected_type(payload)
  return payload