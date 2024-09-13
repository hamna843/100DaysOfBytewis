from flask import Flask, request, render_template, jsonify
from tensorflow.keras.models import load_model
import numpy as np
import pickle
from PIL import Image
import io

app = Flask(__name__)

# Load models and label encoder
cnn_model = load_model('models/cnn_model.h5')
cnn = load_model('CNN_MODEL.h5')  # Updated to CNN_MODEL.h5
with open('models/rf_model.pkl', 'rb') as f:
    rf_model = pickle.load(f)
with open('models/label_encoder.pkl', 'rb') as f:
    label_encoder = pickle.load(f)

# Feature extraction using CNN
def extract_features(image):
    image = image.resize((150, 150))  # Ensure image is resized to 150x150
    image_array = np.array(image) / 255.0
    image_array = np.expand_dims(image_array, axis=0)
    features = cnn_model.predict(image_array)
    return features

@app.route('/')
def index():
    return render_template('index2.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files or 'model' not in request.form:
        return "File or model selection is missing", 400

    file = request.files['file']
    model_choice = request.form['model']

    if file.filename == '':
        return "No selected file", 400

    try:
        image = Image.open(io.BytesIO(file.read()))

        # If CNN model is selected
        if model_choice == 'cnn':
            processed_image = image.resize((150, 150))  # Resize image for CNN
            processed_image = np.array(processed_image) / 255.0
            processed_image = np.expand_dims(processed_image, axis=0)

            # Make prediction using CNN model
            prediction = cnn.predict(processed_image)
            predicted_class = label_encoder.inverse_transform([np.argmax(prediction)])[0]
            confidence_percentages = (prediction[0] * 100).round(2)
            all_confidences = {
                label_encoder.inverse_transform([i])[0]: f"{confidence_percentages[i]}%"
                for i in range(len(confidence_percentages))
            }

            return jsonify({
                'model': 'CNN',
                'predicted_class': predicted_class,
                'confidences': all_confidences
            })
        # If Random Forest model is selected
        elif model_choice == 'rf':
            features = extract_features(image)
            prediction = rf_model.predict(features)
            predicted_class = label_encoder.inverse_transform(prediction)[0]
            # Random Forest model doesn't give probabilities by default, but we can get them
            probabilities = rf_model.predict_proba(features)[0]
            confidence_percentages = (probabilities * 100).round(2)  # Convert to percentages

            # Prepare a dictionary of class labels and confidence percentages
            all_confidences = {
                label_encoder.inverse_transform([i])[0]: f"{confidence_percentages[i]}%"
                for i in range(len(confidence_percentages))
            }

            return jsonify({
                'model': 'Random Forest',
                'predicted_class': predicted_class,
                'confidences': all_confidences
            })
        #return f"Predicted class using {model_choice.upper()}: {predicted_class}"

    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)
