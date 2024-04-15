import string
from Automaitc_number_plate_recognition import logger
from Automaitc_number_plate_recognition.exceptions import custom_exception
dict_char_to_int = {'O': '0', 'I': '1', 'J': '3', 'A': '4', 'G': '6', 'S': '5', 'Z': '2', 'E': '8', 'T': '7'}
dict_int_to_char = {'0': 'O', '1': 'I', '3': 'J', '4': 'A', '6': 'G', '5': 'S', '2': 'Z', '7': "T", '8': 'E'}

def number_plate_format(text):
    try:
        logger.info(f"Checking the format of the number plate: {text}")
        if len(text) not in [9, 10]:
            return False
        if len(text) == 10:
            if (text[0] in string.ascii_uppercase or text[0] in dict_int_to_char.keys()) and \
                (text[1] in string.ascii_uppercase or text[1] in dict_int_to_char.keys()) and \
                (text[2] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[2] in dict_char_to_int.keys()) and \
                (text[3] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[3] in dict_char_to_int.keys()) and \
                (text[4] in string.ascii_uppercase or text[4] in dict_int_to_char.keys()) or text[4] == " "  and \
                (text[5] in string.ascii_uppercase or text[5] in dict_int_to_char.keys()) and \
                (text[6] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[6] in dict_char_to_int.keys()) and \
                (text[7] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[7] in dict_char_to_int.keys()) and \
                (text[8] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[8] in dict_char_to_int.keys()) and \
                (text[9] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[9] in dict_char_to_int.keys()):
                return True
        elif len(text) == 9:
            if (text[0] in string.ascii_uppercase or text[0] in dict_int_to_char.keys()) and \
                (text[1] in string.ascii_uppercase or text[1] in dict_int_to_char.keys()) and \
                (text[2] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[2] in dict_char_to_int.keys()) and \
                (text[3] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[3] in dict_char_to_int.keys()) and \
                (text[4] in string.ascii_uppercase or text[4] in dict_int_to_char.keys()) and \
                (text[5] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[5] in dict_char_to_int.keys()) and \
                (text[6] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[6] in dict_char_to_int.keys()) and \
                (text[7] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[7] in dict_char_to_int.keys()) and \
                (text[8] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[8] in dict_char_to_int.keys()):
                return True
        else:
            return False
        
    except Exception as e:
        logger.error(f"Error in number_plate_format: {e}")
        raise custom_exception(e)
    

    
def format_of_plate(text):
    try:
        number_plate = ""
        if len(text) == 10:
            mapping_for_10 = {0:dict_int_to_char,
                    1:dict_int_to_char,
                    2:dict_char_to_int,
                    3:dict_char_to_int,
                    4:dict_int_to_char,
                    5:dict_int_to_char,
                    6:dict_char_to_int,
                    7:dict_char_to_int,
                    8:dict_char_to_int,
                    9:dict_char_to_int}
            
            for i in list(range(10)):
                if text[i] in mapping_for_10[i].keys():
                    number_plate += mapping_for_10[i][text[i]]
                else:
                    number_plate += text[i]

            return number_plate
        
        elif len(text) == 9:
            mapping_for_9 = {0:dict_int_to_char,
                1:dict_int_to_char,
                2:dict_char_to_int,
                3:dict_char_to_int,
                4:dict_int_to_char,
                5:dict_char_to_int,
                6:dict_char_to_int,
                7:dict_char_to_int,
                8:dict_char_to_int}
            for i in list(range(9)):
                if text[i] in mapping_for_9[i].keys():
                    number_plate += mapping_for_9[i][text[i]]
                else:
                    number_plate += text[i]
            return number_plate
    except Exception as e:
        logger.error(f"Error in format_of_plate: {e}")
        raise custom_exception(e)