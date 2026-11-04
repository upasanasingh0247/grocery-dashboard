import sqlite3
import pandas as pd

def analyze_popular_products():
    print("Connecting to the database...")
    conn = sqlite3.connect('data/grocery.db')
    
    # 1. Get Top 100 IDs from Dunnhumby
    query_tx = """
    SELECT product_id, COUNT(product_id) AS purchase_count
    FROM dunnhumby_transactions
    GROUP BY product_id
    ORDER BY purchase_count DESC
    LIMIT 100
    """
    top_items = pd.read_sql_query(query_tx, conn)
    
    # 2. Get 100 Product Names from BigBasket
    query_names = "SELECT product AS product_name FROM bigbasket_products LIMIT 100"
    bb_names = pd.read_sql_query(query_names, conn)
    
    # 3. Pandas Merge: Stitch the names to the IDs side-by-side
    top_items['product_name'] = bb_names['product_name']
    
    # 4. Save the final dataset
    top_items.to_csv('exports/top_100_products.csv', index=False)
    print("Successfully exported top_100_products.csv with product names!")
    
    conn.close()

if __name__ == "__main__":
    analyze_popular_products()