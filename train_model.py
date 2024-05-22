import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import pickle

# Load dataset
data = pd.read_csv('data/housing.csv')

# Feature selection
features = ['OverallQual', 'GrLivArea', 'GarageCars', 'GarageArea', 'TotalBsmtSF', 
            'FullBath', '1stFlrSF', 'TotRmsAbvGrd', 'YearBuilt', 'YearRemodAdd']
X = data[features]
y = data['SalePrice']  # Assuming 'SalePrice' is the target variable

# Handle missing values if any (simple example: fill with median values)
X = X.fillna(X.median())

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate the model
predictions = model.predict(X_test)
mse = mean_squared_error(y_test, predictions)
print(f'Mean Squared Error: {mse}')

# Save the model
with open('models/model.pkl', 'wb') as f:
    pickle.dump(model, f)