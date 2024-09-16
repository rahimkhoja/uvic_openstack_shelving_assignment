import sqlite3
from openstack import connection
import logging
import os
from datetime import datetime

# Environment variables
openstack_username = os.getenv('OPENSTACK_USERNAME')
openstack_password = os.getenv('OPENSTACK_PASSWORD')
openstack_domain = os.getenv('OPENSTACK_DOMAIN')
research_it_email = os.getenv('RESEARCH_IT_EMAIL')
sqlite_db_path = os.getenv('SQLITE_DB_PATH')

# Create logs directory if it doesn't exist
logs_directory = './logs'
if not os.path.exists(logs_directory):
    os.makedirs(logs_directory)

# Configure the logging
current_date = datetime.now().strftime("%d-%m-%Y")
log_filename = f'auto_shelve_monday_{current_date}.log'
log_path = os.path.join(logs_directory, log_filename)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler(log_path),
        logging.StreamHandler()  # To also print to stdout
    ]
)

# Example usage
logger = logging.getLogger(__name__)
logger.info("This is an informational message.")

def main():
    logger.info("The main function started.")
    # Your code logic here
    logger.info("The main function finished.")

if __name__ == "__main__":
    main()
