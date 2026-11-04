import sqlite3
import pandas as pd

conn = sqlite3.connect('data/grocery.db')
tables = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table';", conn)

for table in tables['name']:
    cols = pd.read_sql_query(f"SELECT * FROM {table} LIMIT 0", conn).columns.tolist()
    print(f"\nTable: {table}")
    print(f"Columns: {cols}")