from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    """Configuration class for data ingestion."""

    root_dir: Path        # Root directory where data will be stored
    source_URL: str       # URL from where the data will be downloaded
    local_data_file: Path  # Path to the local data file
    unzip_dir: Path       # Directory where the data will be extracted after downloading



    # entity for prepare base model

@dataclass(frozen=True)
class PrepareBaseModelConfig:
    """
    Configuration class for preparing the base model.

    Attributes:
        root_dir (Path): Root directory for storing artifacts.
        base_model_path (Path): File path to the base model.
        updated_base_model_path (Path): File path to the updated base model.
        params_image_size (list): Size of the input images [height, width, channels].
        params_learning_rate (float): Learning rate used in the optimizer.
        params_include_top (bool): Whether to include the top (fully connected) layers of the model.
        params_weights (str): Pre-trained weights to initialize the model.
        params_classes (int): Number of classes in the classification problem.
    """
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    params_image_size: list
    params_learning_rate: float
    params_include_top: bool
    params_weights: str
    params_classes: int


@dataclass(frozen=True)
class TrainingConfig:
    """
    Configuration data class for training process.

    Attributes:
        root_dir (Path): Root directory for storing training artifacts.
        trained_model_path (Path): Path to save the trained model file.
        updated_base_model_path (Path): Path to the updated base model file.
        training_data (Path): Path to the directory or file containing training data.
        params_epochs (int): Number of epochs for training.
        params_batch_size (int): Batch size for training.
        params_is_augmentation (bool): Flag indicating whether data augmentation is enabled.
        params_image_size (list): Size of input images [width, height, channels].
    """
    root_dir: Path
    trained_model_path: Path
    updated_base_model_path: Path
    training_data: Path
    params_epochs: int
    params_batch_size: int
    params_is_augmentation: bool
    params_image_size: list

