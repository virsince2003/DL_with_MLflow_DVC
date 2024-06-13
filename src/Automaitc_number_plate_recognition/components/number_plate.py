import string
from Automaitc_number_plate_recognition import logger
from Automaitc_number_plate_recognition.exceptions import custom_exception

dict_char_to_int = {'O': '0', 'I': '1', 'J': '3', 'A': '4', 'G': '6', 'S': '5', 'Z': '2', 'E': '8', 'T': '7'}
dict_int_to_char = {v: k for k, v in dict_char_to_int.items()}

def is_valid_char(char, position, length):
    """
    Checks if character is valid based on its position and number length
    """
    if length == 10:
        if position in [0, 1, 4, 5]:
            return char in string.ascii_uppercase or char in dict_int_to_char
        else:
            return char in string.digits or char in dict_char_to_int
    else:
        if position in [0, 1, 4]:
            return char in string.ascii_uppercase or char in dict_int_to_char
        else:
            return char in string.digits or char in dict_char_to_int
    return False

def number_plate_format(text):
    """
    Checks if the number format is correct
    """
    try:
        logger.info(f"Checking the format of the number plate: {text}")
        length = len(text)
        if length not in [9, 10]:
            return False
        
        for i, char in enumerate(text):
            if not is_valid_char(char, i, length):
                return False
        
        return True
        
    except Exception as e:
        logger.error(f"Error in number_plate_format: {e}")
        raise custom_exception(e)
    

    
def format_of_plate(text):
    try:
        number_plate = ""
        mapping_for_10 = {
                    0:dict_int_to_char,
                    1:dict_int_to_char,
                    2:dict_char_to_int,
                    3:dict_char_to_int,
                    4:dict_int_to_char,
                    5:dict_int_to_char,
                    6:dict_char_to_int,
                    7:dict_char_to_int,
                    8:dict_char_to_int,
                    9:dict_char_to_int
                    }
        
        mapping_for_9 = {
                0:dict_int_to_char,
                1:dict_int_to_char,
                2:dict_char_to_int,
                3:dict_char_to_int,
                4:dict_int_to_char,
                5:dict_char_to_int,
                6:dict_char_to_int,
                7:dict_char_to_int,
                8:dict_char_to_int
                }
        
        mapping = mapping_for_10 if len(text)==10 else mapping_for_9
       
        for i, char in enumerate(text):
            number_plate += mapping[i].get(key=char, default_value=char)

        return number_plate
        
    except Exception as e:
        logger.error(f"Error in format_of_plate: {e}")
        raise custom_exception(e)