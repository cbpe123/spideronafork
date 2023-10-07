import json
import datetime


def handler(event, context):
    data = {
        'output': 'Hello World Hello World Again',
        'timestamp': datetime.datetime.utcnow().isoformat()
    }
    response = {
    "statusCode": 200,
    "body": open('test.html', 'r').read(),
    "headers": {
        'Content-Type': 'text/html',
    }
    }
    return response
    # return {'statusCode': 200,
    #         'body': json.dumps(data),
    #         'headers': {'Content-Type': 'application/json'}}

