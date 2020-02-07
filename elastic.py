from elasticsearch import Elasticsearch
from settings import ELASTIC_HOST, ELASTIC_PORT
import logging


def connect_elasticsearch():
    # Elastic Search Connection
    _es = Elasticsearch([
        {
            'host': ELASTIC_HOST,
            'port': ELASTIC_PORT
        }
    ]
    )
    if _es.ping():
        print('Elastic Connected')
    else:
        print('Could not connect')
    return _es


def create_index(es_object, index_name='recipes'):
    created = False
    # index settings
    settings = {
        "settings": {
            "number_of_shards": 1,
            "number_of_replicas": 0
        },
        "mappings": {
            "members": {
                "dynamic": "strict",
                "properties": {
                    "title": {
                        "type": "text"
                    },
                    "submitter": {
                        "type": "text"
                    },
                    "description": {
                        "type": "text"
                    },
                    "calories": {
                        "type": "integer"
                    },
                }
            }
        }
    }
    try:
        if not es_object.indices.exists(index_name):
            # Ignore 400 means to ignore "Index Already Exist" error.
            es_object.indices.create(index=index_name, ignore=400, body=settings)
            print('Created Index')
            created = True
    except Exception as ex:
        print(str(ex))
    finally:
        print('Create status:', created)
        return created


if __name__ == '__main__':
    es = connect_elasticsearch()
    created_index = create_index(es)
    logging.basicConfig(level=logging.ERROR)
