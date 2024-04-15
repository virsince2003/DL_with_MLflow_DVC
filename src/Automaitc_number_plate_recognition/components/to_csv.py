# collecting data in csv file
import csv
from Automaitc_number_plate_recognition import logger
from Automaitc_number_plate_recognition.exceptions import custom_exception


def csv_data(output, output_path):
    try:
        logger.info("Collecting data in csv file")
        with open(output_path, "w") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([
                "frame_number",
                "number_plate_text",
                "text_confidence_score",
                "bbox",
                "confidence_score"])
            
            for frame_number,frame_data in output.items():
                if "number_plate" in frame_data:
                    number_plate_info = frame_data["number_plate"]
                    writer.writerow([frame_number,
                                    number_plate_info["text"],
                                    number_plate_info["text_confidence_score"],
                                    number_plate_info["bbox"],
                                    number_plate_info["confidence_score"]])
    except Exception as e:
        logger.error(f"Error in csv_data: {e}")
        raise custom_exception(e)