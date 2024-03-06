from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.model_training import Training
from cnnClassifier import logger

# Define the name of the stage
STAGE_NAME = "Training"

# Class to handle the model training pipeline
class ModelTrainingPipeline:
    def __init__(self):
        """
        Initializes the ModelTrainingPipeline object.
        """
        pass

    def main(self):
        """
        Main method to execute the model training pipeline.

        This method orchestrates the entire model training pipeline, including
        configuration retrieval, model training, and logging of pipeline stages.
        """
        # Retrieve configuration settings
        config = ConfigurationManager()
        training_config = config.get_training_config()
        
        # Initialize and execute model training
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()

if __name__ == '__main__':
    try:
        # Log the start of the training stage
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        
        # Initialize and execute the model training pipeline
        obj = ModelTrainingPipeline()
        obj.main()
        
        # Log the completion of the training stage
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        # Log any exceptions that occur during the training stage
        logger.exception(e)
        raise e
