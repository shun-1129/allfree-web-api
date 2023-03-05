def lambda_handler(event, content):
    request_json = event['body']

    print(request_json)

    return {
        'statusCode': 200,
        'body': {
            'content': 'Request Acceptance Complete',
            'message': request_json
        }
    }