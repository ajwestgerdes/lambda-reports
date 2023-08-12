import boto3
import datetime
from create_excel import create_excel

lambda_client = boto3.client('lambda')
logs_client = boto3.client('logs')

function_name_list = []
last_invocation_list = []
last_modified_list = []
code_size_list = []
runtime_list = []
description_list = []

def handler():
    #Iterate through every lambda function we have
    response = lambda_client.list_functions()
    for function in response['Functions']:
        function_name = function['FunctionName']
        last_log_date = get_last_log_date(function_name)
        config = get_function_configuration(function_name)
        function_name_list.append(function_name)
        last_invocation_list.append(last_log_date)
        last_modified_list.append(config["LastModified"].split("T")[0])
        code_size_list.append(config["CodeSize"])
        runtime_list.append(config["Runtime"])
        description_list.append(config["Description"])
    create_excel({
        "function_name": function_name_list,
        "last_invocation": last_invocation_list,
        "last_modified": last_modified_list,
        "code_size": code_size_list,
        "runtime": runtime_list,
        "description": description_list
    })


def get_last_log_date(function_name):
    response = logs_client.describe_log_groups(logGroupNamePrefix='/aws/lambda/' + function_name)
    log_group = response['logGroups']
    if log_group:
        timestamp_datetime = datetime.datetime.fromtimestamp(log_group[0]['creationTime'] / 1000)
        now = datetime.datetime.now()
        time_difference = now - timestamp_datetime
        return int(time_difference.total_seconds() / (60 * 60 * 24))
    else:
        return None

#Get all other lambda configuration stats
def get_function_configuration(function_name):
    response = lambda_client.get_function(FunctionName=function_name)
    if response:
        return response['Configuration']
    return None

handler()