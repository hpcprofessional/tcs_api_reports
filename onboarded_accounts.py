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

cloud_accounts=set()

for project in projects: 
    print ("Processing project: "+project_names[project])
    url = "https://cloud.tenable.com/cns/api/v1/projects/" + project
    response = requests.get(url, headers=headers)
    project_data = json.loads(response.content)
    

    if project_data["cloud_accounts"] != []:
        list = project_data["cloud_accounts"]
        for i in list: 
         cloud_accounts.add(i["cloud_account_name"])

##
#
# Write it out
#
##

filename = 'cloud_accounts.txt'
accounts_file = open (r"reports/" + filename,'w')

for i in cloud_accounts:
     accounts_file.write(i + os.linesep)

accounts_file.close()
