import streamlit as st
import pandas as pd

st.set_page_config(page_title="Grocery Dashboard", layout="wide")
st.title("🛒 Grocery Sales Dashboard")

# Read the stitched data from your exports folder
top_products = pd.read_csv('exports/top_100_products.csv')

st.write("### Top 10 Most Purchased Products")

# Filter to the top 10 so the bar chart is easy to read
chart_data = top_products.head(10)
st.bar_chart(data=chart_data, x='product_name', y='purchase_count')

# Display the full table of 100 items below the chart
st.write("### Full Top 100 List")
st.dataframe(top_products)