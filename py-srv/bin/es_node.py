import logging
from typing import Any, Dict, Optional
from elasticsearch import Elasticsearch
from elasticsearch_dsl.connections import connections
from flask import Flask, _app_ctx_stack, current_app  # type: ignore

from data import DOC, INDEX_NAME

logging.basicConfig(level=logging.INFO)

class Cluster():
    def __init__(self, app:Flask) -> None:
        self.hive = [
            Node(app, "es1"),
            Node(app, 'es2'),
            Node(app, 'es3')
        ]

    def search_by_id(self, i):
        return [
        {
            node.server_name : node.search_by_id(i)
        } for node in self.hive]
        

    def get_all(self):
        return [
        {
            node.server_name : node.get_all()
        } for node in self.hive]
    
class Node():
    server_name = ''

    def __init__(self, app:Flask, server) -> None:
        self.server_name = server
        conn = ElasticsearchProxy(app, server)
        self.es = conn.connect()
        logging.info(self.es.ping())
        self.seed()

    def seed(self):
        for record in DOC:
            resp=self.es.index(index=INDEX_NAME, id=record['id'], document=record)
            logging.info("from {} seed: {}".format(self.server_name, resp['result']))

    def search_by_id(self, i):
        resp=self.es.get(index=INDEX_NAME, id=i)
        logging.info("from {} search_by_id: {}".format(self.server_name, resp['_source']))
        return resp['_source']

    def get_all(self):
        SELECT_ALL = {"match_all": {}}
        result = []
        self.es.indices.refresh(index=INDEX_NAME)
        resp=self.es.search(index=INDEX_NAME, query=SELECT_ALL, size=5)
        logging.info("from {} get_all_hits: {}".format(self.server_name, resp['hits']['total']['value']))
        for hit in resp['hits']['hits']:
            logging.info("from {} get_all: {}".format(self.server_name, hit["_source"]))
            result.append(hit["_source"])
        return result
    
class ElasticsearchProxy:
    """Proxy for Elasticsearch connection that works with Flask.

    Documentation for Elasticseach:
      https://elasticsearch-py.readthedocs.io

    Documentation for Elasticseach DSL:
      https://elasticsearch-dsl.readthedocs.io
    """

    def __init__(self, app: Flask, server):
        self.app = app
        self.server = server
        if app is not None:
            self.init_app(app)

    def init_app(self, app: Flask) -> None:
        app.config.setdefault('ELASTICSEARCH_HOST', self.server)
        app.config.setdefault('ELASTICSEARCH_TIMEOUT', 30)
        app.config.setdefault('ELASTICSEARCH_USERNAME', 'elasticsearch')
        app.config.setdefault('ELASTICSEARCH_PASSWORD', 'changeme')

        app.teardown_appcontext(self.teardown)

    def connect(self) -> Elasticsearch:

        host = self.server
        if not host:
            raise RuntimeError(
                'Cannot connect to elastic search without a host')

        options: Dict[str, Any] = {
            'hosts': [host],
        }

        username = 'elasticsearch'
        password = 'changeme'

        if username and password:
            options['http_auth'] = (username, password)

        timeout = 10
        if timeout is not None:
            options['timeout'] = timeout

        return connections.create_connection(**options)

    def teardown(self, exception: Optional[Exception]) -> None:
        ctx = _app_ctx_stack.top
        if hasattr(ctx, 'elasticsearch'):
            connections.remove_connection('default')
            ctx.elasticsearch = None
