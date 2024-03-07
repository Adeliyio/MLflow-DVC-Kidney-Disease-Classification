from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from cnnClassifier.utils.common import decodeImage
from cnnClassifier.pipeline.prediction import PredictionPipeline

# Set encoding environment variables for compatibility
os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Client application class
class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)

# Route for home page
@app.route("/", methods=['GET'])
@cross_origin()
def home():
    """
    Renders the home page.

    Returns:
    - str: Rendered HTML of the home page.
    """
    return render_template('index.html')

# Route for training
@app.route("/train", methods=['GET','POST'])
@cross_origin()
def trainRoute():
    """
    Triggers the training process.

    Returns:
    - str: Success message upon completion of training.
    """
    os.system("python main.py")
    os.system("dvc repro")  # Uncomment this line if using DVC for reproducibility
    return "Training done successfully!"

# Route for prediction
@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    """
    Handles prediction requests.

    Returns:
    - json: JSON response containing the prediction result.
    """
    image = request.json['image']
    decodeImage(image, clApp.filename)
    result = clApp.classifier.predict()
    return jsonify(result)

# Main execution point
if __name__ == "__main__":
    clApp = ClientApp()
    # Run the Flask app
    app.run(host='0.0.0.0', port=8080)  # for AWS
