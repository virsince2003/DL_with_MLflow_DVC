import os
from Automaitc_number_plate_recognition import logger
from Automaitc_number_plate_recognition.constants import CONFIG_FILE_PATH
from Automaitc_number_plate_recognition.utils.common import read_yaml
from Automaitc_number_plate_recognition.entity.entity_config import TestConfig, ModelConfig, OutputConfig


class ManageConfig:
    def __init__(self, config_file_path = CONFIG_FILE_PATH):
        try:
            self.config = read_yaml(config_file_path)
            logger.info("Configuration loaded successfully.")
        except Exception as e:
            logger.error(f"Error loading configuration: {e}")
            raise
        
    def get_test_config(self) -> TestConfig:
        try:
            config = self.config.test_dir    
            test_config = TestConfig(
                image_path = config.get("image_path", None),
            )
            if test_config.image_path is None:
                logger.error("Image path not found in the configuration file.")
                raise ValueError("Image path not found in the configuration file.")
            
            logger.info("Test image configgiration loaded.")
            return test_config

        except Exception as e:
            raise ValueError(f"Error in loading test configuration file. {e} ")
        
    def get_output_config(self) -> OutputConfig:
        try:
            config = self.config.img_output_dir  
            output_config = OutputConfig(
                output_img_path = config.get("output_img_path", None),
            )
            if output_config.output_img_path is None:
                logger.error("Image path not found in the configuration file.")
                raise ValueError("Output image path not found in the configuration file.")
            
            logger.info("Output image configgiration loaded.")
            return output_config

        except Exception as e:
            raise ValueError(f"Error in loading test configuration file. {e} ")
    
    def get_model_config(self) -> ModelConfig:
        try:
            config = self.config.models_dir
            model_config = ModelConfig(
                model_path = config.get("model_path", None)
            )
            if model_config.model_path is None:
                logger.error("Model path not found in the configuration file.")
                raise ValueError("Model path not found in the configuration file.")
            
            logger.info("Model path loaded.")
            return model_config
        
        except Exception as e:
            raise ValueError(f"Error in loading model configuration file. {e} ")


