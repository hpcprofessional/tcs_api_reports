# tcs_api_reports
Examples of getting reports from different components of Tenable.cs using the API. 

* cspm_report.py generates a report for each project configured in Tenable.cs
* consec_summary_report.py generates a report summarizing each container image in Tenable.cs

## Prerequisites

These scripts assumes you have API access to Tenable.io and Tenable.cs (Tenable Cloud Security) hosted at cloud.tenable.com
For more information: https://docs.tenable.com/tenableio/Content/Platform/Settings/MyAccount/GenerateAPIKey.htm
The scripts assume these API Keys are available via OS Environment variables

## Directory Structure

The presense of a ./reports subdirectory (relative to the scripts) is assumed. The scripts will place the generated reports there.

## Future Work and TODO

These scripts currently do not check for errors or exceptions. Further, there is a lot that can be done to traverse the data deeper in the APIs.
