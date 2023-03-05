import json
from common.db_accessor import DynamoDbAccess

def lambda_handler(event, content):
    request_json = event['body']

    print(request_json)

    result = DynamoDbAccess().get_table_list_all()

    return {
        'statusCode': 200,
        'body': {
            'content': 'Request Acceptance Complete',
            'message': json.dumps(result)
        }
    }