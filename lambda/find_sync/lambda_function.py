import json
from common.db_accessor import DynamoDbAccess

def lambda_handler(event, content):
    request_json = event['body']

    flag = True

    if flag is True:
        documents = DynamoDbAccess().search('users', 'user_id',request_json['user_id'])
    else:
        documents = DynamoDbAccess().get_table_list_all()

    result = {
        'result': documents
    }
    # data_type = type(result)

    return {
        'statusCode': 200,
        'body': {
            'content': 'Request Acceptance Complete',
            'message': result
        }
    }