import cv2
import os
import base64
import torch
import numpy as np
from PIL import Image
from ultralytics import YOLO
from ultralytics.utils.ops import non_max_suppression
from Automaitc_number_plate_recognition.components.to_csv import csv_data
from Automaitc_number_plate_recognition.components.ocr import read_number_plate
from Automaitc_number_plate_recognition import logger
from Automaitc_number_plate_recognition.exceptions import custom_exception
from Automaitc_number_plate_recognition.components.image_processing import bbox_border
from src.Automaitc_number_plate_recognition.configuration.config import ManageConfig
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")


config = ManageConfig()
test_path = config.get_test_config().image_path
model_path = config.get_model_config().model_path
output_image_path = config.get_output_config().output_img_path
model = YOLO(model_path)

os.makedirs(os.path.dirname(output_image_path), exist_ok=True)


def get_output_path():
    root_dir = os.getcwd()
    output_dir = os.path.join(root_dir, 'csv_data')
    output_path = os.path.join(output_dir, 'anpr_data.csv')
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    return output_path

frame = cv2.imread(test_path)
output = {}
frame_number = 0

output[frame_number] = {}
number_plate_ = model.predict(frame)
for data_box in number_plate_[0].boxes.data:
    x1, y1, x2, y2, confidence_score, class_id = data_box
    frame = bbox_border(frame, (x1, y1), (x2, y2))
    cropped_number_plate = frame[int(y1):int(y2), int(x1):int(x2)]
    grey_cropped_number_plate = cv2.cvtColor(cropped_number_plate, cv2.COLOR_BGR2GRAY)
    _, threshold_cropped_number_plate = cv2.threshold(grey_cropped_number_plate, 64, 255, cv2.THRESH_BINARY_INV)

    number_plate_text, number_plate_text_score = read_number_plate(threshold_cropped_number_plate)
    print("number_plate : ", number_plate_text)

    if number_plate_text is not None:
        output[frame_number] = {
            "number_plate": {
                "text": number_plate_text,
                "confidence_score": number_plate_text_score,
                "bbox": [x1, y1, x2, y2],
                "text_confidence_score": number_plate_text_score
            }
        }

        cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
        # Display text
        cv2.putText(frame, number_plate_text, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 0.5)

cv2.imwrite(output_image_path, frame)
csv_data(output, get_output_path())
img = Image.open(output_image_path)
img.show()
