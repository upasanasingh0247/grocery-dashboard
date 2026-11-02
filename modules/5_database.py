import pandas as pd
import sqlite3

def load_dunnhumby_to_db():
    print("Connecting to SQLite database...")
    conn = sqlite3.connect('data/grocery.db')
    
    clean_path = 'data/clean/transaction_clean.csv'
    print(f"Reading data from {clean_path} in chunks...")
    
    # 1. Set our safe chunk limit again
    chunk_size = 50000
    chunk_iterator = pd.read_csv(clean_path, chunksize=chunk_size)
    
    batch_number = 1
    for chunk in chunk_iterator:
        print(f"Injecting batch {batch_number} into database...")
        
        # 2. For the first batch, create a fresh table. For the rest, append to it.
        if batch_number == 1:
            chunk.to_sql('dunnhumby_transactions', conn, if_exists='replace', index=False)
        else:
            chunk.to_sql('dunnhumby_transactions', conn, if_exists='append', index=False)
            
        batch_number += 1
        
    conn.close()
    print("Success! All 2.6 million transactions safely loaded into grocery.db!")

if __name__ == '__main__':
    load_dunnhumby_to_db()