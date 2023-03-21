import numpy as np

import matplotlib.pyplot as plt
import time
import datetime as dt
import pandas as pd

from time import sleep
from tqdm import tqdm, trange

data_list = ['Longitude', 'Timestamp', 'Latitude', 'Radius']
sat_list = ['A','C']
hemisphere_indicator = ['NH', 'SH']



# path = 'C:/Users/krisfau/Desktop/VSCode/Data/'
# #path hjemme
path = 'D:/Git_Codes/Data/'
# path mac
# path = 'Data/'

for sat in sat_list:
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



N_index_9_12 = Data_fratio_NH_array_index_9_12
S_index_9_12 = Data_fratio_SH_array_index_9_12

N_index_12_15 = Data_fratio_NH_array_index_12_15
S_index_12_15 = Data_fratio_SH_array_index_12_15

N_index_21_24 = Data_fratio_NH_array_index_21_24
S_index_21_24 = Data_fratio_SH_array_index_21_24

N_index_0_03 = Data_fratio_NH_array_index_0_03
S_index_0_03 = Data_fratio_SH_array_index_0_03

def find_index(array):
    index = -1
    for i in range(1, len(array)):
        if array[i] < array[i-1]:
            index = i 
            break 
    return index
import datetime

start_summer = datetime.datetime(1900, 4, 1)
end_summer = datetime.datetime(1900, 10, 1)

s_count = 0
v_count = 0

index_list_summer_9_12 = []
index_list_summer_12_15 = []
index_list_summer_21_24 = []
index_list_summer_0_03 = []

index_list_winter_9_12 = []
index_list_winter_12_15 = []
index_list_winter_21_24 = []
index_list_winter_0_03 = []

print(len(N_index_9_12))
print(len(N_index_12_15))
print(len(N_index_21_24))
print(len(N_index_0_03))

def seasonal_index_split(index_list):
    for k in range(len(index_list)):
        for i in range(len(index_list[k])):
            if i <= find_index(index_list[k]) - 1: #Timestamp data for Sat A
                if start_summer.month <= Timestamp_A[index_list[k][i]].month <= end_summer.month and \
                start_summer.day <= Timestamp_A[index_list[k][i]].day <= end_summer.day:
                    if k == 0:
                        index_list_summer_9_12.append(index_list[k])
                    elif k ==1:
                        index_list_summer_12_15.append(index_list[k])
                    elif k ==2:
                        index_list_summer_21_24.append(index_list[k])
                    elif k ==3:
                        index_list_summer_0_03.append(index_list[k])
                        
            elif i > find_index(index_list) - 1: #Timestamp data for Sat C
                if start_summer.month <= Timestamp_A[index_list[k][i]].month <= end_summer.month and \
                start_summer.day <= Timestamp_A[index_list[k][i]].day <= end_summer.day:
                    if k == 0:
                        index_list_summer_9_12.append(index_list[k])
                    elif k ==1:
                        index_list_summer_12_15.append(index_list[k])
                    elif k ==2:
                        index_list_summer_21_24.append(index_list[k])
                    elif k ==3:
                        index_list_summer_0_03.append(index_list[k])

seasonal_index_split([N_index_9_12, N_index_12_15, N_index_21_24, N_index_0_03])
seasonal_index_split([S_index_9_12, S_index_12_15, S_index_21_24, S_index_0_03])

print('##############')
print(index_list_summer_9_12)

for i in range(len(Timestamp_C)):
    if start_summer.month <= Timestamp_C[i].month <= end_summer.month and \
        start_summer.day <= Timestamp_C[i].day <= end_summer.day:
        s_count += 1
    else: 
        v_count += 1

print('Sommer:', s_count)
print('Vinter:', v_count)


"""
#KM
Radius = Radius/1000 - 6371


n = 200000
x = 24292223  - 65_000             #For feilmelding: A = -15... B = + 107_000 ... C = - 65_000
a = np.zeros(n)

# Dette fungerer opp til ett visst punkt___ (24650200 av 37 millioner)
#x = 0
print(f'### Generating MLT data for satellite {sat} ###')
for i in trange(len(Timestamp[x:x+n])):
    apex_out = apexpy.Apex(Timestamp[x+i])
    atime = pd.to_datetime(Timestamp[x+i])
    mlat, mlt = apex_out.convert(Latitude[x+i], Longitude[x+i], 'geo', 'mlt', datetime=atime, height = Radius[x+i])
    print('Timestamp:', Timestamp[x+i])
    if np.isnan(mlt):
        print('Her feiler den:',x+i)
        print(Timestamp[x+i],Latitude[x+i],Longitude[x+i], Radius[x+i])
        print('Her fungerer den:',x+i-1)
        print(Timestamp[x+i-1],Latitude[x+i-1],Longitude[x+i-1], Radius[x+i-1])
        break
    a[i] = mlt



### A ###
Her feiler den: 24292223
2020-01-01 00:00:06.197000 77.01258445761522 103.30880512241181 431.9222690998913
Her fungerer den: 24292222
2019-12-31 23:20:02.197000 -77.03852984882656 90.27543024995508 449.87112311645615

### B ###
Her feiler den: 24399941
2020-01-01 00:00:01.197000 87.64582786716237 -22.763411712336502 497.7811695642895
Her fungerer den: 24399940
2020-01-01 00:00:00.197000 87.6636345182061 -24.249622295059453 497.781516804881

### C ###
Her feiler den: 24237684
2020-01-01 00:00:01.197000 77.20744724933166 104.87853789954224 431.8978422981618
Her fungerer den: 24237683
2020-01-01 00:00:00.197000 77.14441302186003 104.82211573355681 431.9013349004026


print(a)
print(f'### Currently saving the data for satellite {sat} ###')
# np.save('D:/VSCode/Data_B_MLT', a)
"""



# data_list = ['MLT']
# sat_list = ['A', 'B', 'C']


# path = 'C:/Users/krisfau/Desktop/VSCode/Data/'

# for sat in sat_list:
#     for name in data_list:
#         exec(f'{name}_{sat} = np.load("{path}Data_{sat}_{name}.npy", allow_pickle = True)')

# count_A = 0
# count_B = 0
# count_C = 0
# for i in trange(len(MLT_A)):
#     if np.isnan(MLT_A[i]):
#         count_A +=1

# for i in trange(len(MLT_B)):
#     if np.isnan(MLT_B[i]):
#         count_B +=1

# for i in trange(len(MLT_C)):
#     if np.isnan(MLT_C[i]):
#         count_C +=1

# print('A:', len(MLT_A) - count_A)
# print('B:', len(MLT_B) - count_B)
# print('C:', len(MLT_C) - count_C)
"""
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

print(PCP_flag_B[:200])
print(PCP_index_B[:100])
"""

