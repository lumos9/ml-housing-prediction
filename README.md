# ML Model Deployment

This project demonstrates how to deploy a machine learning model using Flask, Docker, and Heroku.

## Setup

1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Train the model:
   ```bash
   python train_model.py
   ```
4. Run the Flask app:
   ```bash
   python app.py
   ```

## Test
1. Local Testing
   ```bash
   curl -X POST -H "Content-Type: application/json" -d '{"OverallQual": 7, "GrLivArea": 1710, "GarageCars": 2, "GarageArea": 548, "TotalBsmtSF": 856, "FullBath": 2, "1stFlrSF": 856, "TotRmsAbvGrd": 8, "YearBuilt": 2003, "YearRemodAdd": 2003}' http://127.0.0.1:5000/predict
   ```

## Docker Instructions

1. Build the Docker image:
   ```bash
   docker build -t ml_model_api .
   ```
2. Run the Docker container:
   ```bash
   docker run -p 5000:80 ml_model_api
   ```

## Heroku Deployment

1. Create a Heroku app:
   ```bash
   heroku create ml-model-api
   ```
2. Push to Heroku:
   ```bash
   git push heroku master
   ```