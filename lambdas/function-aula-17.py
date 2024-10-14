import json

import boto3

print('Loading function')
def lambda_handler(event, context):
    message = json.dumps(event)

    sqs = boto3.client('sqs')
    resp = sqs.send_message(
        QueueUrl="teste-sqs",
        MessageBody=(
          message
        )
    )
    print(resp['MessageId'])
