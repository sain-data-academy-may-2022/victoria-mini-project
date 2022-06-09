from db.db import db_query
from modules.funcs_print import print_non_indexed, print_indexed


data = db_query('SELECT * FROM products ORDER BY category')
# data = db_query('SELECT * FROM couriers')

print_non_indexed(data)
print_indexed(data)