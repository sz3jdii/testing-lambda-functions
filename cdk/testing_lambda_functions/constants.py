from typing import Final

from aws_cdk import aws_lambda

SERVICE_NAME: Final[str] = 'TestingLambdaFunctions'
SERVICE_ROLE_ARN: Final[str] = 'ServiceRoleArn'
LAMBDA_BASIC_EXECUTION_ROLE: Final[str] = 'AWSLambdaBasicExecutionRole'
SERVICE_ROLE: Final[str] = 'ServiceRole'
CREATE_LAMBDA: Final[str] = 'CreateOrder'
LAMBDA_LAYER_NAME: Final[str] = 'common'
API_HANDLER_LAMBDA_MEMORY_SIZE: Final[int] = 128  # MB
API_HANDLER_LAMBDA_TIMEOUT: Final[int] = 10  # seconds
POWERTOOLS_SERVICE_NAME: Final[str] = 'POWERTOOLS_SERVICE_NAME'
POWERTOOLS_TRACE_DISABLED: Final[str] = 'POWERTOOLS_TRACE_DISABLED'
POWER_TOOLS_LOG_LEVEL: Final[str] = 'LOG_LEVEL'
BUILD_FOLDER: Final[str] = '.build/lambdas/'
COMMON_LAYER_BUILD_FOLDER: Final[str] = '.build/common_layer'

LAMBDA_ARCHITECTURE: Final[aws_lambda.Architecture] = aws_lambda.Architecture.ARM_64
LAMBDA_RUNTIME: Final[aws_lambda.Runtime] = aws_lambda.Runtime.PYTHON_3_12
