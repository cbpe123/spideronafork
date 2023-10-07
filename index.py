import json
import datetime


def handler(event, context):
    data = {
        'output': 'Hello World Hello World Again',
        'timestamp': datetime.datetime.utcnow().isoformat()
    }
    f = open('map-test.html', 'r')
    # f = open('Rocket.html', 'r')
    # f = open('test.html', 'r')
    response = {
    "statusCode": 200,
    "body": f.read(),
    "headers": {
        'Content-Type': 'text/html',
    }
    }
    f.close()
    return response
    # return {'statusCode': 200,
    #         'body': json.dumps(data),
    #         'headers': {'Content-Type': 'application/json'}}

