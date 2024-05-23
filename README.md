# ML Housing Prediction

This project demonstrates how to deploy a machine learning model using Flask, Docker, and Heroku.

## Setup

1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. (Optional) This repo already has the dataset (`data/housing.csv`) but if you are looking for a script to download any dataset from Kaggle with some potential modifications, please use the below script. This requires Kaggle account and API setup on your command line [https://www.kaggle.com/docs/api] to run successfully
   ```bash
   python download_dataset.py
   ```
4. Train the model:
   ```bash
   python train_model.py
   ```
5. Run the Flask app:
   ```bash
   python app.py
   ```

## Test
1. Local Testing
   ```bash
   curl -X POST -H "Content-Type: application/json" -d '{"OverallQual": 7, "GrLivArea": 1710, "GarageCars": 2, "GarageArea": 548, "TotalBsmtSF": 856, "FullBath": 2, "1stFlrSF": 856, "TotRmsAbvGrd": 8, "YearBuilt": 2003, "YearRemodAdd": 2003}' http://localhost:6000/predict
   ```

## Docker Instructions

1. Build the Docker image:
   ```bash
   docker build -t ml-housing-prediction .
   ```
2. Run the Docker container:
   ```bash
   docker run -p 5000:80 ml-housing-prediction
   ```

## Heroku Deployment

1. Create a Heroku app:
   ```bash
   heroku create ml-housing-prediction
   ```
2. Push to Heroku:
   ```bash
   git push heroku master
   ```