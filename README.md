# python-web-flask-api-sqlserver-to-multi-node-elasticsearch-client-without-ssl-pop

## Description
Reads a multi node cluster for data in `pop-demo` document.

Uses `pop` table then covverts it to json for
elasticsearch to use.

## Tech stack
- python
    - flask
    - elasticsearch
    - elasticsearch_dsl
    - pymssql
    - sqlalchemy
- elasticsearch
- kibana
- mssql

## Docker stack
- python
- elasticsearch
- kibana
- mcr.microsoft.com/mssql/server:2017-CU17-ubuntu

## To run
`sudo ./install.sh -u`
- Get all beverages: http://localhost/pop
  - Schema id, name, and color
- Query with params: http://localhost/pop/id/<id>

## To stop
`sudo ./install.sh -d`

## For help
`sudo ./install.sh -h`

## Credit
- [Docker setup](https://lynn-kwong.medium.com/all-you-need-to-know-about-using-elasticsearch-in-python-b9ed00e0fdf0)
- [Search setup](https://www.elastic.co/guide/en/elasticsearch/client/python-api/master/examples.html)