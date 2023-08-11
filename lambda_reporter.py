import boto3
import datetime

client = boto3.client('lambda')

def handler(event, context):
    #Iterate through every lambda function we have
    response = client.list_functions()
    for function in response['Functions']:
        function_name = function['FunctionName']
        #Find the last date for each cloudwatch log and get days since
        last_log_date = get_last_log_date(function_name)
        print(last_log_date)
        if last_log_date:
            print(f"{function_name}: {last_log_date}")
        else:
            print(f"{function_name}: No logs found")

def get_last_log_date(function_name):
    response = client.list_functions()
    functions = [f for f in response['Functions'] if f['FunctionName'] == function_name]
    if functions:
        function_arn = functions[0]['FunctionArn']
        response = client.list_tags(Resource=function_arn)
        log_group_name = [t['Value'] for t in response['Tags'] if t['Key'] == 'LogGroup'][0]
        response = client.filter_log_events(
            logGroupName=log_group_name,
            startTime=int((datetime.datetime.now() - datetime.timedelta(days=7)).timestamp() * 1000),
            endTime=int(datetime.datetime.now().timestamp() * 1000),
            filterPattern='""',
            limit=1
        )
        if response['Events']:
            last_event = response['Events'][0]
            last_event_time = datetime.datetime.fromtimestamp(last_event['Timestamp'] / 1000)
            return last_event_time.date()
    return None

#Get all other lambda configuration stats
def get_function_configuration(function_name):
    response = client.get_function(FunctionName=function_name)
    if response:
        return response['Configuration']
    return None

    #Put all data into a list of dicts and dump to excel file

    #Upload excel file to s3