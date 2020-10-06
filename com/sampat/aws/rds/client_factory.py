import boto3

#
class ClientFactory:
    def __init__(self, client):
        self._client = boto3.client(client, region_name="us-east-1",aws_access_key_id='XXXXXXXXXXXXXXX',aws_secret_access_key='XXXXXXXXXXX')

    def get_client(self):
        return self._client


class RDSClient(ClientFactory):
    def __init__(self):
        super().__init__('rds')


class EC2Client(ClientFactory):
    def __init__(self):
        super().__init__('ec2')