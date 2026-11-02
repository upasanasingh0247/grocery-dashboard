import sqlite3
import pandas as pd
def export_for_excel():
    print(" connecting to the database...")
    conn = sqlite3.connect('data/grocery.db')

    # We pull the Top 100 here so you have enough data for a good Excel chart
    query = """
    SELECT product_id, COUNT(product_id) as purchage_count
    FROM dunnhumby_transactions
    GROUP BY product_id
    ORDER BY purchage_count DESC
    """
    print("Scanning data and extracting Top 100 products...")
    summary_data =  pd.read_sql_query(query, conn)

    export_path = 'exports/top_100_products.csv'
    summary_data.to_csv(export_path, index=False)
import sqlite3
import pandas as pd

def export_for_excel():
    print("Connecting to the database...")
    conn = sqlite3.connect('data/grocery.db')
    
    # We pull the Top 100 here so you have enough data for a good Excel chart
    query = """
    SELECT product_id, COUNT(product_id) AS purchase_count
    FROM dunnhumby_transactions
    GROUP BY product_id
    ORDER BY purchase_count DESC
    LIMIT 100;
    """
    
    print("Scanning data and extracting Top 100 products...")
    summary_data = pd.read_sql_query(query, conn)
    
    export_path = 'exports/top_100_products.csv'
    summary_data.to_csv(export_path, index=False)
    
    print(f"Success! Your data is saved to {export_path}")
    conn.close()

if __name__ == '__main__':
    export_for_excel()
 