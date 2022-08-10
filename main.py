#!/usr/bin/env python3

import sys
import requests
import argparse as ap

from requests.auth import HTTPBasicAuth

from utils import bytes_to_json
from utils import print_json

if __name__ == '__main__':
	# Argument Parser
	parser = ap.ArgumentParser(description="Open napari for annotating the specified image path")
	parser.add_argument('-i', '--image', help="path to image for annotation", required=True)
	args = vars(parser.parse_args())

	# Get the image path
	img_path = args['image']

	#url = 'https://api.github.com/users/glc-personal'
	url = 'https://api.github.com/users/'

	# Make a get request for the specified URL
	response = requests.get(url)

	# Check the status code for the response received
	success = True if response.status_code == 200 else False

	# Obtain the content of the response
	if success:
		json_object = bytes_to_json(response.content)
		html_url = json_object['html_url']
		repos_url = json_object['repos_url']

		# Make a request to get the public repository names for this user
		response = requests.get(repos_url)
		
		# Check the status code for the response received
		success = True if response.status_code == 200 else False

		# Obtain the content of the response
		if success:
			repos = bytes_to_json(response.content)
			for repo in repos:
				name = repo['name']
				print(f"Repository Name: {name}")
	else:
		print(f"ERROR: status code {response.status_code} is not OK")
		sys.exit("...exiting")
