import os
import sys
import logging

# Define logging format
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Define directory and file path for log files
log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")

# Create the logs directory if it doesn't exist
os.makedirs(log_dir, exist_ok=True)

# Configure logging settings
logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),  # Log to a file
        logging.StreamHandler(sys.stdout)   # Log to stdout (console)
    ]
)

# Create a logger instance
logger = logging.getLogger("cnnClassifierLogger")
