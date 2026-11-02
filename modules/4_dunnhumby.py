import pandas as pd

def clean_large_transactions():
    input_path = 'data/raw/dunnhumby/transaction_data.csv'
    output_path = 'data/clean/transaction_clean.csv'

    print("Starting the memory-safe chunking process...")

    chunk_size = 50000

    chunk_iterator = pd.read_csv(input_path, chunksize=chunk_size)

    batch_number = 1

    for chunk in chunk_iterator:
        print(f"cleaning and saving batch number {batch_number}")

        chunk.columns = chunk.columns.str.lower()

        if batch_number == 1:
            # chunk.to_csv.read_csv(output_path, mode='w', index=False)
            chunk.to_csv(output_path, mode='w', index=False)
        else:
            chunk.to_csv(output_path, mode='a', header=False, index=False)

        batch_number += 1
    print(f"Success! Large dataset processed safely and saved to {output_path}")

if __name__ == '__main__':
    clean_large_transactions()