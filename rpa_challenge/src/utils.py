import os
import logging
from datetime import datetime

def pylog(message):
    """
    Set up logging configuration with a folder and timestamped log files, and log a message.
    """
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M")
    log_file  = os.path.join(log_dir, f"log_{timestamp}.log")

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )
    logging.info(message)
