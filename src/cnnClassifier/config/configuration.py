from cnnClassifier.constants import *
import os
from cnnClassifier.utils.common import read_yaml, create_directories,save_json
from cnnClassifier.entity.config_entity import (DataIngestionConfig,
                                                PrepareBaseModelConfig
                                                )

                                                

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
    

    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
        """
        Gets the configuration for preparing the base model.

        Returns:
            PrepareBaseModelConfig: Configuration for preparing the base model.
        """
        # Get configuration settings for preparing the base model
        config = self.config.prepare_base_model

        # Create directories specified in the configuration
        create_directories([config.root_dir])

        # Create PrepareBaseModelConfig object with obtained configuration settings
        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir=Path(config.root_dir),
            base_model_path=Path(config.base_model_path),
            updated_base_model_path=Path(config.updated_base_model_path),
            params_image_size=self.params.IMAGE_SIZE,
            params_learning_rate=self.params.LEARNING_RATE,
            params_include_top=self.params.INCLUDE_TOP,
            params_weights=self.params.WEIGHTS,
            params_classes=self.params.CLASSES
        )

        return prepare_base_model_config
