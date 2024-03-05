from cnnClassifier.constants import *
import os
from cnnClassifier.utils.common import read_yaml, create_directories,save_json
from cnnClassifier.entity.config_entity import (DataIngestionConfig)

                                                

# Class for managing configuration settings
class ConfigurationManager:
    def __init__(
        self,
        config_filepath=CONFIG_FILE_PATH,  # Path to the configuration file
        params_filepath=PARAMS_FILE_PATH   # Path to the parameters file
    ):
        # Initialize the configuration and parameters
        self.config = read_yaml(config_filepath)  # Read configuration from YAML file
        self.params = read_yaml(params_filepath)  # Read parameters from YAML file

        # Create necessary directories
        create_directories([self.config.artifacts_root])

    # Method to retrieve data ingestion configuration
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        # Get data ingestion configuration from the main configuration
        config = self.config.data_ingestion

        # Create directories specified in the configuration
        create_directories([config.root_dir])

        # Create DataIngestionConfig object using the retrieved configuration
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,              # Root directory for data ingestion
            source_URL=config.source_URL,          # URL for data source
            local_data_file=config.local_data_file,# Path to local data file
            unzip_dir=config.unzip_dir            # Directory for extracted data
        )

        return data_ingestion_config
