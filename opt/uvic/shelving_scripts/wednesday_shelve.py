import os
import sqlite3
import logging
from openstack import connection
from datetime import datetime

def load_database(db_path):
    """ Load and return the database connection. """
    try:
        conn = sqlite3.connect(db_path)
        logger.info("Database connected successfully.")
        return conn
    except sqlite3.Error as e:
        logger.error(f"Failed to connect to the database: {e}")
        return None

def get_shelving_records(conn, vm_name=None, email=None, shelve_date=None):
    """
    Retrieve records from the shelving table.
    Filter by VM_Name, Email, and Shelve_Date if provided.
    """
    try:
        cursor = conn.cursor()
        query = "SELECT * FROM shelving WHERE 1=1"
        params = []
        
        if vm_name:
            query += " AND VM_Name = ?"
            params.append(vm_name)
        if email:
            query += " AND Email = ?"
            params.append(email)
        if shelve_date:
            query += " AND Shelve_Date = ?"
            params.append(shelve_date)
        
        cursor.execute(query, params)
        records = cursor.fetchall()
        logger.info(f"Retrieved {len(records)} records from the database.")
        return records
    except sqlite3.Error as e:
        logger.error(f"Error retrieving records: {e}")
        return []


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
log_filename = f'auto_shelve_sunday_{current_date}.log'
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
