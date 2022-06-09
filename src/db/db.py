import pymysql
import os
from dotenv import load_dotenv


# Create connection
# Create cursor
# Create Query string
# Execute the query
# Commit to the query
# Close the cursor
# Close the connection



# Load environment variables from .env file
load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")

# Establish a database connection
def get_connection():
    connection = pymysql.connect(
        host,
        user,
        password,
        database
    )

    return connection


def close_connection(connection):
    connection.close()
    

def db_query(sql_query: str):

    connection = get_connection()

    cursor = connection.cursor(pymysql.cursors.DictCursor)

    cursor.execute(sql_query)

    db_data = cursor.fetchall()

    connection.commit()
    cursor.close()
    close_connection(connection)

    return db_data


def db_command(sql_query: str):

    connection = get_connection()

    cursor = connection.cursor()
    
    cursor.execute(sql_query)

    connection.commit()
    cursor.close()
    close_connection(connection)



# connection = get_connection()

# # A cursor is an object that represents a DB cursor, which is used to manage the context of a fetch operation.
# cursor = connection.cursor()

# # Add code here to insert a new record
# cursor.execute('SELECT * FROM products')

# rows = cursor.fetchall()
# for row in rows:
#     print(f'£{float(row[3]):.2f}')

# connection.commit()
# cursor.close()
# connection.close()




# data_list = []

# cnx = get_connection()
# cursor = cnx.cursor(pymysql.cursors.DictCursor)
# cursor.execute('Select * from products')


# print(cursor)


# for row in cursor:
#     data_dict = {}
#     for key, value in row.items():
#         if key == 'price':
#             value = float(value)
#         data_dict[key] = value

#     data_list.append(data_dict)

# return data_list


# print(data_list)