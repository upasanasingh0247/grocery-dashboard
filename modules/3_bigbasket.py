import pandas as pd

def clean_bigbasket():
    print("Loading BigBasket data...")
    
    # 1. Load the raw CSV file into a pandas "DataFrame" (think of it like an Excel sheet)
    file_path = 'data/raw/bigbasket/BigBasket Products.csv'
    df = pd.read_csv(file_path)
    
    print(f"\nOriginal rows {len(df)}")

    # 1. Drop the 'index' column because pandas already creates its own index
    if "index" in df.columns:
        df = df.drop(columns=['index'])

    # 2. Drop any row that is missing a sale price (we can't analyze a product without a price)
    df = df.dropna(subset=['sale_price'])

   # 3. Clean up the text in the 'category' column (make it all uppercase so it's consistent)
    df['category'] = df['category'].str.upper()
    print(f"Clean Rows: {len(df)}")

    # 4. Save the clean data into our 'clean' folder
    clean_path = 'data/clean/bigbasket_clean.csv'
    df.to_csv(clean_path, index=False)
    print(f"Clean data saved to: {clean_path}")

if __name__ == "__main__":
    clean_bigbasket()

