from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    """Configuration class for data ingestion."""

    root_dir: Path        # Root directory where data will be stored
    source_URL: str       # URL from where the data will be downloaded
    local_data_file: Path  # Path to the local data file
    unzip_dir: Path       # Directory where the data will be extracted after downloading