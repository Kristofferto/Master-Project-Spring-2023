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

N_9_12 = Data_fratio_NH_Ne_9_12
S_9_12 = Data_fratio_SH_Ne_9_12
N_index_9_12 = Data_fratio_NH_array_index_9_12
S_index_9_12 = Data_fratio_SH_array_index_9_12

N_12_15 = Data_fratio_NH_Ne_12_15
S_12_15 = Data_fratio_SH_Ne_12_15
N_index_12_15 = Data_fratio_NH_array_index_12_15
S_index_12_15 = Data_fratio_SH_array_index_12_15

N_21_24 = Data_fratio_NH_Ne_21_24
S_21_24 = Data_fratio_SH_Ne_21_24
N_index_21_24 = Data_fratio_NH_array_index_21_24
S_index_21_24 = Data_fratio_SH_array_index_21_24

N_0_03 = Data_fratio_NH_Ne_0_03
S_0_03 = Data_fratio_SH_Ne_0_03
N_index_0_03 = Data_fratio_NH_array_index_0_03
S_index_0_03 = Data_fratio_SH_array_index_0_03

N_3_6 = Data_fratio_NH_Ne_3_6
S_3_6 = Data_fratio_SH_Ne_3_6
N_index_3_6 = Data_fratio_NH_array_index_3_6
S_index_3_6 = Data_fratio_SH_array_index_3_6

N_6_9 = Data_fratio_NH_Ne_6_9
S_6_9 = Data_fratio_SH_Ne_6_9
N_index_6_9 = Data_fratio_NH_array_index_6_9
S_index_6_9 = Data_fratio_SH_array_index_6_9

N_15_18 = Data_fratio_NH_Ne_15_18
S_15_18 = Data_fratio_SH_Ne_15_18
N_index_15_18 = Data_fratio_NH_array_index_15_18
S_index_15_18 = Data_fratio_SH_array_index_15_18

N_18_21 = Data_fratio_NH_Ne_18_21
S_18_21 = Data_fratio_SH_Ne_18_21
N_index_18_21 = Data_fratio_NH_array_index_18_21
S_index_18_21 = Data_fratio_SH_array_index_18_21

#Function to find where the indices starts to indicate data for satellite C and not A 
# - this is used to indicate where the timestamp data needs to be changed
def find_index(array):
    index = -1
    for i in range(1, len(array)):
        if array[i] < array[i-1]:
            index = i 
            break 
    return index


def Hour_date():
    pass 

def PCP_climatology(index_array):
    max_date = datetime.datetime = (2020, 1, 1)
    PCP_index_list_A = []
    PCP_index_list_C = []

    #Satellite A
    for i in range(0, len(index_array), 2):
        if i <= find_index(index_array) - 1:
            PCP_index_A = int((index_array[i+1] + index_array[i]) / 2)
            PCP_index_list_A.append(PCP_index_A)
        elif i > find_index(index_array) - 1:
            PCP_index_C = int((index_array[i+1] + index_array[i]) / 2)
            PCP_index_list_C.append(PCP_index_C)





    print(len(PCP_index_list_A))
    print(len(PCP_index_list_C))
    return PCP_index_list_A, PCP_index_list_C
#        while (Timestamp_A[i] < max_date) == True:
#            for k in range(0, len(index_array), 2):
#                print(k)
#     
PCP_climatology(N_index_9_12)

print(N_index_9_12[630:640])
print(N_index_9_12[:10])

#         # plot andres timeseries of polar cap patches for winter and summer.