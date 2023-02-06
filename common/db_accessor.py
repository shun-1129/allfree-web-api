import boto3


class DynamoDbAccess:
    ENDPOINT_URL = ''


    def __init__(
        self,
        endpoint_url: str or None = None
    ):
        if endpoint_url is None:
            self.dynamodb = boto3.resource('dynamodb')
        else:
            self.ENDPOINT_URL = endpoint_url
            self.dynamodb = boto3.resource('dynamodb', self.ENDPOINT_URL)


    def get_table_list_all(self) -> list:
        document = list(
            self.dynamodb.tables.all()
        )
        return document if document is not None else []


    def create_table(
        self,
        table_name: str,
        key_schema: list,
        attr_defin: list
    ):
        result = self.dynamodb.create_table(
            TableName = table_name,
            KeySchema = [
                key_schema_data
                for key_schema_data in key_schema
            ],
            AttributeDefinitions = [
                attr_defin_data
                for attr_defin_data in attr_defin
            ],
            BillingMode = 'PAY_PER_REQUEST'
        )