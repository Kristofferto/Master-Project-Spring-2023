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
# path = 'Data/'
# #path hjemme
path = 'D:/Git_Codes/Data/'
savepath = 'D:/Git_Codes/Figures/'

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




#Creating boxplots for the standard deviation ratio for the northern and southern hemisphere.
fig, (ax1, ax2) = plt.subplots(1, 2, figsize = (12, 10))
fig.suptitle('Boxplots for the standard deviation ratio between the trailing and leading edge of PCPs. \n Sorted using MLT.')
ax1.boxplot([N_9_12, N_12_15, N_21_24, N_0_03], labels = ['MLT 9-12', 'MLT 12-15', 'MLT 21-24', 'MLT 0-03'])
ax1.set_ylim([-5, 40])
ax2.boxplot([S_9_12, S_12_15, S_21_24, S_0_03], labels = ['MLT 9-12', 'MLT 12-15', 'MLT 21-24', 'MLT 0-03'])
ax2.set_ylim([-5, 100])
ax1.set_title('Nortern Hemisphere')
ax2.set_title('Southern Hemisphere')
ax1.set_ylabel('Standard deviation ratio f')
# plt.savefig(f'C:/Users/krisfau/Desktop/VSCode/FIGURES/Boxplot.png')
plt.savefig(savepath + 'Boxplot.png')
# plt.show()
plt.close()



#Function to find where the indices starts to indicate data for satellite C and not A 
# - this is used to indicate where the timestamp data needs to be changed
def find_index(array):
    index = -1
    for i in range(1, len(array)):
        if array[i] < array[i-1]:
            index = i 
            break 
    return index

#Plotting the timeseries of the standard deviation ratios calculated for the northern hemisphere
fig2, ax = plt.subplots(2, 2, figsize = (12, 10))
fig2.autofmt_xdate()
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
#Setting labels and titles
ax[0,0].set_title('MLT 9-12')
ax[0,1].set_title('MLT 12-15')
ax[1,0].set_title('MLT 21-24')
ax[1,1].set_title('MLT 0-03')
ax[0,0].set_ylabel('Standard deviation ratio f')
ax[1,0].set_ylabel('Standard deviation ratio f')

# plt.savefig(f'C:/Users/krisfau/Desktop/VSCode/FIGURES/Timeseries_std_NH_AC.png')
plt.savefig(savepath + 'Timeseries_std_NH_AC.png')
# plt.show()
plt.close()

#Plotting the timeseries of the standard deviation ratios calculated for the southern hemisphere
fig3, axs = plt.subplots(2, 2, figsize = (12, 10))
fig3.autofmt_xdate()
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

# plt.savefig(f'C:/Users/krisfau/Desktop/VSCode/FIGURES/Timeseries_std_SH_AC.png')
plt.savefig(savepath + 'Timeseries_std_SH_AC.png')
# plt.show()
plt.close()


#Plotting histograms for the standard deviation ratios for the southern hemisphere
fig4, axs = plt.subplots(2, 2, figsize = (12, 10))
fig4.suptitle('Histogram of the standard deviation ratio calculations \n Swarm A and C, Southern Hemisphere')
hist_bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
axs[0,0].hist(S_9_12, bins = hist_bins)
axs[0,1].hist(S_12_15, bins = hist_bins)
axs[1,0].hist(S_21_24, bins = hist_bins)
axs[1,1].hist(S_0_03, bins = hist_bins)

axs[0,0].set_title('MLT 9-12')
axs[0,1].set_title('MLT 12-15')
axs[1,0].set_title('MLT 21-24')
axs[1,1].set_title('MLT 0-03')

axs[0,0].set_ylabel('Frequency')
axs[1,0].set_ylabel('Frequency')
axs[1,0].set_xlabel('Standard deviation ratio f')
axs[1,1].set_xlabel('Standard deviation ratio f')

# plt.savefig(f'C:/Users/krisfau/Desktop/VSCode/FIGURES/Hist_std_SH_AC.png')
plt.savefig(savepath + 'Hist_std_SH_AC.png')
# plt.show()
plt.close()


#Plotting histograms for the standard deviation ratios for the northern hemisphere
fig5, axs = plt.subplots(2, 2, figsize = (12, 10))
fig5.suptitle('Histogram of the standard deviation ratio calculations \n Swarm A and C, Northern Hemisphere')
hist_bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
axs[0,0].hist(N_9_12, bins = hist_bins)
axs[0,1].hist(N_12_15, bins = hist_bins)
axs[1,0].hist(N_21_24, bins = hist_bins)
axs[1,1].hist(N_0_03, bins = hist_bins)

axs[0,0].set_title('MLT 9-12')
axs[0,1].set_title('MLT 12-15')
axs[1,0].set_title('MLT 21-24')
axs[1,1].set_title('MLT 0-03')

axs[0,0].set_ylabel('Frequency')
axs[1,0].set_ylabel('Frequency')
axs[1,0].set_xlabel('Standard deviation ratio f')
axs[1,1].set_xlabel('Standard deviation ratio f')

# plt.savefig(f'C:/Users/krisfau/Desktop/VSCode/FIGURES/Hist_std_NH_AC.png')
plt.savefig(savepath + 'Hist_std_NH_AC.png')
# plt.show()

plt.close()

print('Antall ratios nord:', len(N_9_12) + len(N_12_15) + len(N_21_24) + len(N_0_03))
print('Antall ratios sør:', len(S_9_12) + len(S_12_15) + len(S_21_24) + len(S_0_03))




"""
PLOTTING SUMMER AND WINTER SPLIT FOR NORTHERN AND SOUTHERN HEMISPHERE
"""

def boxplots_one_minusone(array_list_NH, array_list_SH):
    for i in range(4):
        array_list_NH[i][array_list_NH[i] < 0.5] = -1
        array_list_NH[i][(0.5 <= array_list_NH[i]) & (array_list_NH[i] < 2)] = 0
        array_list_NH[i][2 <=array_list_NH[i]] = 1

        array_list_SH[i][array_list_SH[i] < 0.5] = -1
        array_list_SH[i][(0.5 <= array_list_SH[i]) & (array_list_SH[i] < 2)] = 0
        array_list_SH[i][2 <=array_list_SH[i]] = 1

        
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize = (12, 10))
    fig.suptitle('Boxplots for the standard deviation ratio between the trailing and leading edge of PCPs. \n Sorted using MLT.')
    ax1.boxplot([array_list_NH[0], array_list_NH[1], array_list_NH[2], array_list_NH[3]], labels = ['MLT 9-12', 'MLT 12-15', 'MLT 21-24', 'MLT 0-03'])
    ax1.set_ylim([-2, 2])
    ax2.boxplot([array_list_SH[0], array_list_SH[1], array_list_SH[2], array_list_SH[3]], labels = ['MLT 9-12', 'MLT 12-15', 'MLT 21-24', 'MLT 0-03'])
    ax2.set_ylim([-2, 2])
    ax1.set_title('Nortern Hemisphere')
    ax2.set_title('Southern Hemisphere')
    ax1.set_ylabel('Standard deviation ratio f')
    # plt.savefig('C:/Users/krisfau/Desktop/VSCode/FIGURES/Boxplot.png')
    plt.savefig(savepath + 'Boxplotoneminusone.png')
    # plt.show()
    plt.close()

boxplots_one_minusone([N_9_12, N_12_15, N_21_24, N_0_03], [S_9_12, S_12_15, S_21_24, S_0_03])
