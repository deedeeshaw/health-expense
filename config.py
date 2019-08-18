# This file contains configuration settings for the application

import os

# The secret key is used by Flask to encrypt session cookies.
SECRET_KEY = 'Ans7o-J8sNm-K1p6s-HvBx3-Wcn19'

# Project ID
PROJECT_ID = 'deeproject-1547084116288'

# Database configuration
# DATA_BACKEND = 'cloudsql'
# CLOUDSQL_USER = 'ag_app'
# CLOUDSQL_PASSWORD = 'ag8jHsnu0Sli'
# CLOUDSQL_DATABASE = 'ag_db'
# CLOUDSQL_CONNECTION_NAME = 'advisor-group:us-central1:advisor-group-database'

# The CloudSQL proxy is used locally to connect to the cloudsql instance.
# To start the proxy, use:
#
#   $ cloud_sql_proxy -instances=your-connection-name=tcp:3306
#
# Port 3306 is the standard MySQL port. If you need to use a different port,
# change the 3306 to a different port number.

# Alternatively, you could use a local MySQL instance for testing.
# LOCAL_SQLALCHEMY_DATABASE_URI = (
#     'mysql+pymysql://{user}:{password}@127.0.0.1:3306/{database}').format(
#         user=CLOUDSQL_USER, password=CLOUDSQL_PASSWORD,
#         database=CLOUDSQL_DATABASE)

# # When running on App Engine a unix socket is used to connect to the cloudsql
# # instance.
# LIVE_SQLALCHEMY_DATABASE_URI = (
#     'mysql+pymysql://{user}:{password}@localhost/{database}'
#     '?unix_socket=/cloudsql/{connection_name}').format(
#         user=CLOUDSQL_USER, password=CLOUDSQL_PASSWORD,
#         database=CLOUDSQL_DATABASE, connection_name=CLOUDSQL_CONNECTION_NAME)

# if os.environ.get('GAE_INSTANCE'):
#     print("Using cloud database!")
#     SQLALCHEMY_DATABASE_URI = LIVE_SQLALCHEMY_DATABASE_URI
# else:
#     SQLALCHEMY_DATABASE_URI = LOCAL_SQLALCHEMY_DATABASE_URI
#     print("Using local database!")
