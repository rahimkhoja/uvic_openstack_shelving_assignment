import os
import sqlite3
import datetime
from openstack import connection

# Environment variables
openstack_username = os.getenv('OPENSTACK_USERNAME')
openstack_password = os.getenv('OPENSTACK_PASSWORD')
openstack_domain = os.getenv('OPENSTACK_DOMAIN')
research_it_email = os.getenv('RESEARCH_IT_EMAIL')
sqlite_db_path = os.getenv('SQLITE_DB_PATH')
