from enum import Enum


class TableName(str, Enum):
    api = "api"
    contact = "contact"
    license = "license"
    endpoint = "endpoint"
    schema = "schema"
    parameter = "parameter"
    response = "response"

