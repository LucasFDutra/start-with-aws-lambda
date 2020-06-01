import json


def hello(event, context):
    body = {
        "message": "hello you!!!!!!!!!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

