user = 'maria'
password = 'pass'
host = 'db'
database = 'animal'

COCKROACH = {
    'engine': 'cockroachdb',
    'username': 'root',
    'password': '',
    'host': host,
    'db_name': database,
}

MYSQL = {
    'engine': 'mariadb+pymysql',
    'username': user,
    'password': password,
    'host': host,
    'db_name': database,
}

POSTGRESQL = {
    'engine': 'postgresql',
    'username': user,
    'password': password,
    'host': host,
    'db_name': database,
}

SQLSERVER = {
    'engine': 'mssql+pymssql',
    'username': 'sa',
    'password': 'z!x<?oB1ab',
    'host': host,
    'db_name': 'master',
}

SQLALCHEMY = {
  'autocommit': False,
  'autoflush': False,
  'sessionmaker': [False, False],
  'debug': False,
}
