import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from tqdm import tqdm, trange
# data_list = ['Background_Ne', 'Foreground_Ne', 'Grad_Ne_at_100km', 'Grad_Ne_at_20km', 'Grad_Ne_at_50km', 'Grad_Ne_at_PCP_edge',  'Longitude', 'Ne', 'PCP_flag', 'Radius', 'Timestamp', 'Latitude', 'MLT']
data_list = ['Ne', 'PCP_flag', 'Timestamp', 'MLT', 'MLAT', 'Background_Ne']
sat_list = ['A', 'B', 'C']

#path mac
# path = 'Data/'
# #path hjemme
# path = 'D:\\Git_Codes\\Data\\'

# #path UiO
path = 'C:/Users/krisfau/Desktop/VSCode/Data/'


for sat in tqdm(sat_list, desc = 'Loading satellite data'):
    for name in data_list:
        exec(f'{name}_{sat} = np.load("{path}Data_{sat}_{name}.npy", allow_pickle = True)')

for sat in sat_list:
    exec(f'change01 = np.where((PCP_flag_{sat} == 0) & (PCP_flag_{sat} != np.roll(PCP_flag_{sat},1)))[0]')
    exec(f'change10 = np.where((PCP_flag_{sat} == 0) & (PCP_flag_{sat} != np.roll(PCP_flag_{sat},-1)))[0]')
    PCP_indices = np.concatenate((change01, change10))
    exec(f'PCP_index_{sat} = np.sort(PCP_indices)')


for sat in sat_list:
    exec(f'change14 = np.where((PCP_flag_{sat} == 4) & (PCP_flag_{sat} != np.roll(PCP_flag_{sat},1)))[0]')
    exec(f'change41 = np.where((PCP_flag_{sat} == 4) & (PCP_flag_{sat} != np.roll(PCP_flag_{sat},-1)))[0]')
    PCP_proper = np.concatenate((change14, change41))
    exec(f'PCP_proper_{sat} = np.sort(PCP_proper)')
print(PCP_index_A)
print(PCP_proper_A)

break
def PCP_std(PCP, MLT, MLT_max, MLT_min, MLAT, Ne, Time, sat, Background, PCP_flag, PCP_proper):
    ncount = 0    

    for i in range(0, len(PCP), 2):
        #, desc = F'Finding and plotting PCP for satellite {sat}'
        
        if np.abs(MLAT[PCP[i]]) > np.abs(MLAT[PCP[i+1]]):
            start = PCP[i+1]
            end = PCP[i]
            start_prop = PCP_proper[i+1]
            end_prop = PCP_proper[i]

        elif np.abs(MLAT[PCP[i]]) < np.abs(MLAT[PCP[i+1]]):
            start = PCP[i]
            end = PCP[i+1]
            start_prop = PCP_proper[i]
            end_prop = PCP_proper[i+1]
        
        x_range = np.linspace(0, 100, 100001)

        # & (MLT_max >= MLT[start] >= MLT_min) & (MLT_min <= MLT[end] <= MLT_max)
        # & (np.all(( MLT_max >= MLT[start:end] >= MLT_min)) == True)

        if (np.all((MLAT[start:end] > 0)) == True) & (np.all((Ne[start:end] > 0)) == True) & \
                                                     (MLT_max >= MLT[start] >= MLT_min) & \
                                                     (MLT_min <= MLT[end] <= MLT_max) & \
                                                     ((end - start) > 30) & \
                                                     (np.abs(MLAT[end] - MLAT[start]) > 3) & \
                                                     (np.isnan(MLT[start]) == False) & \
                                                     (np.isnan(MLT[end]) == False) & \
                                                     (np.any((PCP_flag[start:end] == 4))):
            print(Ne[start:start_prop])
            print(Ne[end_prop:end])
            a = np.std(Ne[start:start_prop])
            b = np.std(Ne[end_prop:end])
            b = np.std([1,2,3,4,5,6,7,8,9,10])
            print('Std trail:', a)
            print('Std trail:', b)
            
            ncount +=1
            # print('#######')
            # print('start:', start)
            # print('end:', end)
            # print('lengde:', np.abs(start-end))
            # print('count:', ncount)
            # print('Ne start:', Ne[start])
            # print('Ne end:', Ne[end])
            # print('MLAT start:', MLAT[start])
            # print('MLAT end:', MLAT[end])

 
        if ncount == 5:
            break
            
            
        
# for sat in sat_list:
#     exec(f'PCP_plotter(PCP_index_{sat}, MLT_{sat}, MLAT_{sat}, Ne_{sat}, Timestamp_{sat}, sat)')

#PCP_plotter(PCP, MLT, MLT_max, MLT_min MLAT, Ne, Time, sat)

#Input variables for plotting

MLT_max_list = np.array([12, 15, 24, 3])
MLT_min_list = np.array([9, 12, 21, 0])

for sat in sat_list[0]:
    for i in range(len(MLT_max_list)):
        MLT_max = MLT_max_list[0]
        MLT_min = MLT_min_list[0]
        exec(f'PCP_std(PCP_index_{sat}, MLT_{sat}, MLT_max, MLT_min, MLAT_{sat}, Ne_{sat}, Timestamp_{sat}, sat, Background_Ne_{sat}, PCP_flag_{sat}, PCP_proper_{sat})')
        plt.close()



