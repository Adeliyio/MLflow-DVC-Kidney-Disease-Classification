# Import the logger from the cnnClassifier module
from cnnClassifier import logger
# Import the DataIngestionTrainingPipeline class from the stage_01_data_ingestion module in the cnnClassifier.pipeline package
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline


# Define the name of the stage
STAGE_NAME = "Data Ingestion stage"

try:
    # Log that the stage has started
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")

    # Initialize the DataIngestionTrainingPipeline
    data_ingestion = DataIngestionTrainingPipeline()

    # Execute the main method of the pipeline
    data_ingestion.main()

    # Log that the stage has completed
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
    # If an exception occurs, log the error and raise it
    logger.exception(e)
    raise e



# Define the name of the stage
STAGE_NAME = "Prepare base model"

try:
    # Log a separator for better readability
    logger.info(f"*******************")

    # Log that the stage has started
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")

    # Initialize the PrepareBaseModelTrainingPipeline
    prepare_base_model = PrepareBaseModelTrainingPipeline()

    # Execute the main method of the pipeline
    prepare_base_model.main()

    # Log that the stage has completed
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
    # If an exception occurs, log the error and raise it
    logger.exception(e)
    raise e
