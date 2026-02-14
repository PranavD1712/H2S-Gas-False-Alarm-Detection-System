from flask import Flask, request, jsonify
import numpy as np
import pickle

app = Flask (__name__)

with open('lr.pkl', 'rb') as f:
    model=pickle.load(f)

with open('scaler.pkl', 'rb') as f:
    scaler=pickle.load(f)

print('\n Model & Scaler Loaded Successfully!')

# API Health Check
@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "Message": "H2S False Alarm Detection API",
        "Status": "Running",
         })

# API Prediction
@app.route('/test_model', methods=['POST'])
def predict():
    data = request.get_json()

    features = [
        data['Ambient Temperature'],
        data['Calibration'],
        data['Unwanted Substance_Deposition'],
        data['Humidity(%)'],
        data['H2S Content(ppm)'],
        data['detected by_sensors']
    ]

    features_array = np.array(features).reshape(1, -1)
    # Scale features
    features_scaled = scaler.transform(features_array)

    # Making Prediction
    prediction = model.predict(features_scaled)[0]


    response = {
        "Prediction": int(prediction),
        "dangerous": bool(prediction == 1),
        "recommendation": "DISPATCH TEAM" if prediction == 1 else "FALSE ALARM - No action needed",
        "input_features": {
            "Ambient Temperature": data['Ambient Temperature'],
            "Calibration": data['Calibration'],
            "Unwanted Substance_Deposition": data['Unwanted Substance_Deposition'],
            "Humidity(%)": data['Humidity(%)'],
            "H2S Content(ppm)": data['H2S Content(ppm)'],
            "detected by_sensors": data['detected by_sensors']
        }

    }
    return jsonify(response)



# Run Flask
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

