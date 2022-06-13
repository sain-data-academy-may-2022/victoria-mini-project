'''Modules which handles connections and queries with a locally held database'''

from fileinput import close
import pymysql
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
host = os.environ.get('mysql_host')
user = os.environ.get('mysql_user')
password = os.environ.get('mysql_pass')
database = os.environ.get('mysql_db')

# Establish a database connection
def get_connection():
    connection = pymysql.connect(
        host,
        user,
        password,
        database
    )

    return connection

# Close a database connection
def close_connection(connection: pymysql.Connection):
    connection.close()

# Execute a sql query and return data from it
def db_query(sql_query: str, connection: pymysql.Connection):

    cursor = connection.cursor(pymysql.cursors.DictCursor)

    cursor.execute(sql_query)
    
    db_data = cursor.fetchall()

    connection.commit()
    cursor.close()

    return db_data

# Execute a sql query without returning anything
def db_command(sql_query: str, connection: pymysql.Connection):

    cursor = connection.cursor()

    cursor.execute(sql_query)

    connection.commit()
    cursor.close()
