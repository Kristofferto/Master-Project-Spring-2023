import numpy as np
import matplotlib.pyplot as plt

import pandas as pd
import apexpy
from tqdm import tqdm, trange
data_list = ['Longitude', 'Timestamp', 'Latitude', 'Radius']
sat_list = ['A', 'B', 'C']


path = 'C:/Users/krisfau/Desktop/VSCode/Data/'

for sat in sat_list:
    for name in data_list:
        exec(f'{name}_{sat} = np.load("{path}Data_{sat}_{name}.npy", allow_pickle = True)')


for sat in sat_list:
    print(f'### Generating MLT data for satellite {sat}... ###')
    
    #Redefining variables for easier implementation
    exec(f'Timestamp = Timestamp_{sat}')
    exec(f'Longitude = Longitude_{sat}')
    exec(f'Latitude = Latitude_{sat}')

    #Converting the radius to satellite altitude measured in meters
    exec(f'Radius = Radius_{sat} / 1000 - 6371.009')

    #Creating an array for storing the MLT and MLAT data
    MLT_array = np.zeros(len(Timestamp))
    MLAT_array = np.zeros(len(Timestamp))
    
    for i in trange(len(Timestamp)):
        apex_out = apexpy.Apex(Timestamp[i])
        atime = pd.to_datetime(Timestamp[i])
        mlat, mlt = apex_out.convert(Latitude[i], Longitude[i], 'geo', 'mlt', datetime=atime, height = Radius[i])
        
        MLAT_array[i] = mlat
        MLT_array[i] = mlt
    
    #Saving the magnetic local time and magnetic latitude data
    print(f'### Currently saving the MLT and MLAT data for satellite {sat}... ###')
    np.save(f"C:/Users/krisfau/Desktop/VSCode/Data/Data_{sat}_MLT", MLT_array)
    np.save(f"C:/Users/krisfau/Desktop/VSCode/Data/Data_{sat}_MLAT", MLAT_array)

print('### The MLT data has been generated and stored locally ###')
