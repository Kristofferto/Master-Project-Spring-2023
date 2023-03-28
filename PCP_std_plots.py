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

#Renaming the locally saved arrays for more efficient use later on
#N stands for Northern Hemisphere, S stands for Southern Hemisphere
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
fig2.suptitle('Timeseries of the standard deviation ratio calculations. \n Northern Hemisphere.')
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


plt.savefig(savepath + 'Timeseries_std_NH_AC.png')
# plt.show()
plt.close()



#Plotting the timeseries of the standard deviation ratios calculated for the southern hemisphere
fig3, axs = plt.subplots(2, 2, figsize = (12, 10))
fig3.autofmt_xdate()
fig3.suptitle('Timeseries of the standard deviation ratio calculations. \n Southern Hemisphere.')
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


plt.savefig(savepath + 'Timeseries_std_SH_AC.png')
# plt.show()
plt.close()


#Plotting histograms for the standard deviation ratios for the southern hemisphere
fig4, axs = plt.subplots(2, 2, figsize = (12, 10))
fig4.suptitle('Histogram of the standard deviation ratio calculations. \n Sorted using MLT. \n Southern Hemisphere.')
hist_bins = [0, 2, 10, 20, 30, 40, 50, 60, 70, 80, 90]
axs[0,0].hist(S_9_12, bins = hist_bins, histtype='bar', ec='black')
axs[0,1].hist(S_12_15, bins = hist_bins, histtype='bar', ec='black')
axs[1,0].hist(S_21_24, bins = hist_bins, histtype='bar', ec='black')
axs[1,1].hist(S_0_03, bins = hist_bins, histtype='bar', ec='black')

axs[0,0].set_title('MLT 9-12')
axs[0,1].set_title('MLT 12-15')
axs[1,0].set_title('MLT 21-24')
axs[1,1].set_title('MLT 0-03')

axs[0,0].set_ylabel('Frequency')
axs[1,0].set_ylabel('Frequency')
axs[1,0].set_xlabel('Standard deviation ratio f')
axs[1,1].set_xlabel('Standard deviation ratio f')


plt.savefig(savepath + 'Hist_std_SH_AC.png')
# plt.show()
plt.close()


#Plotting histograms for the standard deviation ratios for the northern hemisphere
fig5, axs = plt.subplots(2, 2, figsize = (12, 10))
fig5.suptitle('Histogram of the standard deviation ratio calculations. \n Sorted using MLT. \n Northern Hemisphere.')
hist_bins = [0, 2, 10, 20, 30, 40, 50, 60, 70, 80, 90]
axs[0,0].hist(N_9_12, bins = hist_bins, histtype='bar', ec='black')
axs[0,1].hist(N_12_15, bins = hist_bins, histtype='bar', ec='black')
axs[1,0].hist(N_21_24, bins = hist_bins, histtype='bar', ec='black')
axs[1,1].hist(N_0_03, bins = hist_bins, histtype='bar', ec='black')

axs[0,0].set_title('MLT 9-12')
axs[0,1].set_title('MLT 12-15')
axs[1,0].set_title('MLT 21-24')
axs[1,1].set_title('MLT 0-03')

axs[0,0].set_ylabel('Frequency')
axs[1,0].set_ylabel('Frequency')
axs[1,0].set_xlabel('Standard deviation ratio f')
axs[1,1].set_xlabel('Standard deviation ratio f')


plt.savefig(savepath + 'Hist_std_NH_AC.png')
# plt.show()

plt.close()

print('Antall ratios nord:', len(N_9_12) + len(N_12_15) + len(N_21_24) + len(N_0_03) + len(N_15_18) + len(N_3_6) + len(N_6_9) + len(N_18_21))
print('Antall ratios sør:', len(S_9_12) + len(S_12_15) + len(S_21_24) + len(S_0_03) + len(S_15_18) + len(S_3_6) + len(S_6_9) + len(S_18_21))




"""
PLOTTING SUMMER AND WINTER SPLIT FOR NORTHERN AND SOUTHERN HEMISPHERE
"""

def boxplots_one_minusone(array_list_NH, array_list_SH, San_array_list_NH, San_array_list_SH):
    for i in range(4):
        array_list_NH[i][array_list_NH[i] < 1] = -1
        array_list_NH[i][(1 <= array_list_NH[i]) & (array_list_NH[i] < 2)] = 0
        array_list_NH[i][2 <=array_list_NH[i]] = 1

        array_list_SH[i][array_list_SH[i] < 1] = -1
        array_list_SH[i][(1 <= array_list_SH[i]) & (array_list_SH[i] < 2)] = 0
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

    plt.savefig(savepath + 'Boxplotoneminusone.png')
    # plt.show()
    plt.close()

    # Boxplot for sanity checks
    for i in range(4):
        San_array_list_NH[i][San_array_list_NH[i] < 1] = -1
        San_array_list_NH[i][(1 <= San_array_list_NH[i]) & (San_array_list_NH[i] < 2)] = 0
        San_array_list_NH[i][2 <=San_array_list_NH[i]] = 1

        San_array_list_SH[i][San_array_list_SH[i] < 1] = -1
        San_array_list_SH[i][(1 <= San_array_list_SH[i]) & (San_array_list_SH[i] < 2)] = 0
        San_array_list_SH[i][2 <=San_array_list_SH[i]] = 1

        
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize = (12, 10))
    fig.suptitle('Boxplots for the standard deviation ratio between the trailing and leading edge of PCPs. \n Sorted using MLT.')
    ax1.boxplot([San_array_list_NH[0], San_array_list_NH[1], San_array_list_NH[2], San_array_list_NH[3]], labels = ['MLT 6-9', 'MLT 15-18', 'MLT 18-21', 'MLT 3-6'])
    ax1.set_ylim([-2, 2])
    ax2.boxplot([San_array_list_SH[0], San_array_list_SH[1], San_array_list_SH[2], San_array_list_SH[3]], labels = ['MLT 6-9', 'MLT 15-18', 'MLT 18-21', 'MLT 3-6'])
    ax2.set_ylim([-2, 2])
    ax1.set_title('Nortern Hemisphere')
    ax2.set_title('Southern Hemisphere')
    ax1.set_ylabel('Standard deviation ratio f')

    plt.savefig(savepath + 'Sanity_Boxplotoneminusone.png')
    # plt.show()
    plt.close()
    





ratio_list_NH_summer_9_12 = []
ratio_list_NH_summer_12_15 = []
ratio_list_NH_summer_21_24 = []
ratio_list_NH_summer_0_03 = []
ratio_list_NH_summer_3_6 = []
ratio_list_NH_summer_6_9 = []
ratio_list_NH_summer_15_18 = []
ratio_list_NH_summer_18_21 = []

ratio_list_NH_winter_9_12 = []
ratio_list_NH_winter_12_15 = []
ratio_list_NH_winter_21_24 = []
ratio_list_NH_winter_0_03 = []
ratio_list_NH_winter_3_6 = []
ratio_list_NH_winter_6_9 = []
ratio_list_NH_winter_15_18 = []
ratio_list_NH_winter_18_21 = []

ratio_list_SH_summer_9_12 = []
ratio_list_SH_summer_12_15 = []
ratio_list_SH_summer_21_24 = []
ratio_list_SH_summer_0_03 = []
ratio_list_SH_summer_3_6 = []
ratio_list_SH_summer_6_9 = []
ratio_list_SH_summer_15_18 = []
ratio_list_SH_summer_18_21 = []

ratio_list_SH_winter_9_12 = []
ratio_list_SH_winter_12_15 = []
ratio_list_SH_winter_21_24 = []
ratio_list_SH_winter_0_03 = []
ratio_list_SH_winter_3_6 = []
ratio_list_SH_winter_6_9 = []
ratio_list_SH_winter_15_18 = []
ratio_list_SH_winter_18_21 = []

print('Totalt antall sommer før:', (len(N_index_9_12) + len(N_index_12_15) + len(N_index_21_24) + len(N_index_0_03) + \
                                    len(N_index_15_18) + len(N_index_6_9) + len(N_index_18_21) + len(N_index_3_6)) / 2)

print('Totalt antall vinter før:', (len(S_index_9_12) + len(S_index_12_15) + len(S_index_21_24) + len(S_index_0_03) + \
                                    len(S_index_15_18) + len(S_index_6_9) + len(S_index_18_21) + len(S_index_3_6)) / 2)

start_summer = datetime.datetime(2000, 4, 1)
end_summer = datetime.datetime(2000, 10, 1)

def seasonal_index_fratio_split(index_list,ratio_list, append_list_summer, append_list_winter, hemisphere):
    patches_lost = 0
    for i in range(0, len(index_list), 2):
        
        if i <= find_index(index_list) - 1: #Timestamp data for Sat A
            if start_summer.month < Timestamp_A[index_list[i]].month < end_summer.month and \
                start_summer.month < Timestamp_A[index_list[i+1]].month < end_summer.month:
                if hemisphere == 'NH':
                    append_list_summer.append(ratio_list[int(i / 2)])
                    # append_list_summer.append(ratio_list[i+1])
                elif hemisphere == 'SH':
                    append_list_winter.append(ratio_list[int(i / 2)])
                    # append_list_winter.append(ratio_list[i+1])

            elif (end_summer.month <= Timestamp_A[index_list[i]].month <= 12 or \
                1 <= Timestamp_A[index_list[i]].month <= start_summer.month) and \
                    (end_summer.month <= Timestamp_A[index_list[i+1]].month <= 12 or \
                1 <= Timestamp_A[index_list[i+1]].month <= start_summer.month):
                if hemisphere == 'NH':
                    append_list_winter.append(ratio_list[int(i / 2)])
                    # append_list_winter.append(ratio_list[i+1])
                elif hemisphere == 'SH':
                    append_list_summer.append(ratio_list[int(i / 2)])
                    # append_list_summer.append(ratio_list[i+1])
            else:
                patches_lost +=1

                    
        elif i > find_index(index_list) - 1: #Timestamp data for Sat C
            if start_summer.month < Timestamp_C[index_list[i]].month < end_summer.month and \
                start_summer.month < Timestamp_C[index_list[i+1]].month < end_summer.month:
                if hemisphere == 'NH':
                    append_list_summer.append(ratio_list[int(i / 2)])
                    # append_list_summer.append(ratio_list[i+1])
                elif hemisphere == 'SH':
                    append_list_winter.append(ratio_list[int(i / 2)])
                    # append_list_winter.append(ratio_list[i+1])

            elif (end_summer.month <= Timestamp_C[index_list[i]].month <= 12 or \
                1 <= Timestamp_C[index_list[i]].month <= start_summer.month) and \
                    (end_summer.month <= Timestamp_C[index_list[i+1]].month <= 12 or \
                1 <= Timestamp_C[index_list[i+1]].month <= start_summer.month):
                if hemisphere == 'NH':
                    append_list_winter.append(ratio_list[int(i / 2)])
                    # append_list_winter.append(ratio_list[i+1])
                elif hemisphere == 'SH':
                    append_list_summer.append(ratio_list[int(i / 2)])
                    # append_list_summer.append(ratio_list[i+1])
            else:
                patches_lost +=1

    append_list_summer_ = np.array(append_list_summer)
    append_list_winter_ = np.array(append_list_winter)
    return patches_lost, append_list_summer_, append_list_winter_

patches_lost1, ratio_array_NH_summer_9_12, ratio_array_NH_winter_9_12 = seasonal_index_fratio_split(N_index_9_12, N_9_12, ratio_list_NH_summer_9_12, ratio_list_NH_winter_9_12, 'NH')
patches_lost2, ratio_array_NH_summer_12_15, ratio_array_NH_winter_12_15 = seasonal_index_fratio_split(N_index_12_15, N_12_15, ratio_list_NH_summer_12_15, ratio_list_NH_winter_12_15, 'NH')
patches_lost3, ratio_array_NH_summer_21_24, ratio_array_NH_winter_21_24 = seasonal_index_fratio_split(N_index_21_24, N_21_24, ratio_list_NH_summer_21_24, ratio_list_NH_winter_21_24, 'NH')
patches_lost4, ratio_array_NH_summer_0_03, ratio_array_NH_winter_0_03 = seasonal_index_fratio_split(N_index_0_03, N_0_03, ratio_list_NH_summer_0_03, ratio_list_NH_winter_0_03, 'NH')

patches_lost5, ratio_array_NH_summer_3_6, ratio_array_NH_winter_3_6 = seasonal_index_fratio_split(N_index_3_6, N_3_6, ratio_list_NH_summer_3_6, ratio_list_NH_winter_3_6, 'NH')
patches_lost6, ratio_array_NH_summer_6_9, ratio_array_NH_winter_6_9 = seasonal_index_fratio_split(N_index_6_9, N_6_9, ratio_list_NH_summer_6_9, ratio_list_NH_winter_6_9, 'NH')
patches_lost7, ratio_array_NH_summer_15_18, ratio_array_NH_winter_15_18 = seasonal_index_fratio_split(N_index_15_18, N_15_18, ratio_list_NH_summer_15_18, ratio_list_NH_winter_15_18, 'NH')
patches_lost8, ratio_array_NH_summer_18_21, ratio_array_NH_winter_18_21 = seasonal_index_fratio_split(N_index_18_21, N_18_21, ratio_list_NH_summer_18_21, ratio_list_NH_winter_18_21, 'NH')


patches_lost9, ratio_array_SH_summer_9_12, ratio_array_SH_winter_9_12 = seasonal_index_fratio_split(S_index_9_12, S_9_12, ratio_list_SH_summer_9_12, ratio_list_SH_winter_9_12, 'SH')
patches_lost10, ratio_array_SH_summer_12_15, ratio_array_SH_winter_12_15 = seasonal_index_fratio_split(S_index_12_15, S_12_15, ratio_list_SH_summer_12_15, ratio_list_SH_winter_12_15, 'SH')
patches_lost11, ratio_array_SH_summer_21_24, ratio_array_SH_winter_21_24 = seasonal_index_fratio_split(S_index_21_24, S_21_24, ratio_list_SH_summer_21_24, ratio_list_SH_winter_21_24, 'SH')
patches_lost12, ratio_array_SH_summer_0_03, ratio_array_SH_winter_0_03 = seasonal_index_fratio_split(S_index_0_03, S_0_03, ratio_list_SH_summer_0_03, ratio_list_SH_winter_0_03, 'SH')

patches_lost13, ratio_array_SH_summer_3_6, ratio_array_SH_winter_3_6 = seasonal_index_fratio_split(S_index_3_6, S_3_6, ratio_list_SH_summer_3_6, ratio_list_SH_winter_3_6, 'SH')
patches_lost14, ratio_array_SH_summer_6_9, ratio_array_SH_winter_6_9 = seasonal_index_fratio_split(S_index_6_9, S_6_9, ratio_list_SH_summer_6_9, ratio_list_SH_winter_6_9, 'SH')
patches_lost15, ratio_array_SH_summer_15_18, ratio_array_SH_winter_15_18 = seasonal_index_fratio_split(S_index_15_18, S_15_18, ratio_list_SH_summer_15_18, ratio_list_SH_winter_15_18, 'SH')
patches_lost16, ratio_array_SH_summer_18_21, ratio_array_SH_winter_18_21 = seasonal_index_fratio_split(S_index_18_21, S_18_21, ratio_list_SH_summer_18_21, ratio_list_SH_winter_18_21, 'SH')

# print('Totalt antall sommer etter:', len(ratio_list_summer_9_12) + len(ratio_list_summer_12_15) + len(ratio_list_summer_21_24) + len(ratio_list_summer_0_03))
# print('Totalt antall vinter etter:', len(ratio_list_winter_9_12) + len(ratio_list_winter_12_15) + len(ratio_list_winter_21_24) + len(ratio_list_winter_0_03))
print(patches_lost1)
print(patches_lost2)
print(patches_lost3)
print(patches_lost4)
print(patches_lost5)
print(patches_lost6)
print(patches_lost7)
print(patches_lost8)
print(patches_lost9)
print(patches_lost10)
print(patches_lost11)
print(patches_lost12)
print(patches_lost13)
print(patches_lost14)
print(patches_lost15)
print(patches_lost16)


print('Total amount of patches:', len(ratio_list_NH_summer_9_12) +  len(ratio_list_NH_winter_9_12) + \
                                  len(ratio_list_NH_summer_12_15) + len(ratio_list_NH_winter_12_15) + \
                                  len(ratio_list_NH_summer_21_24) + len(ratio_list_NH_winter_21_24) + \
                                  len(ratio_list_NH_summer_0_03) +  len(ratio_list_NH_winter_0_03) + \
                                  len(ratio_list_NH_summer_3_6) +   len(ratio_list_NH_winter_3_6) + \
                                  len(ratio_list_NH_summer_6_9) +   len(ratio_list_NH_winter_6_9) + \
                                  len(ratio_list_NH_summer_15_18) + len(ratio_list_NH_winter_15_18) + \
                                  len(ratio_list_NH_summer_18_21) + len(ratio_list_NH_winter_18_21) + \
                                  len(ratio_list_SH_summer_9_12) +  len(ratio_list_SH_winter_9_12) + \
                                  len(ratio_list_SH_summer_12_15) + len(ratio_list_SH_winter_12_15) + \
                                  len(ratio_list_SH_summer_21_24) + len(ratio_list_SH_winter_21_24) + \
                                  len(ratio_list_SH_summer_0_03) +  len(ratio_list_SH_winter_0_03) + \
                                  len(ratio_list_SH_summer_3_6) +   len(ratio_list_SH_winter_3_6) + \
                                  len(ratio_list_SH_summer_6_9) +   len(ratio_list_SH_winter_6_9) + \
                                  len(ratio_list_SH_summer_15_18) + len(ratio_list_SH_winter_15_18) + \
                                  len(ratio_list_SH_summer_18_21) + len(ratio_list_SH_winter_18_21))

def seasonal_variation_plots(Hemisphere, array_list_winter, array_list_summer):
    #Seasonal histogram plot
    #Winter
    fig6, axs = plt.subplots(2, 2, figsize = (12, 10))
    hist_bins = [0, 2, 10, 20, 30, 40, 50, 60, 70, 80, 90]
    axs[0,0].hist(array_list_winter[0], bins = hist_bins, histtype='bar', ec='black')
    axs[0,1].hist(array_list_winter[1], bins = hist_bins, histtype='bar', ec='black')
    axs[1,0].hist(array_list_winter[2], bins = hist_bins, histtype='bar', ec='black')
    axs[1,1].hist(array_list_winter[3], bins = hist_bins, histtype='bar', ec='black')

    axs[0,0].set_title('MLT 9-12')
    axs[0,1].set_title('MLT 12-15')
    axs[1,0].set_title('MLT 21-24')
    axs[1,1].set_title('MLT 0-3')

    axs[0,0].set_ylabel('Frequency')
    axs[1,0].set_ylabel('Frequency')
    axs[1,0].set_xlabel('Standard deviation ratio f')
    axs[1,1].set_xlabel('Standard deviation ratio f')

    if Hemisphere == 'NH':
        fig6.suptitle('Histogram of the standard deviation ratio calculations during winter. \n Northern Hemisphere.')
       
        plt.savefig(savepath + 'Seasonal_variation_Hist_std_NH_winter_AC.png')
    elif Hemisphere == 'SH':
        fig6.suptitle('Histogram of the standard deviation ratio calculations during winter. \n Southern Hemisphere.')
        
        plt.savefig(savepath + 'Seasonal_variation_Hist_std_SH_winter_AC.png')


    # plt.show()
    plt.close()

    
    #Summer
    fig6, axs = plt.subplots(2, 2, figsize = (12, 10))
    hist_bins = [0, 2, 10, 20, 30, 40, 50, 60, 70, 80, 90]
    axs[0,0].hist(array_list_summer[0], bins = hist_bins, histtype='bar', ec='black')
    axs[0,1].hist(array_list_summer[1], bins = hist_bins, histtype='bar', ec='black')
    axs[1,0].hist(array_list_summer[2], bins = hist_bins, histtype='bar', ec='black')
    axs[1,1].hist(array_list_summer[3], bins = hist_bins, histtype='bar', ec='black')

    axs[0,0].set_title('MLT 9-12')
    axs[0,1].set_title('MLT 12-15')
    axs[1,0].set_title('MLT 21-24')
    axs[1,1].set_title('MLT 0-3')

    axs[0,0].set_ylabel('Frequency')
    axs[1,0].set_ylabel('Frequency')
    axs[1,0].set_xlabel('Standard deviation ratio f')
    axs[1,1].set_xlabel('Standard deviation ratio f')

    if Hemisphere == 'NH':
        fig6.suptitle('Histogram of the standard deviation ratio calculations during summer. \n Northern Hemisphere.')
        
        plt.savefig(savepath + 'Seasonal_variation_Hist_std_NH_summer_AC.png')
    elif Hemisphere == 'SH':
        fig6.suptitle('Histogram of the standard deviation ratio calculations during summer. \n Southern Hemisphere.')
        
        plt.savefig(savepath + 'Seasonal_variation_Hist_std_SH_summer_AC.png')

    # plt.show()
    plt.close()

    for i in range(4):
        array_list_winter[i][array_list_winter[i] < 1] = -1
        array_list_winter[i][(1 <= array_list_winter[i]) & (array_list_winter[i] < 2)] = 0
        array_list_winter[i][2 <=array_list_winter[i]] = 1

        array_list_summer[i][array_list_summer[i] < 1] = -1
        array_list_summer[i][(1 <= array_list_summer[i]) & (array_list_summer[i] < 2)] = 0
        array_list_summer[i][2 <=array_list_summer[i]] = 1
    #Seasonal boxplot
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize = (12, 10))
    ax1.boxplot([array_list_winter[0], array_list_winter[1], array_list_winter[2], array_list_winter[3]], labels = ['MLT 9-12', 'MLT 12-15', 'MLT 21-24', 'MLT 0-03'])
    ax1.set_ylim([-2, 2])
    ax2.boxplot([array_list_summer[0], array_list_summer[1], array_list_summer[2], array_list_summer[3]], labels = ['MLT 9-12', 'MLT 12-15', 'MLT 21-24', 'MLT 0-03'])
    ax2.set_ylim([-2, 2])

    ax1.set_title('Local Winter')
    ax2.set_title('Local Summer')
    ax1.set_ylabel('Standard deviation ratio f')
    if Hemisphere == 'NH':
        fig.suptitle('Boxplots for the standard deviation ratio between the trailing and leading edge of PCPs. \n Sorted using MLT. \n Northern Hemisphere.')
        
        plt.savefig(savepath + 'Seaesonal_variation__NH_boxplot.png')
    elif Hemisphere == 'SH':
        fig.suptitle('Boxplots for the standard deviation ratio between the trailing and leading edge of PCPs. \n Sorted using MLT. \n Southern Hemisphere.')
        
        plt.savefig(savepath + 'Seaesonal_variation__SH_boxplot.png')
   
    # plt.show()
    plt.close()


    
seasonal_variation_plots('NH', [ratio_array_NH_winter_9_12, ratio_array_NH_winter_12_15, ratio_array_NH_winter_21_24, ratio_array_NH_winter_0_03], [ratio_array_NH_summer_9_12, ratio_array_NH_summer_12_15, ratio_array_NH_summer_21_24, ratio_array_NH_summer_0_03])
seasonal_variation_plots('SH', [ratio_array_SH_winter_9_12, ratio_array_SH_winter_12_15, ratio_array_SH_winter_21_24, ratio_array_SH_winter_0_03], [ratio_array_SH_summer_9_12, ratio_array_SH_summer_12_15, ratio_array_SH_summer_21_24, ratio_array_SH_summer_0_03])

def sanity_seasonal_variation_plots(Hemisphere, array_list_winter, array_list_summer):
    #Seasonal histogram plot for sanity check
    #Winter
    fig6, axs = plt.subplots(2, 2, figsize = (12, 10))
    hist_bins = [0, 2, 10, 20, 30, 40, 50, 60, 70, 80, 90]
    axs[0,0].hist(array_list_winter[0], bins = hist_bins, histtype='bar', ec='black')
    axs[0,1].hist(array_list_winter[1], bins = hist_bins, histtype='bar', ec='black')
    axs[1,0].hist(array_list_winter[2], bins = hist_bins, histtype='bar', ec='black')
    axs[1,1].hist(array_list_winter[3], bins = hist_bins, histtype='bar', ec='black')

    axs[0,0].set_title('MLT 6-9')
    axs[0,1].set_title('MLT 15-18')
    axs[1,0].set_title('MLT 18-21')
    axs[1,1].set_title('MLT 3-6')

    axs[0,0].set_ylabel('Frequency')
    axs[1,0].set_ylabel('Frequency')
    axs[1,0].set_xlabel('Standard deviation ratio f')
    axs[1,1].set_xlabel('Standard deviation ratio f')

    if Hemisphere == 'NH':
        fig6.suptitle('Sanity Test. \n Histogram of the standard deviation ratio calculations during winter. \n Northern Hemisphere.')
        
        plt.savefig(savepath + 'Sanity_Seasonal_variation_Hist_std_NH_winter_AC.png')
    elif Hemisphere == 'SH':
        fig6.suptitle('Sanity Test. \n Histogram of the standard deviation ratio calculations during winter. \n Southern Hemisphere.')
        
        plt.savefig(savepath + 'Sanity_Seasonal_variation_Hist_std_SH_winter_AC.png')


    # plt.show()
    plt.close()

    
    #Summer
    fig6, axs = plt.subplots(2, 2, figsize = (12, 10))
    hist_bins = [0, 2, 10, 20, 30, 40, 50, 60, 70, 80, 90]
    axs[0,0].hist(array_list_summer[0], bins = hist_bins, histtype='bar', ec='black')
    axs[0,1].hist(array_list_summer[1], bins = hist_bins, histtype='bar', ec='black')
    axs[1,0].hist(array_list_summer[2], bins = hist_bins, histtype='bar', ec='black')
    axs[1,1].hist(array_list_summer[3], bins = hist_bins, histtype='bar', ec='black')

    axs[0,0].set_title('MLT 6-9')
    axs[0,1].set_title('MLT 15-18')
    axs[1,0].set_title('MLT 18-21')
    axs[1,1].set_title('MLT 3-6')

    axs[0,0].set_ylabel('Frequency')
    axs[1,0].set_ylabel('Frequency')
    axs[1,0].set_xlabel('Standard deviation ratio f')
    axs[1,1].set_xlabel('Standard deviation ratio f')

    if Hemisphere == 'NH':
        fig6.suptitle('Sanity Test. \n Histogram of the standard deviation ratio calculations during summer. \n Northern Hemisphere.')
        
        plt.savefig(savepath + 'Sanity_Seasonal_variation_Hist_std_NH_summer_AC.png')
    elif Hemisphere == 'SH':
        fig6.suptitle('Sanity Test. \n Histogram of the standard deviation ratio calculations during summer. \n Southern Hemisphere.')
       
        plt.savefig(savepath + 'Sanity_Seasonal_variation_Hist_std_SH_summer_AC.png')

    # plt.show()
    plt.close()

    for i in range(4):
        array_list_winter[i][array_list_winter[i] < 1] = -1
        array_list_winter[i][(1 <= array_list_winter[i]) & (array_list_winter[i] < 2)] = 0
        array_list_winter[i][2 <=array_list_winter[i]] = 1

        array_list_summer[i][array_list_summer[i] < 1] = -1
        array_list_summer[i][(1 <= array_list_summer[i]) & (array_list_summer[i] < 2)] = 0
        array_list_summer[i][2 <=array_list_summer[i]] = 1
    #Seasonal boxplot
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize = (12, 10))
    ax1.boxplot([array_list_winter[0], array_list_winter[1], array_list_winter[2], array_list_winter[3]], labels = ['MLT 6-9', 'MLT 15-18', 'MLT 18-21', 'MLT 3-6'])
    ax1.set_ylim([-2, 2])
    ax2.boxplot([array_list_summer[0], array_list_summer[1], array_list_summer[2], array_list_summer[3]], labels = ['MLT 6-9', 'MLT 15-18', 'MLT 18-21', 'MLT 3-6'])
    ax2.set_ylim([-2, 2])

    ax1.set_title('Local Winter')
    ax2.set_title('Local Summer')
    ax1.set_ylabel('Standard deviation ratio f')
    if Hemisphere == 'NH':
        fig.suptitle('Sanity Test. \n Boxplots for the standard deviation ratio between the trailing and leading edge of PCPs. \n Sorted using MLT. \n Northern Hemisphere.')
        
        plt.savefig(savepath + 'Sanity_Seaesonal_variation_NH_boxplot.png')
    elif Hemisphere == 'SH':
        fig.suptitle('Sanity Test. \n Boxplots for the standard deviation ratio between the trailing and leading edge of PCPs. \n Sorted using MLT. \n Southern Hemisphere.')

        plt.savefig(savepath + 'Sanity_Seaesonal_variation_SH_boxplot.png')
    # plt.show()
    plt.close()




sanity_seasonal_variation_plots('NH', [ratio_array_NH_winter_6_9, ratio_array_NH_winter_15_18, ratio_array_NH_winter_18_21, ratio_array_NH_winter_3_6], [ratio_array_NH_summer_6_9, ratio_array_NH_summer_15_18, ratio_array_NH_summer_18_21, ratio_array_NH_summer_3_6])
sanity_seasonal_variation_plots('SH', [ratio_array_SH_winter_6_9, ratio_array_SH_winter_15_18, ratio_array_SH_winter_18_21, ratio_array_SH_winter_3_6], [ratio_array_SH_summer_6_9, ratio_array_SH_summer_15_18, ratio_array_SH_summer_18_21, ratio_array_SH_summer_3_6])


boxplots_one_minusone([N_9_12, N_12_15, N_21_24, N_0_03], [S_9_12, S_12_15, S_21_24, S_0_03], [N_6_9, N_15_18, N_18_21, N_3_6], [S_6_9, S_15_18, S_18_21, S_3_6])



# import pandas as pd

def PCP_climatology(index_array):
    max_date = datetime.datetime = (2020, 1, 1)

    #Satellite A
    for i in range(len(Timestamp_A)):
        while (Timestamp_A[i] < max_date) == True:
            for k in range(0, len(index_array), 2):
                print(k)
#     #Satellite C

    

#         # plot andres timeseries of polar cap patches for winter and summer.