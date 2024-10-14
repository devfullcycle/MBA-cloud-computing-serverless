import json

print('Loading function')
def lambda_handler(event, context):
    body = ""
    statusCode = 200

    if 'httpMethod' in event and 'resource' in event:
        rota = str(event['httpMethod']) + ' '+ str(event['resource'])
    else:
        body = "Esta funçao devera serchamada via proxy do APi Gateway"
        statusCode = 400
        return {
            'statusCode': statusCode,
            'body': body
        }

    print(json.dumps(event))

    name = event['queryStringParameters']['name']

    if rota == "GET /customer":
        body = "Ola "+name
    else:
        body = "Rota nao implementada"
        statusCode = 500
        return {
            'statusCode': statusCode,
            'body': body
        }
    return {
        'statusCode': statusCode,
        'body': json.dumps(body)
    }