import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm, trange

data_list = ['Ne', 'PCP_flag', 'Timestamp', 'MLT', 'MLAT', 'Background_Ne']
sat_list = ['A', 'B', 'C']

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

#Loading the satellite data
for sat in tqdm(sat_list, desc = 'Loading satellite data'):
    for name in data_list:
        exec(f'{name}_{sat} = np.load("{path}Data_{sat}_{name}.npy", allow_pickle = True)')

#Locating where the PCP flag index changes from 0 to 1 and 1 to 0
for sat in sat_list:
    exec(f'change01 = np.where((PCP_flag_{sat} == 0) & (PCP_flag_{sat} != np.roll(PCP_flag_{sat},1)))[0]')
    exec(f'change10 = np.where((PCP_flag_{sat} == 0) & (PCP_flag_{sat} != np.roll(PCP_flag_{sat},-1)))[0]')
    PCP_indices = np.concatenate((change01, change10))
    exec(f'PCP_index_{sat} = np.sort(PCP_indices)')


def PCP_plotter(PCP, MLT, MLT_max, MLT_min, MLAT, Ne, Time, sat, Background, PCP_flag):
    ###Function to plots PCPs five at a time###
    PCP_count = 0    
 
    for i in trange(0, len(PCP), 2, desc = F'Finding and plotting PCP for satellite {sat}'):

        #Setting the start and end of every patch on the dayside
        if (9 <= MLT_max <= 15) & (9 <= MLT_min <= 15):
            if np.abs(MLAT[PCP[i]]) > np.abs(MLAT[PCP[i+1]]):
                start = PCP[i+1]
                end = PCP[i]
            elif np.abs(MLAT[PCP[i]]) < np.abs(MLAT[PCP[i+1]]):
                start = PCP[i]
                end = PCP[i+1]

        #Setting the start and end of every patch on the nightside
        elif ((21 <= MLT_max <= 24) & (21 <= MLT_min <= 24)) | (( 0 <= MLT_max <= 3) & (0 <= MLT_min <= 3)):
            if np.abs(MLAT[PCP[i]]) < np.abs(MLAT[PCP[i+1]]):
                start = PCP[i+1]
                end = PCP[i]
            elif np.abs(MLAT[PCP[i]]) > np.abs(MLAT[PCP[i+1]]):
                start = PCP[i]
                end = PCP[i+1]
        
        #Range used in interpolating the PCP dataset
        x_range = np.linspace(0, 100, 100001)

        #PCP requirements
        if (np.all((MLAT[start:end] < 0)) == True) & (np.all((Ne[start:end] > 0)) == True) & \
                                                     (MLT_max >= MLT[start] >= MLT_min) & \
                                                     (MLT_min <= MLT[end] <= MLT_max) & \
                                                     ((end - start) > 30) & \
                                                     (np.abs(MLAT[end] - MLAT[start]) > 3) & \
                                                     (np.isnan(MLT[start]) == False) & \
                                                     (np.isnan(MLT[end]) == False) & \
                                                     (np.any((PCP_flag[start:end] == 4))):
            PCP_count += 1

            #Interpolating so that the PCPs have the same length
            y1 = np.interp(x_range, np.linspace(0, 100, len(MLAT[start:end])), Ne[start:end])

            # plt.xlabel('MLAT')
            plt.ylabel('Ne ($10^4 cm^{-3}$)')
            plt.plot(x_range, y1 /1e4, label = f'SWARM {sat}. Patch number: {PCP_count}')

            #Plotting five PCPs on the same plot
            if PCP_count % 5 == 0:
                plt.title(f'Five Polar Cap Patches Northern Hemisphere, SWARM {sat}. \n MLT {MLT_min}-{MLT_max}')
                plt.legend(loc = 'lower center', fontsize = 8)
                plt.savefig(f'C:/Users/krisfau/Desktop/VSCode/FIGURES/SH_SWARM_{sat}_MLT{MLT_max}_{MLT_min}_PCP{PCP_count}.png')
                plt.close()
            

#Magnetic local time used for plotting the PCPs
MLT_max_list = np.array([12, 15, 24, 3])
MLT_min_list = np.array([9, 12, 21, 0])

for sat in sat_list:
    for i in range(len(MLT_max_list)):
        MLT_max = MLT_max_list[i]
        MLT_min = MLT_min_list[i]
        exec(f'PCP_plotter(PCP_index_{sat}, MLT_{sat}, MLT_max, MLT_min, MLAT_{sat}, Ne_{sat}, Timestamp_{sat}, sat, Background_Ne_{sat}, PCP_flag_{sat})')
        plt.close()



