import os
import sys
import yaml
import json
from pathlib import Path
from box import ConfigBox
from ensure import ensure_annotations
from box.exceptions import BoxValueError
from Automaitc_number_plate_recognition import logger
from Automaitc_number_plate_recognition.exceptions import custom_exception


@ensure_annotations
def read_yaml(file_path: Path) -> ConfigBox:
    try:
        logger.info(f"Reading yaml file: {file_path}")
        with open(file_path, "r") as file:
            content = yaml.safe_load(file)
            print(content)
            logger.info(f"Yaml file read successfully: {file_path}")
        
            if content is None:
                logger.warning(f"YAML file {file_path} is empty.")
                return ConfigBox()
            
        return ConfigBox(content)
    
    except (FileNotFoundError, BoxValueError, yaml.YAMLError) as e:  
        logger.error(f"Error in reading yaml file: {file_path}")
        raise custom_exception(e)
    
    
    