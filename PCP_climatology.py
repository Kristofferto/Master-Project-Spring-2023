import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from tqdm import tqdm, trange
import sys
from scipy import stats
import glob
import datetime
# data_list = ['Background_Ne', 'Foreground_Ne', 'Grad_Ne_at_100km', 'Grad_Ne_at_20km', 'Grad_Ne_at_50km', 'Grad_Ne_at_PCP_edge',  'Longitude', 'Ne', 'PCP_flag', 'Radius', 'Timestamp', 'Latitude', 'MLT']
data_list = ['Timestamp', 'MLAT']
sat_list = ['A', 'C']
hemisphere_indicator = ['NH', 'SH']

# path mac
path_mac = 'Data/'
savepath_mac = 'Figures/'

# path hjemme
path_hjemme = 'D:/Git_Codes/Data/'
savepath_hjemme = 'D:/Git_Codes/Figures/'


# path UiO
path_UiO = 'C:/Users/krisfau/Desktop/VSCode/Data/'
savepath_UiO = 'C:/Users/krisfau/Desktop/VSCode/FIGURES/'


savepath = savepath_mac
path = path_mac

for sat in tqdm(sat_list, desc = 'Loading locally stored data'):
    for name in data_list:
        exec(f'{name}_{sat} = np.load("{path}Data_{sat}_{name}.npy", allow_pickle = True)')

for indicator in hemisphere_indicator:
    #MLT 9-12
    exec(f'Data_fratio_{indicator}_Ne_9_12 = np.load("{path}Data_fratio_{indicator}_Ne_9_12.npy", allow_pickle = True)')
    exec(f'Data_fratio_{indicator}_Fg_9_12 = np.load("{path}Data_fratio_{indicator}_Fg_9_12.npy", allow_pickle = True)')
    exec(f'Data_fratio_{indicator}_array_index_9_12 = np.load("{path}Data_fratio_{indicator}_array_index_9_12.npy", allow_pickle = True)')

    #MLT 12-15
    exec(f'Data_fratio_{indicator}_Ne_12_15 = np.load("{path}Data_fratio_{indicator}_Ne_12_15.npy", allow_pickle = True)')
    exec(f'Data_fratio_{indicator}_Fg_12_15 = np.load("{path}Data_fratio_{indicator}_Fg_12_15.npy", allow_pickle = True)')
    exec(f'Data_fratio_{indicator}_array_index_12_15 = np.load("{path}Data_fratio_{indicator}_array_index_12_15.npy", allow_pickle = True)')

    #MLT 21-24
    exec(f'Data_fratio_{indicator}_Ne_21_24 = np.load("{path}Data_fratio_{indicator}_Ne_21_24.npy", allow_pickle = True)')
    exec(f'Data_fratio_{indicator}_Fg_21_24 = np.load("{path}Data_fratio_{indicator}_Fg_21_24.npy", allow_pickle = True)')
    exec(f'Data_fratio_{indicator}_array_index_21_24 = np.load("{path}Data_fratio_{indicator}_array_index_21_24.npy", allow_pickle = True)')

    #MLT 0-03
    exec(f'Data_fratio_{indicator}_Ne_0_03 = np.load("{path}Data_fratio_{indicator}_Ne_0_03.npy", allow_pickle = True)')
    exec(f'Data_fratio_{indicator}_Fg_0_03 = np.load("{path}Data_fratio_{indicator}_Fg_0_03.npy", allow_pickle = True)')
    exec(f'Data_fratio_{indicator}_array_index_0_03 = np.load("{path}Data_fratio_{indicator}_array_index_0_03.npy", allow_pickle = True)')

    #MLT 3-6
    exec(f'Data_fratio_{indicator}_Ne_3_6 = np.load("{path}Data_fratio_{indicator}_Ne_3_6.npy", allow_pickle = True)')
    exec(f'Data_fratio_{indicator}_Fg_3_6 = np.load("{path}Data_fratio_{indicator}_Fg_3_6.npy", allow_pickle = True)')
    exec(f'Data_fratio_{indicator}_array_index_3_6 = np.load("{path}Data_fratio_{indicator}_array_index_3_6.npy", allow_pickle = True)')

    #MLT 6-9
    exec(f'Data_fratio_{indicator}_Ne_6_9 = np.load("{path}Data_fratio_{indicator}_Ne_6_9.npy", allow_pickle = True)')
    exec(f'Data_fratio_{indicator}_Fg_6_9 = np.load("{path}Data_fratio_{indicator}_Fg_6_9.npy", allow_pickle = True)')
    exec(f'Data_fratio_{indicator}_array_index_6_9 = np.load("{path}Data_fratio_{indicator}_array_index_6_9.npy", allow_pickle = True)')

    #MLT 15-18
    exec(f'Data_fratio_{indicator}_Ne_15_18 = np.load("{path}Data_fratio_{indicator}_Ne_15_18.npy", allow_pickle = True)')
    exec(f'Data_fratio_{indicator}_Fg_15_18 = np.load("{path}Data_fratio_{indicator}_Fg_15_18.npy", allow_pickle = True)')
    exec(f'Data_fratio_{indicator}_array_index_15_18 = np.load("{path}Data_fratio_{indicator}_array_index_15_18.npy", allow_pickle = True)')

    #MLT 18-21
    exec(f'Data_fratio_{indicator}_Ne_18_21 = np.load("{path}Data_fratio_{indicator}_Ne_18_21.npy", allow_pickle = True)')
    exec(f'Data_fratio_{indicator}_Fg_18_21 = np.load("{path}Data_fratio_{indicator}_Fg_18_21.npy", allow_pickle = True)')
    exec(f'Data_fratio_{indicator}_array_index_18_21 = np.load("{path}Data_fratio_{indicator}_array_index_18_21.npy", allow_pickle = True)')
