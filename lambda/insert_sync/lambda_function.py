from common.db_accessor import DynamoDbAccess

ERROR_RETURN = {
    'Request_Error' : {
        'statusCode': 400,
        'body': {
            'request is Injustice'
        }
    },
    'Process_Error': {
        'statusCode': 500,
        'body': {
            'Process Error!!'
        }
    }
}

def lambda_handler(event, content):
    request_json = event['body']

    if 'user_id' not in request_json or 'user_name' not in request_json:
        return ERROR_RETURN['Reqest_Error']

    insert_data = {
        'user_id': request_json['user_id'],
        'user_name': request_json['user_name']
    }

    if 'pass' in request_json:
        insert_data['pass'] = request_json['pass']

    print(insert_data)

    try:
        DynamoDbAccess().insert(table_name='users', insert_data=insert_data)
    except:
        return ERROR_RETURN['Process_Error']

    return {
        'statusCode': 200,
        'body': {
            'content': 'Request Acceptance Complete',
            'message': request_json
        }
    }