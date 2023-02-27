import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from tqdm import tqdm, trange
# data_list = ['Background_Ne', 'Foreground_Ne', 'Grad_Ne_at_100km', 'Grad_Ne_at_20km', 'Grad_Ne_at_50km', 'Grad_Ne_at_PCP_edge',  'Longitude', 'Ne', 'PCP_flag', 'Radius', 'Timestamp', 'Latitude', 'MLT']
data_list = ['Ne', 'PCP_flag', 'Timestamp', 'MLT', 'MLAT']
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

#håper du liker bolognese

def PCP_plotter(PCP, MLT, MLT_max, MLT_min, MLAT, Ne, Time, sat):
    ncount = 0    
    scount = 0

    for i in trange(0, len(PCP), 2, desc = F'Finding and plotting PCP for satellite {sat}'):
        #, desc = 'Finding and plotting PCP'
        
        if MLAT[PCP[i]] > MLAT[PCP[i+1]]:
            start = PCP[i+1]
            end = PCP[i]
        elif MLAT[PCP[i]] < MLAT[PCP[i+1]]:
            start = PCP[i]
            end = PCP[i+1]
        
        # start -= 5
        # end += 5
        
        x_range = np.linspace(0, 100, 100001)

        # & (MLT_max >= MLT[start] >= MLT_min) & (MLT_min <= MLT[end] <= MLT_max)
        # & (np.all(( MLT_max >= MLT[start:end] >= MLT_min)) == True)

        if (np.all((MLAT[start:end] > 0)) == True) & (np.all((Ne[start:end] > 0)) == True) & (MLT_max >= MLT[start] >= MLT_min) & (MLT_min <= MLT[end] <= MLT_max) & ((end - start) > 30) & ((MLAT[end] - MLAT[start]) > 3) & (np.isnan(MLT[start]) == False) & (np.isnan(MLT[end]) == False):
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

            plt.title('Polar Cap Patches Northern Hemisphere. Dayside.')
            plt.xlabel('MLAT')
            plt.ylabel('Ne')
            # plt.plot(MLAT[start:end], Ne[start:end], label = f'SWARM {sat}. Patch number: {ncount}')
            plt.plot(x_range, y1, label = f'SWARM {sat}. Patch number: {ncount}')
            # plt.annotate(xy =(MLAT[start+5], Ne[start+5]), text = 'PCP start.')
            # plt.annotate(xy = (MLAT[end-5], Ne[end-5]), text = 'PCP end.')
            # plt.vlines(MLAT[start], linestyles = 'dotted', label = 'PCP start', color = 'black')
            # plt.vlines(MLAT[end], linestyles = 'dotted', label = 'PCP end', color = 'black')
            #plt.yscale('log')


            if ncount % 5 == 0:
                plt.legend(loc = 'lower center', fontsize = 10)
                plt.savefig(f'SWARM_{sat}_PCP{ncount}_MLT{MLT_max}_{MLT_min}.png')
                plt.close()
        if ncount == 55:
            break
            
            
        
# for sat in sat_list:
#     exec(f'PCP_plotter(PCP_index_{sat}, MLT_{sat}, MLAT_{sat}, Ne_{sat}, Timestamp_{sat}, sat)')

#PCP_plotter(PCP, MLT, MLT_max, MLT_min MLAT, Ne, Time, sat)

#Input variables for plotting

MLT_max_list = np.array([12, 15, 24, 3])
MLT_min_list = np.array([9, 12, 21, 24])

for sat in sat_list:
    for i in range(len(MLT_max_list)):
        MLT_max = MLT_max_list[i]
        MLT_min = MLT_min_list[i]
        exec(f'PCP_plotter(PCP_index_{sat}, MLT_{sat}, MLT_max, MLT_min, MLAT_{sat}, Ne_{sat}, Timestamp_{sat}, sat)')



# PCP_plotter(PCP_index_A, MLT_A, MLT_max, MLT_min, MLAT_A, Ne_A, Timestamp_A, 'A')
# PCP_plotter(PCP_index_B, MLT_B, MLAT_B, Ne_B, Timestamp_B, 'B')
# PCP_plotter(PCP_index_C, MLT_C, MLAT_C, Ne_C, Timestamp_C, 'C')

def PCP_plotter123(PCP, MLT, MLAT, Ne, Time):
    for i in trange(0, len(PCP), 2, desc = 'Plotting PCP'):
        if MLAT[i] > 0:
            plt.title('Polar Cap Patches Northern Hemisphere')
            plt.scatter(Time[patch_start:patch_end], Ne[patch_start:patch_end], label = 'Ne', marker = '.')




# plt.title('Testplot')
# plt.scatter(Timestamp_A[100000:100200] ,Ne_A[100000:100200], label = 'Ne', marker = '.')
# plt.scatter(Timestamp_A[100000:100200] ,PCP_flag_A[100000:100200]*1000, label = 'PCP flag', marker = '.')
# plt.legend()
# plt.show()
