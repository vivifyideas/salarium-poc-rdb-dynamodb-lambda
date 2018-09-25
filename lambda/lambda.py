'''
Example lambda function
'''

import json

def lambda_handler(event, context):
    msg = 'Request processed with AWS Lambda - Salarium PoC'
    body = { "message": msg }
    return {
        "statusCode": 200,
        "headers": {
            "x-processed": "lambda"
        },
        "body" : json.dumps(body, separators=(',',':')),
        "isBase64Encoded": False
        }