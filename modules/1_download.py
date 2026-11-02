import os
# This line tells Python: "Look for the kaggle.json file in this exact folder!"
os.environ['KAGGLE_CONFIG_DIR'] = os.getcwd()

from kaggle.api.kaggle_api_extended import KaggleApi

def fetch_datasets():
    api = KaggleApi()
    api.authenticate()

    print("Downloading BigBasket dataset...")
    api.dataset_download_files(
        'surajjha101/bigbasket-entire-product-list-28k-datapoints',
        path='data/raw/bigbasket',
        unzip=True
    )
    
    print("Downloading Dunnhumby dataset...")
    api.dataset_download_files(
        'frtgnn/dunnhumby-the-complete-journey',
        path='data/raw/dunnhumby',
        unzip=True
    )
    
    print("All datasets downloaded and unzipped successfully!")

if __name__ == "__main__":
    fetch_datasets()