import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from tqdm import tqdm, trange
# data_list = ['Background_Ne', 'Foreground_Ne', 'Grad_Ne_at_100km', 'Grad_Ne_at_20km', 'Grad_Ne_at_50km', 'Grad_Ne_at_PCP_edge',  'Longitude', 'Ne', 'PCP_flag', 'Radius', 'Timestamp', 'Latitude', 'MLT']
data_list = ['Longitude', 'Ne', 'PCP_flag', 'Timestamp', 'Latitude', 'MLT']
sat_list = ['A', 'B', 'C']

path = 'C:/Users/krisfau/Desktop/VSCode/Data/'

for sat in tqdm(sat_list, desc = 'Loading satellite data'):
    for name in data_list:
        exec(f'{name}_{sat} = np.load("{path}Data_{sat}_{name}.npy", allow_pickle = True)')


def PCP_plotter(Lat, PCP, MLT, Ne, Time, patchcount):
    Northcount = 0
    Southcount = 0
    for i in trange(PCP_flag_A, desc = 'Finding and plotting PCP'):
        if Lat[i] > 0:
            #northern hemisphere
            
            Northcount += 1

            plt.title('Polar Cap Patches Northern Hemisphere')
            plt.scatter(Time[patch_start:patch_end], Ne[patch_start:patch_end], label = 'Ne', marker = '.')
            plt.legend()
            


        elif Lat[i] < 0:
            #southern hemisphere

            Southcount += 1

            plt.title('Polar Cap Patches Southern Hemisphere')
            plt.scatter(Time[patch_start:patch_end], Ne[patch_start:patch_end], label = 'Ne', marker = '.')
            plt.legend()






change_list = []
count = 0
for i in trange(len(PCP_flag_A)):
    if PCP_flag_A[i] == count:
        continue
    count = PCP_flag_A[i]
    change_list.append(i)

print(len(change_list))


    # plt.scatter(Timestamp_A[], Ne_A[], label = 'Ne', marker = '.')



# plt.show()





# plt.title('Testplot')
# plt.scatter(Timestamp_A[100000:100200] ,Ne_A[100000:100200], label = 'Ne', marker = '.')
# plt.scatter(Timestamp_A[100000:100200] ,PCP_flag_A[100000:100200]*1000, label = 'PCP flag', marker = '.')
# plt.legend()
# plt.show()











# count= 0
# for i in trange(len(PCP_flag_A)):
#     if PCP_flag_A[i] == 4 or PCP_flag_A[i] == 4 or PCP_flag_A[i] == 4:
#         count += 1


# print(count)