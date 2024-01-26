# import the JSON utility package
import json
# import the Python math library
import math

# import the AWS SDK (for Python the package name is boto3)
import boto3
# import two packages to help us with dates and date formatting
from time import gmtime, strftime

# create a DynamoDB object using the AWS SDK
dynamodb = boto3.resource('dynamodb')
# use the DynamoDB object to select our table
table = dynamodb.Table('casestudyDb')
# store the current time in a human readable format in a variable
now = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())

# define the handler function that the Lambda service will use an entry point
def lambda_handler(event, context):

# extract the two numbers from the Lambda service's event object
    print(event)
    if event.get('name'):
        print("name=", event['name'])
        # write result and time to the DynamoDB table using the object we instantiated and save response in a variable
        response = table.put_item(
                    Item={
                    'ID': event['id'],
                    'name': event['name'],
                    'location': event['location'],
                    'org': event['org'],
                    'salary': event['salary'],
                    'LatestGreetingTime':now
                    })
        # return a properly formatted JSON object
        return {
        'statusCode': 200,
        'body': json.dumps('Employee Id created Successfully:' + str(event['id']))
        }
    else:
        print("id=", event['id'])
        response = table.get_item(Key={'ID':str(event['id'])})
        print("response=",response)
        mathResult=response['Item']
        
        # return a properly formatted JSON object
        return {
        'statusCode': 200,
        'body': json.dumps('Employee Id created Successfully:' + str(mathResult))
        }