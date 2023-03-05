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


    def get_table_list_all(self):
        documents = (
            self.dynamodb.tables.all()
        )

        print(type(documents))

        return documents


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


    def search(
        self,
        table_name: str,
        primary_key: str,
        search_primary_key: str
    ) -> any:
        table = self.dynamodb.table(table_name)
        result = table.get_item(
            key={
                primary_key: search_primary_key
            }
        )
        return result


    def insert(
        self,
        table_name: str,
        insert_data: dict or list[dict]
    ):
        table = self.dynamodb.Table(table_name)

        if type(insert_data) == dict:
            table.put_item(Item=insert_data)
        
        if type(insert_data) == list:
            for data in insert_data:
                table.put_item(Item=data)
