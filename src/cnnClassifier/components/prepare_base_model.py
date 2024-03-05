import os
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf
from pathlib import Path
from cnnClassifier.entity.config_entity import PrepareBaseModelConfig

class PrepareBaseModel:
    def __init__(self, config: PrepareBaseModelConfig):
        """
        Initializes PrepareBaseModel with the given configuration.

        Args:
            config (PrepareBaseModelConfig): Configuration for preparing the base model.
        """
        self.config = config

    def get_base_model(self):
        """
        Loads the base model and saves it.

        This method loads the base model, sets its configuration,
        and saves the model to the specified path.
        """
        # Load base model
        self.model = tf.keras.applications.vgg16.VGG16(
            input_shape=self.config.params_image_size,
            weights=self.config.params_weights,
            include_top=self.config.params_include_top
        )

        # Save the base model
        self.save_model(path=self.config.base_model_path, model=self.model)

    @staticmethod
    def _prepare_full_model(model, classes, freeze_all, freeze_till, learning_rate):
        """
        Prepares the full model by adding additional layers.

        Args:
            model (tf.keras.Model): Base model.
            classes (int): Number of classes.
            freeze_all (bool): Whether to freeze all layers.
            freeze_till (int): Number of layers to freeze.
            learning_rate (float): Learning rate for optimizer.

        Returns:
            tf.keras.Model: Prepared full model.
        """
        # Freeze layers as per configuration
        if freeze_all:
            for layer in model.layers:
                model.trainable = False
        elif (freeze_till is not None) and (freeze_till > 0):
            for layer in model.layers[:-freeze_till]:
                model.trainable = False

        # Add additional layers
        flatten_in = tf.keras.layers.Flatten()(model.output)
        prediction = tf.keras.layers.Dense(
            units=classes,
            activation="softmax"
        )(flatten_in)

        # Compile the full model
        full_model = tf.keras.models.Model(
            inputs=model.input,
            outputs=prediction
        )

        full_model.compile(
            optimizer=tf.keras.optimizers.SGD(learning_rate=learning_rate),
            loss=tf.keras.losses.CategoricalCrossentropy(),
            metrics=["accuracy"]
        )

        # Print model summary
        full_model.summary()
        return full_model

    def update_base_model(self):
        """
        Updates the base model with additional layers and saves it.

        This method prepares the full model, updates the base model
        with additional layers, and saves the updated model to the specified path.
        """
        # Prepare the full model
        self.full_model = self._prepare_full_model(
            model=self.model,
            classes=self.config.params_classes,
            freeze_all=True,
            freeze_till=None,
            learning_rate=self.config.params_learning_rate
        )

        # Save the updated base model
        self.save_model(path=self.config.updated_base_model_path, model=self.full_model)

    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        """
        Saves the model to the specified path.

        Args:
            path (Path): Path to save the model.
            model (tf.keras.Model): Model to be saved.
        """
        model.save(path)
