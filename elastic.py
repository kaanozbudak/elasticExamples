from elasticsearch import Elasticsearch
from settings import ELASTIC_HOST, ELASTIC_PORT

# Elastic Search Connection
es = Elasticsearch([
    {
        'host': ELASTIC_HOST,
        'port': ELASTIC_PORT
    }
]
)
