'''
Config Parser example

@author: puneethabm
'''

from pbm_python_config_parser.common import utils as utils

def main():
    """
    Read configuration parameters - Example
    """

    print("Reading Table configuration")
    config = utils.run_config_instance()
    source_section = config["sample_source_name"]
    source_stage1 = source_section["my_first_source"]["stage1"]
    
    source_table = source_stage1["source_table"]
    destination_table = source_stage1["destination_table"]
    destination_location = source_stage1["destination_location"]
    
    print("""source_section={}
            , source_table={}
            , destination_table={}
            , destination_location={}
            """ .format(source_section
                       , source_table
                       , destination_table
                       , destination_location
                )
          )  
    
if __name__ == '__main__':
    main()