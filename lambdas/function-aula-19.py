import boto3
import logging

# Configurar o logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Criar um cliente SSM
ssm_client = boto3.client('ssm')


def lambda_handler(event, context):
    # Nome do parâmetro que você quer acessar
    parameter_name = 'teste'

    try:
        # Obter o valor do parâmetro
        response = ssm_client.get_parameter(
            Name=parameter_name,
            WithDecryption=True
        )

        parameter_value = response['Parameter']['Value']

        # Logar o valor do parâmetro
        logger.info(f"Parameter Value: {parameter_value}")

    except ssm_client.exceptions.ParameterNotFound:
        logger.error(f"Parameter {parameter_name} not found.")
    except Exception as e:
        logger.error(f"Error getting parameter {parameter_name}: {e}")

    return {
        'statusCode': 200,
        'body': 'Parameter logged successfully'
    }
