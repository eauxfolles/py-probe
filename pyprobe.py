#!/usr/bin/env python3
# ==============================================================================
# Name: pyprobe.py (Python Probe)
# Version: v4 (alpha)
# Author: eauxfolles
# Date: 12.08.2020
# Description: Script to check if HTTP and HTTPS domains are resolving. 
# Usage: "probe.py <source> <target>"
# ==============================================================================

import sys
import socket
import requests

source_file = False
target_file = False
source_list = []
target_list = []
process_list = []

# function to validate input provided with command line (has to be 1 or 3 parameters or -help/--help)
def validate_command_line():

	source_file = False

	# validate correct use of calling an options or parameter and set variable
	if len(sys.argv) < 2:
		print("error: no parameters provided")
		exit()
	elif len(sys.argv) > 3:
		print("error: too many parameters provided")
		exit()
	elif sys.argv[1] == "-help" or sys.argv[1] == "--help":
		print("usage: httpyprobe.py <source> <target>")
		exit()
	elif len(sys.argv) == 3:
		source_file = sys.argv[1]
		target_file = sys.argv[2]
	else:
		print("error: please check correct usage of parameters")
		exit()

	return source_file, target_file

# function to load entries from source-file into variable
def load_list():

	with open(source_file) as f: 
		source_list = [line.rstrip() for line in f.readlines()]

	return source_list

# function to write validated entries to target-file
def write_list(target_list):

	with open(target_file, 'w') as f: 
		for y in target_list:
			f.write(y + '\n')

# function to probe for http (port 80) and https (port 443) of each entry
def probe(single_entry, protocol): 

	single_entry_url = protocol + single_entry

	try:
		response = requests.get(single_entry_url, timeout=5, allow_redirects=False)
		if response.status_code == 200: 
			print(response.url + " resolved")
		elif (response.status_code == 301) or (response.status_code == 302):
			print(response.url + " redirected to " + str(response.headers['Location']))
			response.url = response.headers['Location']
		else: 
			print(response.url + " caused " + response.status_code)
		if response.url not in target_list:
			target_list.append(response.url) 
	except requests.Timeout:
		print(single_entry_url + " request timed out")
		pass
	except requests.ConnectionError:
		print(single_entry_url + " url does not resolve")
		pass
	except:
		pass

source_file, target_file = validate_command_line()
source_list = load_list()

for i in source_list:
	probe(i, "http://")
	probe(i, "https://")

write_list(target_list)
