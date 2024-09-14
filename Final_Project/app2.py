from flask import Flask, render_template, request, jsonify
import requests
from PIL import Image
import io
import logging

# Initialize Flask app
app = Flask(__name__)

# Enable logging for debugging purposes
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def index():
    return render_template('frontend.html')

@app.route('/predict', methods=['POST'])
def predict():
    app.logger.info("Prediction request received")
    
    if 'file' not in request.files:
        app.logger.error("No file uploaded")
        return "No file uploaded", 400

    file = request.files['file']
    if file.filename == '':
        app.logger.error("No selected file")
        return "No selected file", 400

    try:
        # Send the image to the CNN service for feature extraction
        app.logger.info("Sending image to CNN service for feature extraction")
        cnn_response = requests.post('http://localhost:5001/extract_features', files={'file': file})
        if cnn_response.status_code != 200:
            app.logger.error(f"Error in CNN service: {cnn_response.text}")
            return f"Error in CNN service: {cnn_response.text}", 500

        cnn_data = cnn_response.json()
        features = cnn_data['features']
        app.logger.info(f"Features extracted: {features}")

        # Send the extracted features to the Random Forest service for classification
        app.logger.info("Sending features to Random Forest service for classification")
        rf_response = requests.post('http://localhost:5002/classify', json={'features': features})
        if rf_response.status_code != 200:
            app.logger.error(f"Error in RF service: {rf_response.text}")
            return f"Error in RF service: {rf_response.text}", 500

        rf_data = rf_response.json()
        app.logger.info(f"RF prediction: {rf_data}")
        
        return jsonify(rf_data)
    except Exception as e:
        app.logger.error(f"Error: {str(e)}")
        return f"Error: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)  # Main app runs on port 5000
