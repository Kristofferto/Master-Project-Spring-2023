import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from tqdm import tqdm, trange
# data_list = ['Background_Ne', 'Foreground_Ne', 'Grad_Ne_at_100km', 'Grad_Ne_at_20km', 'Grad_Ne_at_50km', 'Grad_Ne_at_PCP_edge',  'Longitude', 'Ne', 'PCP_flag', 'Radius', 'Timestamp', 'Latitude', 'MLT']
data_list = ['Ne', 'PCP_flag', 'Timestamp', 'MLT', 'MLAT']
sat_list = ['A', 'B', 'C']

#path mac
path = 'Data/'
# #path hjemme
path = 'D:\\Git_Codes\\Data\\'

# #path UiO
# path = 'C:/Users/krisfau/Desktop/VSCode/Data/'



for sat in tqdm(sat_list, desc = 'Loading satellite data'):
    for name in data_list:
        exec(f'{name}_{sat} = np.load("{path}Data_{sat}_{name}.npy", allow_pickle = True)')

for name in sat_list:
    exec(f'change01 = np.where((PCP_flag_{name} == 0) & (PCP_flag_{name} != np.roll(PCP_flag_{name},1)))[0]')
    exec(f'change10 = np.where((PCP_flag_{name} == 0) & (PCP_flag_{name} != np.roll(PCP_flag_{name},-1)))[0]')
    PCP_indices = np.concatenate((change01, change10))
    exec(f'PCP_index_{name} = np.sort(PCP_indices)')

#håper du liker bolognese

def PCP_plotter(PCP, MLT, MLAT, Ne, Time):
    ncount = 0    
    scount = 0

    for i in range(0, len(PCP), 2):
        #, desc = 'Finding and plotting PCP'
        
        if MLAT[PCP[i]] > MLAT[PCP[i+1]]:
            start = PCP[i+1]
            end = PCP[i]
        elif MLAT[PCP[i]] < MLAT[PCP[i+1]]:
            start = PCP[i]
            end = PCP[i+1]
        if MLAT[start] > 0 and MLAT[end] > 0 and 12 > MLT[start] > 9 and 9 < MLT[end] < 12 and np.abs(start - end) > 100 and np.abs(MLAT[start] - MLAT[end]) > 2:
            ncount +=1
            print('start:', start)
            print('end:', end)
            print('lengde:', np.abs(start-end))
            # fig1, ax1 = plt.subplots()
            plt.title('Polar Cap Patches Northern Hemisphere. Dayside.')
            plt.xlabel('MLAT')
            plt.ylabel('Ne')
            plt.plot(MLAT[start:end], Ne[start:end], label = f'Patch number: {ncount}', marker = '.')

            if ncount % 3 == 0:
                plt.legend()
                plt.savefig(f'test_{ncount}')
                plt.close()

        # elif MLAT[start] < 0 and MLAT[end] < 0:
        #     scount +=1
        #     fig2, ax2 = plt.subplots()
        #     ax2.title.set_text('Polar Cap Patches Southern Hemisphere')
        #     ax2.plot(np.arange(0,end - start), Ne[start:end], label = f'Patch number: {scount}', marker = '.')

        #     if scount % 5 == 0:
        #         fig2.legend()
        #         fig2.savefig(f'test_{scount}')
        #         plt.close()

        #Save each plot of 5 PCPs
        # if ncount % 5 == 0:
        #     fig1.legend()
        #     fig1.savefig(f'test_{ncount}')
            
            
        # elif scount % 5 == 0:
        #     fig2.legend()
        #     fig2.savefig(f'test_{scount}')
            
            
            
            
            
        
for name in sat_list:
    exec(f'PCP_plotter(PCP_index_{name}, MLT_{name}, MLAT_{name}, Ne_{name}, Timestamp_{name})')

def PCP_plotter(PCP, MLT, MLAT, Ne, Time):
    for i in trange(0, len(PCP), 2, desc = 'Plotting PCP'):
        if MLAT[i] > 0:
            plt.title('Polar Cap Patches Northern Hemisphere')
            plt.scatter(Time[patch_start:patch_end], Ne[patch_start:patch_end], label = 'Ne', marker = '.')





"""

        elif MLAT[i] < 0:
            #southern hemisphere

            Southcount += 1
            patch_start = 
            patch_end = 
            plt.title('Polar Cap Patches Southern Hemisphere')
            plt.scatter(Time[patch_start:patch_end], Ne[patch_start:patch_end], label = 'Ne', marker = '.')
            plt.legend()
"""


# plt.title('Testplot')
# plt.scatter(Timestamp_A[100000:100200] ,Ne_A[100000:100200], label = 'Ne', marker = '.')
# plt.scatter(Timestamp_A[100000:100200] ,PCP_flag_A[100000:100200]*1000, label = 'PCP flag', marker = '.')
# plt.legend()
# plt.show()
