import boto3
import logging
import json

# Configurar o logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Criar um cliente para o Secrets Manager
secrets_client = boto3.client('secretsmanager')


def lambda_handler(event, context):
    # ID ou nome do segredo que você quer acessar
    secret_name = 'dev/my/secret'

    try:
        # Obter o valor do segredo
        response = secrets_client.get_secret_value(
            SecretId=secret_name
        )

        secret_value = response['SecretString']

        # Logar o valor do segredo
        logger.info(f"Secret Value: {secret_value}")

    except secrets_client.exceptions.ResourceNotFoundException:
        logger.error(f"Secret {secret_name} not found.")
    except Exception as e:
        logger.error(f"Error getting secret {secret_name}: {e}")

    return {
        'statusCode': 200,
        'body': 'Secret logged successfully'
    }
