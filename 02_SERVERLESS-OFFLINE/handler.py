import json

def hello(event, context):
    print('aplicação serverless rodando tranquilamente')
    response = {
        "statusCode": 200
    }
    return response