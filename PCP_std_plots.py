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
# path = 'D:\\Git_Codes\\Data\\'

# #path UiO
path = 'C:/Users/krisfau/Desktop/VSCode/Data/'


for sat in tqdm(sat_list, desc = 'Loading locally stored data'):
    for name in data_list:
        exec(f'{name}_{sat} = np.load("{path}Data_{sat}_{name}.npy", allow_pickle = True)')

for indicator in hemisphere_indicator:
    exec(f'Data_fratio_{indicator}_Ne_9_12 = np.load("{path}Data_fratio_{indicator}_Ne_9_12.npy", allow_pickle = True)')
    exec(f'Data_fratio_{indicator}_Fg_9_12 = np.load("{path}Data_fratio_{indicator}_Fg_9_12.npy", allow_pickle = True)')

    exec(f'Data_fratio_{indicator}_Ne_12_15 = np.load("{path}Data_fratio_{indicator}_Ne_12_15.npy", allow_pickle = True)')
    exec(f'Data_fratio_{indicator}_Fg_12_15 = np.load("{path}Data_fratio_{indicator}_Fg_12_15.npy", allow_pickle = True)')

    exec(f'Data_fratio_{indicator}_Ne_21_24 = np.load("{path}Data_fratio_{indicator}_Ne_21_24.npy", allow_pickle = True)')
    exec(f'Data_fratio_{indicator}_Fg_21_24 = np.load("{path}Data_fratio_{indicator}_Fg_21_24.npy", allow_pickle = True)')

    exec(f'Data_fratio_{indicator}_Ne_0_03 = np.load("{path}Data_fratio_{indicator}_Ne_0_03.npy", allow_pickle = True)')
    exec(f'Data_fratio_{indicator}_Fg_0_03 = np.load("{path}Data_fratio_{indicator}_Fg_0_03.npy", allow_pickle = True)')


# NH
print(Data_fratio_NH_Ne_9_12)
print(Data_fratio_NH_Fg_9_12)
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

print(max(Data_fratio_NH_Ne_0_03))


# plt.hist(Data_fratio_NH_Ne_9_12,  alpha = 0.5, label = '9-12')
# plt.hist(Data_fratio_NH_Ne_12_15,  alpha = 0.5, label = '12-15')
# plt.hist(Data_fratio_NH_Ne_21_24,  alpha = 0.5, label = '21-24')
# plt.hist(Data_fratio_NH_Ne_0_03,  alpha = 0.5, label = '0-03')
# plt.legend()
# plt.show()
plt.title('Histogram')
plt.hist([Data_fratio_NH_Ne_9_12, Data_fratio_NH_Ne_12_15, Data_fratio_NH_Ne_21_24, Data_fratio_NH_Ne_0_03],  alpha = 0.5, label = ['9-12', '12-15', '21-24', '0-03'])
plt.legend()
plt.show()

mask1 = Data_fratio_NH_Ne_9_12 <= 10
arr1 = Data_fratio_NH_Ne_9_12[mask1]

mask2 = Data_fratio_NH_Ne_12_15 <= 10
arr2 = Data_fratio_NH_Ne_12_15[mask2]

mask3 = Data_fratio_NH_Ne_21_24 <= 10
arr3 = Data_fratio_NH_Ne_21_24[mask3]

mask4 = Data_fratio_NH_Ne_0_03 <= 10
arr4 = Data_fratio_NH_Ne_0_03[mask4]

# plt.title('Boxplot')
# plt.boxplot([Data_fratio_NH_Ne_9_12, Data_fratio_NH_Ne_12_15, Data_fratio_NH_Ne_21_24, Data_fratio_NH_Ne_0_03][mask], labels = ['9-12', '12-15', '21-24', '0-03'])
# plt.xlabel('Magnetic Local Time [MLT]')
# plt.ylabel('PCP edge ratio [f]')
# plt.show()

plt.title('Boxplot')
plt.boxplot([arr1, arr2, arr3, arr4], labels = ['9-12', '12-15', '21-24', '0-03'])
plt.xlabel('Magnetic Local Time [MLT]')
plt.ylabel('PCP edge ratio [f]')
plt.show()