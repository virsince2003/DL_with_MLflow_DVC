import os
import sys
import logging
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d')}.log"
log_path = os.path.join(os.getcwd(), 
                        "logs")

os.makedirs(log_path,exist_ok=True)

log_file_path = os.path.join(log_path, LOG_FILE)

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(filename)s:%(lineno)d - %(name)s - %(levelname)s - %(message)s]",
    handlers=[
        logging.FileHandler(log_file_path),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("Automatic_number_plate_recognition")




