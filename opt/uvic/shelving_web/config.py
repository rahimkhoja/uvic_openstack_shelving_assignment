import os

class Config:
    LOG_PATH = os.getenv('LOG_PATH', "/var/log/uvic/")
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', "sqlite:////opt/uvic/shelving_web/shelving.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS', 'False')
    if SQLALCHEMY_TRACK_MODIFICATIONS.upper() == "FALSE":
        SQLALCHEMY_TRACK_MODIFICATIONS = False
    else:
        SQLALCHEMY_TRACK_MODIFICATIONS = True	
    GOOGLE_ANALYTICS_ID = os.getenv('GOOGLE_ANALYTICS_ID')
    if GOOGLE_ANALYTICS_ID and GOOGLE_ANALYTICS_ID.upper() == 'NONE':
        GOOGLE_ANALYTICS_ID = None
    GOOGLE_SITE_VERIFICATION = os.getenv('GOOGLE_SITE_VERIFICATION')
    if GOOGLE_SITE_VERIFICATION and GOOGLE_SITE_VERIFICATION.upper() == 'NONE':
        GOOGLE_SITE_VERIFICATION = None
    BING_SITE_VERIFICATION = os.getenv('BING_SITE_VERIFICATION')
    if BING_SITE_VERIFICATION and BING_SITE_VERIFICATION.upper() == 'NONE':
        BING_SITE_VERIFICATION = None
    SYSTEM_MAINTENANCE_MODE = os.getenv('SYSTEM_MAINTENANCE_MODE', 'False')
    EMAIL_SERVER = os.getenv('EMAIL_SERVER', 'smtp.uvic.ca')
    EMAIL_PORT = int(os.getenv('EMAIL_PORT', '587'))
    EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS', 'True')
    RT_USERNAME = os.getenv('RT_USERNAME')
    RT_PASSWORD = os.getenv('RT_PASSWORD')
    RT_QUEUE = os.getenv('RT_QUEUE', 'AUTOSHELVING')
