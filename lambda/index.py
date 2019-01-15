import json

def lambda_handler(event, context):
    print(json.dumps(event))

    return {
        'statusCode': 200,
        'body': 'Hello World!'
    }
