from pathlib import Path
from dataclasses import dataclass


@dataclass(frozen=True)
class TestConfig:
    image_path: Path
    
    
    

@dataclass(frozen=True)
class ModelConfig:
    model_path: Path
    
    
@dataclass(frozen=True)
class OutputConfig:
    output_img_path: Path
