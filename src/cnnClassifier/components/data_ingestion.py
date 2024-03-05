import os
import zipfile
import gdown
from cnnClassifier import logger
from cnnClassifier.utils.common import get_size
from cnnClassifier.entity.config_entity import (DataIngestionConfig)



class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        """
        Initializes DataIngestion instance with provided configuration.

        Args:
            config (DataIngestionConfig): Configuration for data ingestion.
        """
        self.config = config

    def download_file(self) -> str:
        """
        Downloads data from the specified URL.

        Returns:
            str: Path to the downloaded file.
        """
        try:
            dataset_url = self.config.source_URL
            zip_download_dir = self.config.local_data_file

            # Create directory for downloaded data if it doesn't exist
            os.makedirs("artifacts/data_ingestion", exist_ok=True)

            logger.info(f"Downloading data from {dataset_url} into file {zip_download_dir}")

            # Extract file ID from the dataset URL
            file_id = dataset_url.split("/")[-2]
            prefix = 'https://drive.google.com/uc?/export=download&id='

            # Download the file using gdown library
            gdown.download(prefix + file_id, zip_download_dir)

            logger.info(f"Downloaded data from {dataset_url} into file {zip_download_dir}")

            return zip_download_dir

        except Exception as e:
            raise e

    def extract_zip_file(self):
        """
        Extracts the contents of the zip file into the specified directory.
        """
        unzip_path = self.config.unzip_dir

        # Create directory for extracted data if it doesn't exist
        os.makedirs(unzip_path, exist_ok=True)

        # Extract the zip file
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)


