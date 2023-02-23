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

PCP_flag_A = PCP_flag_A
en = np.where((PCP_flag_A == 0) & (PCP_flag_A != np.roll(PCP_flag_A,1)))[0]
to = np.where((PCP_flag_A == 0) & (PCP_flag_A != np.roll(PCP_flag_A,-1)))[0]

PCP_indices = np.concatenate((en, to))
PCP_index_list = np.sort(PCP_indices)



def PCP_plotter(PCP, MLT, MLAT, Ne, Time):
    ncount = 0    
    scount = 0

    for i in trange(0, len(PCP), 2, desc = 'Finding and plotting PCP'):
        
        if MLAT_A[PCP[i]] > MLAT_A[PCP[i+1]]:
            start = PCP[i+1]
            end = PCP[i]
        elif MLAT_A[PCP[i]] < MLAT_A[PCP[i+1]]:
            start = PCP[i]
            end = PCP[i+1]
        if MLAT[i] > 0 and MLAT[i+1] > 0:
            ncount +=1
            fig1, ax1 = plt.subplots()
            ax1.title.set_text('Polar Cap Patches Northern Hemisphere')
            ax1.scatter(np.arange(0,end - start), Ne[start:end], label = f'Patch_{ncount}', marker = '.')
        elif MLAT[i] < 0 and MLAT[i+1] < 0:
            scount +=1
            fig2, ax2 = plt.subplots()
            ax2.title.set_text('Polar Cap Patches Southern Hemisphere')
            ax2.scatter(np.arange(0,end - start), Ne[start:end], label = f'Patch_{scount}', marker = '.')
        if ncount == 10:
            fig1.legend()
            fig1.savefig('test1')
            
            ncount = 0
        elif scount == 10:
            fig2.legend()
            fig2.savefig('test2')
            
            scount = 0
        

PCP_plotter(PCP_index_list, MLT_A, MLAT_A, Ne_A, Timestamp_A)

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
