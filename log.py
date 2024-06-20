import os
import jdatetime 
import logging
from jdatetime import datetime as jdatetime


LOG_BASE_DIR = "logs"
os.makedirs(LOG_BASE_DIR, exist_ok=True)
class JalaliFormatter(logging.Formatter):
    def formatTime(self, record, datefmt=None):
        return jdatetime.now().strftime('%Y-%m-%d %H:%M:%S')



#_______ Logger For handling errors
error_logger = logging.getLogger('error_logger')
error_logger.setLevel(logging.ERROR)
error_file_handler = logging.FileHandler(os.path.join(LOG_BASE_DIR, 'errors.log'))
error_file_handler.setLevel(logging.ERROR)
error_file_handler.setFormatter(JalaliFormatter('%(asctime)s : %(message)s'))
error_logger.addHandler(error_file_handler)


# _______ infoentication APP logger
info_logger = logging.getLogger('info_logger')
info_logger.setLevel(logging.INFO)
info_file_handler = logging.FileHandler(os.path.join(LOG_BASE_DIR, 'info.log'))
info_file_handler.setLevel(logging.INFO)
info_file_handler.setFormatter(JalaliFormatter('%(asctime)s : %(message)s'))
info_logger.addHandler(info_file_handler)
