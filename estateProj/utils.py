import boto3
import os

# Initialize the Boto3 client for AWS Systems Manager (Parameter Store)
ssm_client = boto3.client('ssm', region_name='eu-west-1')

def get_parameter(parameter_name):
    response = ssm_client.get_parameter(
        Name=parameter_name,
        WithDecryption=True  # If the parameter is stored as a secure string
    )
    return response['Parameter']['Value']