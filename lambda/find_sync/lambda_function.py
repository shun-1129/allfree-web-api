import json
from common.db_accessor import DynamoDbAccess

def lambda_handler(event, content):
    request_json = event['body']

    print(request_json)

    result = {
        'result': DynamoDbAccess().get_table_list_all()
    }
    # data_type = type(result)

    return {
        'statusCode': 200,
        'body': {
            'content': 'Request Acceptance Complete',
            'message': {'result': 'data'}
        }
    }