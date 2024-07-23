import base64
import json
import os
from urllib.parse import quote_plus

import boto3
import pymongo
from botocore.exceptions import ClientError
from dotenv import load_dotenv

from SecretManager import get_secret


class DocumentDB:
    def __init__(self):
        load_dotenv()
        self.secret = get_secret(os.getenv('DOCUMENTDB_SECRET'), os.getenv('REGION_NAME'))
        # print(os.getenv('REGION_NAME'))
        # print(self.secret)

    def build_client(self, localHost=False):
        endpoint = os.getenv("DOCUMENT_ENDPOINT_LOCALHOST") if localHost else os.getenv("DOCUMENTDB_ENDPOINT_AWS")
        http_parameters_string = os.getenv("DOCUMENTDB_ENDPOINT_LOCALHOST_PARAMETERS") if localHost else os.getenv(
            "DOCUMENTDB_ENDPOINT_AWS_PARAMETERS")

        port_number = os.getenv("DOCUMENTDB_PORT")
        password = quote_plus(self.secret["password"])
        username = quote_plus(self.secret["username"])
        URL = f'mongodb://{username}:{password}@{endpoint}:{port_number}/{http_parameters_string}'
        return pymongo.MongoClient(URL)
