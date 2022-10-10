#!/usr/bin/env python3

import os #For environment
import requests #for API interaction
import json #API returns JSON, usually

bearer = os.getenv('TENABLECS_API_TOKEN')
offset = 0 #Record offset for API
limit = 1000 #Record limit for API

##
#
# Get projects in array to loop through
#
##

url = "https://cloud.tenable.com/cns/api/v1/projects?offset=" + str(offset) + "&limit=" + str(limit)

headers = {
    "accept": "application/json",
    "authorization": "Bearer " + bearer
}

response = requests.get(url, headers=headers)
#TODO: Error checking logic, e.g. HTTP 403/404

projects=[]
project_names={}

responses=json.loads(response.text)
for response in responses:
    projects.append(response.get('id'))
    project_names[response.get('id')]=response.get('name')

##
#
#  Loop through projects
#
##


for project in projects: 
    url = "https://cloud.tenable.com/cns/api/v1/violations?project_id=" + project + "&csv_format=true"

    response = requests.get(url, headers=headers)
    cspm_report = open(r"reports/" + project_names.get(project) + ".csv","w")
    cspm_report.write(response.text)
    cspm_report.close()
