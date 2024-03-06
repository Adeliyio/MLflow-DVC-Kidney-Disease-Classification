from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.data_ingestion import DataIngestion
from cnnClassifier import logger

STAGE_NAME = "Data Ingestion stage"


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        """
        Main method to orchestrate the data ingestion pipeline.
        """
        # Initialize ConfigurationManager to retrieve configuration settings
        config = ConfigurationManager()

        # Get data ingestion configuration
        data_ingestion_config = config.get_data_ingestion_config()

        # Initialize DataIngestion with the obtained configuration
        data_ingestion = DataIngestion(config=data_ingestion_config)

        # Download data from the specified URL
        data_ingestion.download_file()

        # Extract the downloaded zip file
        data_ingestion.extract_zip_file()


if __name__ == '__main__':
    try:
        # Log start of the data ingestion stage
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")

        # Instantiate the DataIngestionTrainingPipeline object
        pipeline = DataIngestionTrainingPipeline()

        # Execute the main method to run the data ingestion pipeline
        pipeline.main()

        # Log completion of the data ingestion stage
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        # Log any exceptions that occur during the pipeline execution
        logger.exception(e)
        raise e  # Re-raise the exception for further handling
