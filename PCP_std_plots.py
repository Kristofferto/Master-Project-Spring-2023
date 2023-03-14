import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from tqdm import tqdm, trange
import sys
from scipy import stats
import glob
# data_list = ['Background_Ne', 'Foreground_Ne', 'Grad_Ne_at_100km', 'Grad_Ne_at_20km', 'Grad_Ne_at_50km', 'Grad_Ne_at_PCP_edge',  'Longitude', 'Ne', 'PCP_flag', 'Radius', 'Timestamp', 'Latitude', 'MLT']
data_list = ['Timestamp', 'MLT']
sat_list = ['A', 'C']
hemisphere_indicator = ['NH', 'SH']

#path mac
path = 'Data/'
# #path hjemme
# path = 'D:/Git_Codes/Data/'

# #path UiO
# path = 'C:/Users/krisfau/Desktop/VSCode/Data/'


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


# NH
# print(Data_fratio_NH_Ne_9_12)
# print(Data_fratio_NH_Fg_9_12)
# print(Data_fratio_NH_Ne_12_15)
# print(Data_fratio_NH_Fg_12_15)
# print(Data_fratio_NH_Ne_21_24)
# print(Data_fratio_NH_Fg_21_24)
# print(Data_fratio_NH_Ne_0_03)
# print(Data_fratio_NH_Fg_0_03)

# SH
# Data_fratio_SH_Ne_9_12
# Data_fratio_SH_Fg_9_12
# Data_fratio_SH_Ne_12_15
# Data_fratio_SH_Fg_12_15
# Data_fratio_SH_Ne_21_24
# Data_fratio_SH_Fg_21_24
# Data_fratio_SH_Ne_0_03
# Data_fratio_SH_Fg_0_03


# plt.title('Histogram')
# plt.hist(Data_fratio_NH_Ne_9_12,  alpha = 0.5, label = '9-12')
# plt.hist(Data_fratio_NH_Ne_12_15,  alpha = 0.5, label = '12-15')
# plt.hist(Data_fratio_NH_Ne_21_24,  alpha = 0.5, label = '21-24')
# plt.hist(Data_fratio_NH_Ne_0_03,  alpha = 0.5, label = '0-03')
# plt.legend()
# plt.show()

# plt.title('Histogram')
# plt.hist([Data_fratio_NH_Ne_9_12, Data_fratio_NH_Ne_12_15, Data_fratio_NH_Ne_21_24, Data_fratio_NH_Ne_0_03],  alpha = 0.5, label = ['9-12', '12-15', '21-24', '0-03'])
# plt.xlim(0,100)
# plt.legend()
# plt.show()

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

# plt.title('Boxplot')
# plt.boxplot([Data_fratio_NH_Ne_9_12, Data_fratio_NH_Ne_12_15, Data_fratio_NH_Ne_21_24, Data_fratio_NH_Ne_0_03][mask], labels = ['9-12', '12-15', '21-24', '0-03'])
# plt.xlabel('Magnetic Local Time [MLT]')
# plt.ylabel('PCP edge ratio [f]')
# plt.show()

# plt.title('Boxplot')
# plt.boxplot([N_9_12, N_12_15, N_21_24, N_0_03], labels = ['9-12', '12-15', '21-24', '0-03'])
# plt.xlabel('Magnetic Local Time [MLT]')
# plt.ylabel('PCP edge ratio [f]')
# plt.ylim(-5,40)
# plt.show()

# plt.title('Boxplot')
# plt.boxplot([S_9_12, S_12_15, S_21_24, S_0_03], labels = ['9-12', '12-15', '21-24', '0-03'])
# plt.xlabel('Magnetic Local Time [MLT]')
# plt.ylabel('PCP edge ratio [f]')
# plt.ylim(-5,100)
# plt.show()

fig, (ax1, ax2) = plt.subplots(1, 2, figsize = (12, 10))
fig.suptitle('Boxplots for the standard deviation ratio between the trailing and leading edge of PCPs. \n Sorted using MLT.')
ax1.boxplot([N_9_12, N_12_15, N_21_24, N_0_03], labels = ['MLT 9-12', 'MLT 12-15', 'MLT 21-24', 'MLT 0-03'])
ax1.set_ylim([-5, 40])
ax2.boxplot([S_9_12, S_12_15, S_21_24, S_0_03], labels = ['MLT 9-12', 'MLT 12-15', 'MLT 21-24', 'MLT 0-03'])
ax2.set_ylim([-5, 100])
ax1.set_title('Nortern Hemisphere')
ax2.set_title('Southern Hemisphere')
ax1.set_ylabel('standard deviation ratio f')
plt.savefig(f'C:/Users/krisfau/Desktop/VSCode/FIGURES/Boxplot.png')
plt.show()
plt.close()


N_index_9_12_A = N_index_9_12[:270]

# print('##########################################################################')

# print(f'Antall PCP Nord: {len(N_9_12)} {len(N_12_15)} {len(N_21_24)} {len(N_0_03)}')
# print('1:', N_index_9_12)
# print('2:', N_index_12_15) 
# print('3:', N_index_21_24) 
# print('4:', N_index_0_03)
# print('##########################################################################')
# print(f'Antall PCP Sør: {len(S_9_12)} {len(S_12_15)} {len(S_21_24)} {len(S_0_03)}')
# print('1:', S_index_9_12)
# print('2:', S_index_12_15) 
# print('3:', S_index_21_24) 
# print('4:', S_index_0_03)
# print('##########################################################################')


def find_index(array):
    index = -1
    for i in range(1, len(array)):
        if array[i] < array[i-1]:
            index = i 
            break 
    return index
print(find_index(N_index_9_12))
print(N_index_9_12[find_index(N_index_9_12)])

fig2, ax = plt.subplots(2, 2, figsize = (12, 10))
fig2.suptitle('Timeseries of the standard deviation ratio calculations \n Swarm A and C, Northern Hemisphere')
for i in range(len(N_9_12)):
    if i <= find_index(N_index_9_12) - 1:
        ax[0,0].scatter(Timestamp_A[N_index_9_12[i]] ,N_9_12[i], color = 'black')
    elif i > find_index(N_index_9_12) - 1:
        ax[0,0].scatter(Timestamp_C[N_index_9_12[i]] ,N_9_12[i], color = 'black')
for i in range(len(N_12_15)):
    if i <= find_index(N_index_12_15) - 1:
        ax[0,1].scatter(Timestamp_A[N_index_12_15[i]] ,N_12_15[i], color = 'black')
    elif i > find_index(N_index_12_15) - 1:
        ax[0,1].scatter(Timestamp_C[N_index_12_15[i]] ,N_12_15[i], color = 'black')
for i in range(len(N_21_24)):
    if i <= find_index(N_index_21_24) - 1:
        ax[1,0].scatter(Timestamp_A[N_index_21_24[i]] ,N_21_24[i], color = 'black')
    elif i > find_index(N_index_21_24) - 1:
        ax[1,0].scatter(Timestamp_C[N_index_21_24[i]] ,N_21_24[i], color = 'black')
for i in range(len(N_0_03)):
    if i <= find_index(N_index_0_03) - 1:
        ax[1,1].scatter(Timestamp_A[N_index_0_03[i]] ,N_0_03[i], color = 'black')
    elif i > find_index(N_index_0_03) - 1:
        ax[1,1].scatter(Timestamp_C[N_index_0_03[i]] ,N_0_03[i], color = 'black')

ax[0,0].set_title('MLT 9-12')
ax[0,1].set_title('MLT 12-15')
ax[1,0].set_title('MLT 21-24')
ax[1,1].set_title('MLT 0-03')

ax[0,0].set_ylabel('Standard deviation ratio f')
ax[1,0].set_ylabel('Standard deviation ratio f')

plt.savefig(f'C:/Users/krisfau/Desktop/VSCode/FIGURES/Timeseries_std_NH_AC.png')
plt.show()
plt.close()


fig3, axs = plt.subplots(2, 2, figsize = (12, 10))
fig3.suptitle('Timeseries of the standard deviation ratio calculations \n Swarm A and C, Southern Hemisphere')
for i in range(len(S_9_12)):
    if i <= find_index(S_index_9_12) - 1:
        axs[0,0].scatter(Timestamp_A[S_index_9_12[i]] ,S_9_12[i], color = 'black')
    elif i > find_index(S_index_9_12) - 1:
        axs[0,0].scatter(Timestamp_C[S_index_9_12[i]] ,S_9_12[i], color = 'black')
for i in range(len(S_12_15)):
    if i <= find_index(S_index_12_15) - 1:
        axs[0,1].scatter(Timestamp_A[S_index_12_15[i]] ,S_12_15[i], color = 'black')
    elif i > find_index(S_index_12_15) - 1:
        axs[0,1].scatter(Timestamp_C[S_index_12_15[i]] ,S_12_15[i], color = 'black')
for i in range(len(S_21_24)):
    if i <= find_index(S_index_21_24) - 1:
        axs[1,0].scatter(Timestamp_A[S_index_21_24[i]] ,S_21_24[i], color = 'black')
    elif i > find_index(S_index_21_24) - 1:
        axs[1,0].scatter(Timestamp_C[S_index_21_24[i]] ,S_21_24[i], color = 'black')
for i in range(len(S_0_03)):
    if i <= find_index(S_index_0_03) - 1:
        axs[1,1].scatter(Timestamp_A[S_index_0_03[i]] ,S_0_03[i], color = 'black')
    elif i > find_index(S_index_0_03) - 1:
        axs[1,1].scatter(Timestamp_C[S_index_0_03[i]] ,S_0_03[i], color = 'black')

axs[0,0].set_title('MLT 9-12')
axs[0,1].set_title('MLT 12-15')
axs[1,0].set_title('MLT 21-24')
axs[1,1].set_title('MLT 0-03')

axs[0,0].set_ylabel('Standard deviation ratio f')
axs[1,0].set_ylabel('Standard deviation ratio f')

plt.savefig(f'C:/Users/krisfau/Desktop/VSCode/FIGURES/Timeseries_std_SH_AC.png')
plt.show()
plt.close()
