import sys
from src.Automaitc_number_plate_recognition import logging



def error_message_details(error,error_details:sys):
    _,_,exc_tb = error_details.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = f"Error occured in python script name [{file_name}] line number [{exc_tb.tb_lineno}] error message[{str(error)}]"
    return error_message


class custom_exception(Exception):
    def __init__(self, error, error_details:sys):
        self.error = error
        self.error_details = error_details
        self.error_message = error_message_details(self.error, self.error_details)
        logging.error(self.error_message)
        super().__init__(self.error_message)
        self.error_details = error_details
        self.__str__ = lambda: self.error_message

    def __str__(self):
        return self.error_message