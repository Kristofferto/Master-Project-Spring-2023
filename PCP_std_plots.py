import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from tqdm import tqdm, trange
import sys
from scipy import stats
# data_list = ['Background_Ne', 'Foreground_Ne', 'Grad_Ne_at_100km', 'Grad_Ne_at_20km', 'Grad_Ne_at_50km', 'Grad_Ne_at_PCP_edge',  'Longitude', 'Ne', 'PCP_flag', 'Radius', 'Timestamp', 'Latitude', 'MLT']
data_list = ['Ne', 'PCP_flag', 'Timestamp', 'MLT', 'MLAT', 'Foreground_Ne']
sat_list = ['A', 'C']

#path mac
# path = 'Data/'
# #path hjemme
# path = 'D:\\Git_Codes\\Data\\'

# #path UiO
path = 'C:/Users/krisfau/Desktop/VSCode/Data/'


for sat in tqdm(sat_list, desc = 'Loading satellite data'):
    for name in data_list:
        exec(f'{name}_{sat} = np.load("{path}Data_{sat}_{name}.npy", allow_pickle = True)')
