'''
All environment specific functions will be kept here

@author: puneethabm
'''

import os

def get_config_filename():
    """
    Set the environment variable 'PROJECT_CONFIG' to point to 'config' folder
    """
    config_file = "config_test.ini"
    
    if 'PROJECT_CONFIG' in os.environ:
        config_file = "config_test.ini"
        config_file = os.path.join(os.environ['PROJECT_CONFIG'] , config_file)
        
    return config_file