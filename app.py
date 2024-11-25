# app.py

from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

# Load the trained Random Forest model
model_path = 'rf_model.pkl'  # Ensure this matches the filename of your saved model
with open(model_path, 'rb') as file:
    model = joblib.load(file)

app = Flask(__name__)

# Define the feature names expected by the model
feature_names = [
    'Issue_Size(crores)', 'QIB', 'HNI', 'RII', 'Issue_price', 
    'Listing_Open', 'Listing_Close', 'CMP', 'Market_Profit', 'SME'
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract data from form inputs
        input_features = [float(request.form[feature]) for feature in feature_names]
        final_features = [np.array(input_features)]
        
        # Make prediction
        prediction = model.predict(final_features)
        output = 'Underpriced' if prediction[0] == 1 else 'Overpriced'
        
        return render_template('index.html', prediction_text=f'Prediction: {output}')
    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {str(e)}')

if __name__ == "__main__":
    app.run(debug=True)
