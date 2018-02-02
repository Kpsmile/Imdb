"""Configuration file for the application."""
import os


from configobj import ConfigObj


# Instantiating the ConfigObj and reading the ini file to use
# hardcoded values like loggers. The ini path is
# hardcoded for now we can make it dynamic depending on our need in future.

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config_path = os.path.join(BASE_DIR, 'config', 'config.ini')
config = ConfigObj(config_path, interpolation=False)

def get_application_port():
    return int(config['SERVERSETTINGS']['application_port'])


def get_db_url():
    db = config['DATABASE']
    return '{0}+pymysql://{1}:{2}@{3}/{4}'.format(db['DRIVER'], db['USER'], db['PASSWORD'], db['HOST'],
                                                  db['DATABASE_NAME'])
