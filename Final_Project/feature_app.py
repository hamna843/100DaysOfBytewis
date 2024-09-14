from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import io

app = Flask(__name__)

# Load the CNN model
cnn_model = load_model('models/cnn_model.h5')

# Feature extraction function
def extract_features(image):
    image = image.resize((150, 150))  # Resize to match model input
    image_array = np.array(image) / 255.0  # Normalize
    image_array = np.expand_dims(image_array, axis=0)  # Add batch dimension
    features = cnn_model.predict(image_array)  # Extract features
    return features

# Home route for testing the service
@app.route('/')
def home():
    return "CNN Service is running"

# Feature extraction route
@app.route('/extract_features', methods=['POST'])
def extract_features_endpoint():
    if 'file' not in request.files:
        return "No file uploaded", 400

    file = request.files['file']
    image = Image.open(io.BytesIO(file.read()))
    features = extract_features(image)
    features_list = features.tolist()  # Convert to list to make JSON serializable
    return jsonify({'features': features_list})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
