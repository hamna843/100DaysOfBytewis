from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load Random Forest model and label encoder
with open('models/rf_model.pkl', 'rb') as f:
    rf_model = pickle.load(f)
with open('models/label_encoder.pkl', 'rb') as f:
    label_encoder = pickle.load(f)

@app.route('/classify', methods=['POST'])
def classify():
    try:
        data = request.json
        features = np.array(data['features'])

        # Predict using Random Forest model
        prediction = rf_model.predict(features)
        predicted_class = label_encoder.inverse_transform(prediction)[0]

        # Predict class probabilities
        probabilities = rf_model.predict_proba(features)[0]
        confidence_percentages = (probabilities * 100).round(2)

        # Prepare a dictionary of class labels and confidence percentages
        all_confidences = {
            label_encoder.inverse_transform([i])[0]: f"{confidence_percentages[i]}%"
            for i in range(len(confidence_percentages))
        }

        return jsonify({
            'predicted_class': predicted_class,
            'confidences': all_confidences
        })
    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True, port=5002)  # Runs on port 5002
