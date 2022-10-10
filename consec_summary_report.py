#!/usr/bin/env python3

import os #For environment
import requests #for API interaction
import json #API returns JSON, usually

#This controls the column order in the CSV report. It is based on the key names in the JSON returned by the reports API
csv_column_order = [ 'image_name', 'tag', 'created_at', 'os', 'os_version', 'updated_at', 'risk_score', 'malware', 'digest', 'potentially unwanted programs']

accessKey = os.getenv('TENABLE_ACCESS_KEY')
secretKey = os.getenv('TENABLE_SECRET_KEY')

url = "https://cloud.tenable.com/container-security/api/v2/images"

headers = {
    "accept": "application/json",
    "X-ApiKeys": "accessKey=" + accessKey + ";secretKey=" + secretKey
}

response = requests.get(url, headers=headers)
responses=json.loads(response.text)

filename = 'container_security_summary.csv'
summary_report = open(r"reports/" + filename,'w')

#Write first row of CSV
sep=""
for column in csv_column_order:
    summary_report.write(sep+column)
    sep=","


#Loop over responses and add a line for each item, with the data specified in csv_column_order
for item in responses.get("items"):
    summary_report.write('\n')

    url = "https://cloud.tenable.com/container-security/api/v2/reports/" + item.get('repoName') + "/" + item.get('name') +"/" + item.get('tag')
    responses= requests.get(url, headers=headers)
    json_responses = json.loads(responses.text)
    sep=""
    for column_name in csv_column_order:
        summary_report.write(sep+str(json_responses.get(column_name)))
        sep=","
summary_report.close()
