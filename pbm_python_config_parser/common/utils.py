'''
General Utilities

@author: puneethabm
'''

from configobj import ConfigObj

from pbm_python_config_parser.common import settings as settings

def run_config_instance():
    config_file = settings.get_config_filename()
    print("Config File Location: {}".format(config_file))
    
    config = ConfigObj(config_file)
    return config