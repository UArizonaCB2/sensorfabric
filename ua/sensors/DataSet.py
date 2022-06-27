"""
Module which is responsible for loading various different datasets.
"""

import os
import Raw

def load_data(namespace : str, tag : str, path : str):
    """
    Returns the requested dataset.
    User must be authorized to access this dataset.

    Parameters
    -----------
    namespace : Project namespace
    tag : Sensor tag, for example "fitbit", "apple", "garmin", "empatica", etc.
    path : The data set path
    """

    # For now this method is rather dumb. Based on the namespace requested it 
    # will return one of the pre-populated dataset. 

    if not 'DATA_BASE_DIR' in os.environ:
        print('$DATA_BASE_DIR must be set when running in folder mode')

    BASE_DIR = os.environ['DATA_BASE_DIR']

    # In directoy / local mode, data is referenced as 
    # BASE_DIR / namespace / tag / path

    fullpath = BASE_DIR+'/'+namespace+'/'+tag+'/'+path
    # Check if the path is a regular file.
    if not os.path.isfile(fullpath):
        print('load_data : Path must terminate into a valid regular file')
        return None

    (ret, json_buffer) = Raw.scanJsonFile(fullpath)
    if not ret:
        return None

    print('Data has been loaded and returned')
    return json_buffer

if __name__ == '__main__':
    json_buffer = load_data('cb2', 'fitbit', '20220620-20220621/fitbit_intraday_activities_heart/MDH-4950-2492/activities_heart_date_2022-06-19_1d_1sec.json')

    if not json_buffer is None:
        Raw.prettyPrintSchema(json_buffer[0])  
