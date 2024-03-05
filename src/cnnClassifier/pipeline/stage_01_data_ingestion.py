from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.data_ingestion import DataIngestion
from cnnClassifier import logger

STAGE_NAME = "Data Ingestion stage"


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        """
        Main method to execute the data ingestion training pipeline.
        """
        try:
            # Initialize ConfigurationManager to get configuration settings
            config_manager = ConfigurationManager()

            # Get data ingestion configuration from the configuration manager
            data_ingestion_config = config_manager.get_data_ingestion_config()

            # Initialize DataIngestion with the obtained configuration
            data_ingestion = DataIngestion(config=data_ingestion_config)

            # Download data from the specified URL
            data_ingestion.download_file()

            # Extract the downloaded zip file
            data_ingestion.extract_zip_file()

        except Exception as e:
            # Log any exceptions that occur during the process
            logger.exception(e)
            raise e

if __name__ == '__main__':
    try:
        # Log the start of the stage
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")

        # Instantiate the DataIngestionTrainingPipeline and execute the main method
        obj = DataIngestionTrainingPipeline()
        obj.main()

        # Log the completion of the stage
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

    except Exception as e:
        # Log any exceptions that occur during the process and raise them
        logger.exception(e)
        raise e
