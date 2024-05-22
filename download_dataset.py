import os
from kaggle.api.kaggle_api_extended import KaggleApi

# Initialize the Kaggle API
api = KaggleApi()
api.authenticate()

# Define the dataset and file names
dataset = 'house-prices-advanced-regression-techniques'
filename = 'train.csv'

# Download the dataset
api.competition_download_file(dataset, filename, path='data')

# Unzip the file if necessary
#import zipfile
#with zipfile.ZipFile(f'downloaded/{filename}.zip', 'r') as zip_ref:
#    zip_ref.extractall('data')

# Rename the file to housing.csv
os.rename('data/train.csv', 'data/housing.csv')