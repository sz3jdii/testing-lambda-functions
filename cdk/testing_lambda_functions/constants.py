from typing import Final

SERVICE_NAME: Final[str] = 'TestingLambdaFunctions'
SERVICE_ROLE_ARN = 'ServiceRoleArn'
LAMBDA_BASIC_EXECUTION_ROLE = 'AWSLambdaBasicExecutionRole'
SERVICE_ROLE = 'ServiceRole'
CREATE_LAMBDA = 'CreateOrder'
LAMBDA_LAYER_NAME = 'common'
API_HANDLER_LAMBDA_MEMORY_SIZE = 128  # MB
API_HANDLER_LAMBDA_TIMEOUT = 10  # seconds
POWERTOOLS_SERVICE_NAME = 'POWERTOOLS_SERVICE_NAME'
POWERTOOLS_TRACE_DISABLED = 'POWERTOOLS_TRACE_DISABLED'
POWER_TOOLS_LOG_LEVEL = 'LOG_LEVEL'
BUILD_FOLDER = '.build/lambdas/'
COMMON_LAYER_BUILD_FOLDER = '.build/common_layer'
ENVIRONMENT = 'dev'
