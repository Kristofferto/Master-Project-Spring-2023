import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from tqdm import tqdm, trange
import sys
from scipy import stats
# data_list = ['Background_Ne', 'Foreground_Ne', 'Grad_Ne_at_100km', 'Grad_Ne_at_20km', 'Grad_Ne_at_50km', 'Grad_Ne_at_PCP_edge',  'Longitude', 'Ne', 'PCP_flag', 'Radius', 'Timestamp', 'Latitude', 'MLT']
data_list = ['Ne', 'PCP_flag', 'Timestamp', 'MLT', 'MLAT', 'Foreground_Ne']
sat_list = ['A', 'C']

#path mac
# path = 'Data/'
# #path hjemme
path = 'D:/Git_Codes/Data/'

# #path UiO
# path = 'C:/Users/krisfau/Desktop/VSCode/Data/'


for sat in tqdm(sat_list, desc = 'Loading satellite data'):
    for name in data_list:
        exec(f'{name}_{sat} = np.load("{path}Data_{sat}_{name}.npy", allow_pickle = True)')

for sat in sat_list:
    exec(f'change01 = np.where((PCP_flag_{sat} == 0) & (PCP_flag_{sat} != np.roll(PCP_flag_{sat},1)))[0]')
    exec(f'change10 = np.where((PCP_flag_{sat} == 0) & (PCP_flag_{sat} != np.roll(PCP_flag_{sat},-1)))[0]')
    PCP_indices = np.concatenate((change01, change10))
    exec(f'PCP_index_{sat} = np.sort(PCP_indices)')


for sat in sat_list:
    exec(f'change14 = np.where((PCP_flag_{sat} == 4) & (PCP_flag_{sat} != np.roll(PCP_flag_{sat},1)))[0]')
    exec(f'change41 = np.where((PCP_flag_{sat} == 4) & (PCP_flag_{sat} != np.roll(PCP_flag_{sat},-1)))[0]')
    PCP_proper = np.concatenate((change14, change41))
    exec(f'PCP_proper_{sat} = np.sort(PCP_proper)')
# print(PCP_index_A[:100])
# print(len(PCP_index_A))
# print(PCP_proper_A[:100])
# print(len(PCP_proper_A))

# for i in range(0, len(PCP_index_A), 2):
#         #, desc = F'Finding and plotting PCP_index_A for satellite {sat}'
        
#         if np.abs(MLAT_A[PCP_index_A[i]]) > np.abs(MLAT_A[PCP_index_A[i+1]]):
#             start = PCP_index_A[i+1]
#             end = PCP_index_A[i]
#             start_prop = PCP_proper_A[np.argmin(np.abs(PCP_proper_A - start))]
#             end_prop = PCP_proper_A[np.argmin(np.abs(PCP_proper_A - end))]

#         elif np.abs(MLAT_A[PCP_index_A[i]]) < np.abs(MLAT_A[PCP_index_A[i+1]]):
#             start = PCP_index_A[i]
#             end = PCP_index_A[i+1]
#             start_prop = PCP_proper_A[np.argmin(np.abs(PCP_proper_A - start))]
#             end_prop = PCP_proper_A[np.argmin(np.abs(PCP_proper_A - end))]


#         print('start :', start)
#         print('end :', end)
#         print('start_proper :', start_prop)
#         print('end_proper :', end_prop)
#         if i == 8:
#             break

# sys.exit()

x_range = np.linspace(0, 100, 100001)


def PCP_std(PCP, MLT, MLT_max, MLT_min, MLAT, Ne, Time, sat, Foreground, PCP_flag, PCP_proper):
    ncount = 0    
    std_trail = 0
    std_lead = 0
    std_prop = 0
    a_count = 0
    b_count = 0
    

    for i in trange(0, len(PCP), 2, desc = F'Calculating the standard deviation for satellite {sat}'):
        #, desc = F'Finding and plotting PCP for satellite {sat}'
        if (9 <= MLT_max <= 15) & (9 <= MLT_min <= 15):
            if np.abs(MLAT[PCP[i]]) > np.abs(MLAT[PCP[i+1]]):
                start = PCP[i+1]
                end = PCP[i]
                start_prop = PCP_proper[np.argmin(np.abs(PCP_proper - start))]
                end_prop = PCP_proper[np.argmin(np.abs(PCP_proper - end))]

            elif np.abs(MLAT[PCP[i]]) < np.abs(MLAT[PCP[i+1]]):
                start = PCP[i]
                end = PCP[i+1]
                start_prop = PCP_proper[np.argmin(np.abs(PCP_proper - start))]
                end_prop = PCP_proper[np.argmin(np.abs(PCP_proper - end))]

        elif ((21 <= MLT_max <= 24) & (21 <= MLT_min <= 24)) | (( 0 <= MLT_max <= 3) & (0 <= MLT_min <= 3)):
            if np.abs(MLAT[PCP[i]]) < np.abs(MLAT[PCP[i+1]]):
                start = PCP[i+1]
                end = PCP[i]
                start_prop = PCP_proper[np.argmin(np.abs(PCP_proper - start))]
                end_prop = PCP_proper[np.argmin(np.abs(PCP_proper - end))]

            elif np.abs(MLAT[PCP[i]]) > np.abs(MLAT[PCP[i+1]]):
                start = PCP[i]
                end = PCP[i+1]
                start_prop = PCP_proper[np.argmin(np.abs(PCP_proper - start))]
                end_prop = PCP_proper[np.argmin(np.abs(PCP_proper - end))]


        
        if (np.all((MLAT[start:end] > 0)) == True) & (np.all((Ne[start:end] > 0)) == True) & \
                                                     (MLT_max >= MLT[start] >= MLT_min) & \
                                                     (MLT_min <= MLT[end] <= MLT_max) & \
                                                     ((end - start) > 30) & \
                                                     (np.abs(MLAT[end] - MLAT[start]) > 3) & \
                                                     (np.isnan(MLT[start]) == False) & \
                                                     (np.isnan(MLT[end]) == False) & \
                                                     (np.any((PCP_flag[start:end] == 4))) & \
                                                     (start < start_prop) & \
                                                     (start_prop < end_prop) & \
                                                     (end_prop < end):
            # y1 = np.interp(x_range, np.linspace(0, 100, len(MLAT[start:start_prop])), Ne[start:start_prop])
            # y2 = np.interp(x_range, np.linspace(0, 100, len(MLAT[end_prop:end])), Ne[end_prop:end])

            # m, b = np.polyfit(x_range, y1)

            #y2 = np.interp(x_range, np.linspace(0, 100, len(Ne[start:end])), Ne[start:end])
            slope, intercept, r_value, p_value, std_err = stats.linregress(MLAT[start:start_prop], Ne[start:start_prop])
            slope1, intercept1, r_value1, p_value1, std_err1 = stats.linregress(MLAT[end_prop:end], Ne[end_prop:end])
            
            slope3, intercept3, r_value3, p_value3, std_err2 = stats.linregress(MLAT[start:start_prop], Foreground[start:start_prop])
            slope4, intercept4, r_value4, p_value4, std_err3 = stats.linregress(MLAT[end_prop:end], Foreground[end_prop:end])

            if (np.isnan(std_err) == False) & (np.isnan(std_err1) == False) & \
                                              (np.isnan(std_err2) == False) & \
                                              (np.isnan(std_err3) == False) & \
                                              ((std_err1 != 0) == True) & \
                                              ((std_err3 != 0) == True):
                f_Ne = std_err / std_err1
                f_Foreground = std_err2 / std_err3

                if (12 >= MLT[start] >= 9) & (9 <= MLT[end] <= 12):
                    f_list_Ne_9_12.append(f_Ne)
                    f_list_Fg_9_12.append(f_Foreground)
                elif (15 >= MLT[start] >= 12) & (12 <= MLT[end] <= 15):
                    f_list_Ne_12_15.append(f_Ne)
                    f_list_Fg_12_15.append(f_Foreground)
                elif (24 >= MLT[start] >= 21) & (21 <= MLT[end] <= 24):
                    f_list_Ne_21_24.append(f_Ne)
                    f_list_Fg_21_24.append(f_Foreground)
                elif (3 >= MLT[start] >= 0) & (0 <= MLT[end] <= 3):
                    f_list_Ne_0_03.append(f_Ne)
                    f_list_Fg_0_03.append(f_Foreground)
                
    
            #     c = std_err2
            #     d = std_err3
            #     a_count += 1
            #     b_count += 1
            # # c = np.std(Ne[start_prop:end_prop])
            #     std_trail += a
            #     std_lead += b
            # std_prop += c
            # print('########')
            # print('start:', start)
            # print('end:', end)
            # print('start prop:', start_prop)
            # print('end prop:', end_prop)
            # print('Std trail            :', a)
            # print('Std lead             :', b)
            # print('Ratio trail / lead   :', a/b)
            
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
    
        # if ncount == 100:
        #     break
    # print('##################################')
    # print(f'std_trail: {std_trail}')
    # print(f'std_lead: {std_lead}')
    # print(f'std_prop: {std_prop}')
    # print(f'Sum Ratio trail / lead Sat {sat} \n MLT: {MLT_min} - {MLT_max} :', std_trail / std_lead)
    # print('######################################################')
    # print(f_list_Ne_9_12)
    # print('######################################################')
            
        
# for sat in sat_list:
#     exec(f'PCP_plotter(PCP_index_{sat}, MLT_{sat}, MLAT_{sat}, Ne_{sat}, Timestamp_{sat}, sat)')

#PCP_plotter(PCP, MLT, MLT_max, MLT_min MLAT, Ne, Time, sat)

#Input variables for plotting


f_list_Ne_9_12 = []
f_list_Fg_9_12 = []

f_list_Ne_12_15 = []
f_list_Fg_12_15 = []

f_list_Ne_21_24 = []
f_list_Fg_21_24 = []

f_list_Ne_0_03 = []
f_list_Fg_0_03 = []

MLT_max_list = np.array([12, 15, 24, 3])
MLT_min_list = np.array([9, 12, 21, 0])
for sat in sat_list:
    for i in range(len(MLT_max_list)):
        MLT_max = MLT_max_list[i]
        MLT_min = MLT_min_list[i]
        exec(f'PCP_std(PCP_index_{sat}, MLT_{sat}, MLT_max, MLT_min, MLAT_{sat}, Ne_{sat}, Timestamp_{sat}, sat, Foreground_Ne_{sat}, PCP_flag_{sat}, PCP_proper_{sat})')
        plt.close()

print(f'### Currently saving the f ratio data... ###')
np.save(path + "Data_fratio_NH_Ne_9_12", np.array(f_list_Ne_9_12))
np.save(path + "Data_fratio_NH_Fg_9_12", np.array(f_list_Ne_9_12))

np.save(path + "Data_fratio_NH_Ne_12_15", np.array(f_list_Ne_12_15))
np.save(path + "Data_fratio_NH_Fg_12_15", np.array(f_list_Ne_12_15))

np.save(path + "Data_fratio_NH_Ne_21_24", np.array(f_list_Ne_21_24))
np.save(path + "Data_fratio_NH_Fg_21_24", np.array(f_list_Ne_21_24))

np.save(path + "Data_fratio_NH_Ne_0_03", np.array(f_list_Ne_0_03))
np.save(path + "Data_fratio_NH_Fg_0_03", np.array(f_list_Ne_0_03))
