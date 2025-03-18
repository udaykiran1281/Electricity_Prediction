from flask import Flask, request, jsonify
import numpy as np
import joblib

app = Flask(__name__)

# Load the trained model and scaler
model = joblib.load("power_plant_model.pkl")  # Ensure this file exists
scaler = joblib.load("scaler.pkl")  # Ensure this file exists

@app.route('/')
def home():
    return "Power Plant Prediction API is running! 🚀"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from the request
        data = request.json  
        
        # Ensure 'features' key is in the JSON
        if "features" not in data:
            return jsonify({"error": "Missing 'features' in request"}), 400

        # Convert input to NumPy array
        values = np.array(data["features"]).reshape(1, -1)  
        
        # Scale the input
        scaled_values = scaler.transform(values)  

        # Make prediction
        prediction = model.predict(scaled_values)[0]  

        return jsonify({"predicted_power_output": prediction})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Run on port 5001
