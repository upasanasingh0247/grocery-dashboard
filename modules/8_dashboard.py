import streamlit as st
import pandas as pd
import sqlite3 
# st.set_page_config(page_title="Grocery Dashboard", layout="wide")
st.set_page_config(page_title="Grocery Dashboard", layout="wide")
st.title("🛒 Grocery Sales Dashboard")
conn = sqlite3.connect('data/grocery.db')
query = """
SELECT product_id, COUNT(product_id) AS purchage_count
FROM dunnhumby_transactions
GROUP BY product_id
ORDER BY purchage_count DESC
LIMIT 10
"""
# Load the Data
st.write("### Top 10 Most Purchased Products")
top_products = pd.read_sql_query(query, conn)
top_products['product_id'] = top_products['product_id'].astype(str)
st.bar_chart(data=top_products, x='product_id', y='purchage_count')
conn.close()