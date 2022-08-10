import json

def bytes_to_json(bytes_object):
	'''
	Converts a bytes object obtained from response content (requests module) as
		JSON object.
	'''
	json_object = json.loads(bytes_object.decode('utf-8'))
	return json_object

def print_json(json_object, indent=4, sort=False):
	'''
	Displays a json object for printing.
	'''
	print(json.dumps(json_object, indent=indent, sort_keys=sort))
