import boto3

print('Loading function')
def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name='us-east-1')
    #colocar o id da instancia a ser parada ou uniciada
    instances = ['i-sua-instancia']

    if event['action'] == 'start':
        ec2.start_instances(InstanceIds=instances)
        print('instacias iniciadas: ' + str(instances))
    elif event['action'] == 'stop':
        ec2.stop_instances(InstanceIds=instances)
        print('instancias paradas: ' + str(instances))
    else:
        print('acao nao programada')
