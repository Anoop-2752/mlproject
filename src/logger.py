import logging
import os
from datetime import datetime

# Corrected LOG_FILE to avoid the escape sequence issue
LOG_FILE = f"{datetime.now().strftime('%m_%d_%y_%H_%M_%S')}.log"

# Constructing the logs path
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)

# Full log file path
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Setting up logging configuration
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


