import boto3
import json
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key


### define service resource

##dynamodb = boto3.resource('dynamodb')

### set variables

##tablename = dynamodb.Table('website-visits')

### Create update function

##def update_site_counter(tablename,value,connection):



### Create handler to execute function

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('website-visits')
    response = table.update_item(
        Key={
        'site':'engebreth.com'
        },
         UpdateExpression= 'ADD numbCount :inc',
            ExpressionAttributeValues={
                ':inc': 1
        },
        ReturnValues="UPDATED_NEW"
    )
    
    # Format dynamodb response into variable
    responseBody = json.dumps({"site": int(float(response["Attributes"]["numbCount"]))})
    
       #API Response Object And Format To JSON
    apiResponse = {
        "isBase64Encoded": False,
        "statusCode": 200,
        "body": responseBody,
        "headers": {
            "Access-Control-Allow-Headers" : "Content-Type,X-Amz-Date,Authorization,X-Api-Key,x-requested-with",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET,OPTIONS" 
        },
    }

    # Return API Response
    return apiResponse