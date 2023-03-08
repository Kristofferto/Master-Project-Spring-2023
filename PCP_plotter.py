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


# for sat in sat_list:
#     exec(f'change14 = np.where((PCP_flag_{sat} == 4) & (PCP_flag_{sat} != np.roll(PCP_flag_{sat},1)))[0]')
#     exec(f'change41 = np.where((PCP_flag_{sat} == 4) & (PCP_flag_{sat} != np.roll(PCP_flag_{sat},-1)))[0]')
#     PCP_proper = np.concatenate((change14, change41))
#     exec(f'PCP_proper_{sat} = np.sort(PCP_proper)')



def PCP_plotter(PCP, MLT, MLT_max, MLT_min, MLAT, Ne, Time, sat, Background, PCP_flag):
    ncount = 0    
    scount = 0

    for i in trange(0, len(PCP), 2, desc = F'Finding and plotting PCP for satellite {sat}'):
        #, desc = 'Finding and plotting PCP'

        if (9 <= MLT_max <= 15) & (9 <= MLT_min <= 15):
            if np.abs(MLAT[PCP[i]]) > np.abs(MLAT[PCP[i+1]]):
                start = PCP[i+1]
                end = PCP[i]

            elif np.abs(MLAT[PCP[i]]) < np.abs(MLAT[PCP[i+1]]):
                start = PCP[i]
                end = PCP[i+1]
                
        elif ((21 <= MLT_max <= 24) & (21 <= MLT_min <= 24)) | (( 0 <= MLT_max <= 3) & (0 <= MLT_min <= 3)):
            if np.abs(MLAT[PCP[i]]) < np.abs(MLAT[PCP[i+1]]):
                start = PCP[i+1]
                end = PCP[i]

            elif np.abs(MLAT[PCP[i]]) > np.abs(MLAT[PCP[i+1]]):
                start = PCP[i]
                end = PCP[i+1]
        
        # if np.abs(MLAT[PCP[i]]) > np.abs(MLAT[PCP[i+1]]):
        #     start = PCP[i+1]
        #     end = PCP[i]

        # elif np.abs(MLAT[PCP[i]]) < np.abs(MLAT[PCP[i+1]]):
        #     start = PCP[i]
        #     end = PCP[i+1]
        
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

            y1 = np.interp(x_range, np.linspace(0, 100, len(MLAT[start:end])), Ne[start:end])

            
            #plt.xlabel('MLAT')
            plt.ylabel('Ne ($10^4 cm^{-3}$)')
            # plt.plot(MLAT[start:end], Ne[start:end] / 1e4, label = f'SWARM {sat}. PCP #{ncount}')
            # plt.plot(MLAT[start:end], Background[start:end] / 1e4, label = f'SWARM {sat}. Background. PCP #{ncount}')
            plt.plot(x_range, y1 /1e4, label = f'SWARM {sat}. Patch number: {ncount}')
            # plt.annotate(xy =(MLAT[start+5], Ne[start+5]), text = 'PCP start.')
            # plt.annotate(xy = (MLAT[end-5], Ne[end-5]), text = 'PCP end.')
            # plt.vlines(MLAT[start], linestyles = 'dotted', label = 'PCP start', color = 'black')
            # plt.vlines(MLAT[end], linestyles = 'dotted', label = 'PCP end', color = 'black')
            # plt.yscale('log')


            if ncount % 5 == 0:
                plt.title(f'Five Polar Cap Patches Northern Hemisphere, SWARM {sat}. \n For MLT {MLT_min}-{MLT_max}')
                plt.legend(loc = 'lower center', fontsize = 5)
                plt.savefig(f'NH_SWARM_{sat}_MLT{MLT_max}_{MLT_min}_PCP{ncount}.png')
                plt.close()
        # if ncount == 20:
        #     break
            
            
        
# for sat in sat_list:
#     exec(f'PCP_plotter(PCP_index_{sat}, MLT_{sat}, MLAT_{sat}, Ne_{sat}, Timestamp_{sat}, sat)')

#PCP_plotter(PCP, MLT, MLT_max, MLT_min MLAT, Ne, Time, sat)

#Input variables for plotting

MLT_max_list = np.array([12, 15, 24, 3])
MLT_min_list = np.array([9, 12, 21, 0])

for sat in sat_list:
    for i in range(len(MLT_max_list)):
        MLT_max = MLT_max_list[i]
        MLT_min = MLT_min_list[i]
        exec(f'PCP_plotter(PCP_index_{sat}, MLT_{sat}, MLT_max, MLT_min, MLAT_{sat}, Ne_{sat}, Timestamp_{sat}, sat, Background_Ne_{sat}, PCP_flag_{sat})')
        plt.close()



