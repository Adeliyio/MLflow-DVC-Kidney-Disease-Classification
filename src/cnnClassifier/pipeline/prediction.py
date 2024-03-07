import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

class PredictionPipeline:
    def __init__(self, filename):
        """
        Initialize the PredictionPipeline with the filename of the image to predict.

        Parameters:
        - filename (str): The path to the image file for prediction.
        """
        self.filename = filename

    
    def predict(self):
        """
        Perform prediction on the given image file.

        Returns:
        - list: A list containing a dictionary with the prediction result.
        """
        # Load the trained model
        model = load_model(os.path.join("model", "model.h5"))

        # Load and preprocess the image
        imagename = self.filename
        test_image = image.load_img(imagename, target_size=(224, 224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)

        # Perform prediction
        result = np.argmax(model.predict(test_image), axis=1)
        print(result)

        # Interpret the prediction result
        if result[0] == 1:
            prediction = 'Tumor'
            return [{"image": prediction}]
        else:
            prediction = 'Normal'
            return [{"image": prediction}]
