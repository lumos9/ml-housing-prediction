from flask import Flask, request, jsonify
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load the trained model
with open('models/model.pkl', 'rb') as f:
    model = pickle.load(f)

# Define the expected feature names
feature_names = [
    'OverallQual', 'GrLivArea', 'GarageCars', 'GarageArea', 'TotalBsmtSF', 
    'FullBath', '1stFlrSF', 'TotRmsAbvGrd', 'YearBuilt', 'YearRemodAdd'
]

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    
    # Create a DataFrame using the input data
    input_data = pd.DataFrame([data], columns=feature_names)
    
    # Predict using the model
    prediction = model.predict(input_data)
    
    # Return the prediction as a JSON response
    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=6000)