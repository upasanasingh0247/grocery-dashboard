import sqlite3
import pandas as pd
def analyze_popular_products():
    print("Connecting to the database...")
    conn = sqlite3.connect('data/grocery.db')

    sql_command = """ 
    SELECT product_id, COUNT(product_id) AS purchage_count FROM dunnhumby_transactions
    GROUP BY product_id
    ORDER BY purchage_count DESC 
    LIMIT 10;
    """

    print("Scanning 2.6 million rows to find the top 10 most popular products...")
    result = pd.read_sql_query(sql_command, conn)

    print("\nTop 10 Most Purchased Products:")
    print(result)

if __name__ == "__main__":
    analyze_popular_products()