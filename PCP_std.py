import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from tqdm import tqdm, trange
from scipy import stats

data_list = ['Ne', 'PCP_flag', 'Timestamp', 'MLT', 'MLAT', 'Foreground_Ne']
sat_list = ['A', 'C']

#Path
path_mac = 'Data/'
savepath_mac = 'Figures/'

savepath = savepath_mac
path = path_mac

#Loading the satellite data
for sat in tqdm(sat_list, desc = 'Loading satellite data'):
    for name in data_list:
        exec(f'{name}_{sat} = np.load("{path}Data_{sat}_{name}.npy", allow_pickle = True)')


#Locating where the PCP flag data indicates PCP edge
for sat in sat_list:
    exec(f'change01 = np.where((PCP_flag_{sat} == 0) & (PCP_flag_{sat} != np.roll(PCP_flag_{sat},1)))[0]')
    exec(f'change10 = np.where((PCP_flag_{sat} == 0) & (PCP_flag_{sat} != np.roll(PCP_flag_{sat},-1)))[0]')
    PCP_indices = np.concatenate((change01, change10))
    #Sorting the values in ascending order
    exec(f'PCP_index_{sat} = np.sort(PCP_indices)')

#Loacting where the PCP flag data indicates PCP proper, ie. inside of a polar cap patch
for sat in sat_list:
    exec(f'change14 = np.where((PCP_flag_{sat} == 4) & (PCP_flag_{sat} != np.roll(PCP_flag_{sat},1)))[0]')
    exec(f'change41 = np.where((PCP_flag_{sat} == 4) & (PCP_flag_{sat} != np.roll(PCP_flag_{sat},-1)))[0]')
    PCP_proper = np.concatenate((change14, change41))
    #Sorting the values in ascending order
    exec(f'PCP_proper_{sat} = np.sort(PCP_proper)')


def PCP_std(PCP, MLT, MLT_max, MLT_min, MLAT, Ne, Time, sat, Foreground, PCP_flag, PCP_proper):
    ###Function to calculate the standard deviation between density measurements in the trailing vs leading edge###
    PCP_count = 0    

    for i in trange(0, len(PCP), 2, desc = F'Calculating the standard deviation for satellite {sat}'):

        if (6 <= MLT_max <= 18) & (6 <= MLT_min <= 18):
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

        elif ((18 <= MLT_max <= 24) & (18 <= MLT_min <= 24)) | (( 0 <= MLT_max <= 6) & (0 <= MLT_min <= 6)):
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

        #Currently set to the northern hemisphere    |Criteria for the polar cap patches
        if (np.all((MLAT[start:end] > 0)) == True) & (np.all((Ne[start:end] > 0)) == True) & \
                                                     (MLT_max >= MLT[start] >= MLT_min) & \
                                                     (MLT_min <= MLT[end] <= MLT_max) & \
                                                     ((end - start) > 15) & \
                                                     (np.abs(MLAT[end] - MLAT[start]) > 1) & \
                                                     (np.isnan(MLT[start]) == False) & \
                                                     (np.isnan(MLT[end]) == False) & \
                                                     (np.any((PCP_flag[start:end] == 4))) & \
                                                     (start < start_prop) & \
                                                     (start_prop < end_prop) & \
                                                     (end_prop < end):
            
            #Using a linear regression tool from scipy/stats to calculate the linear regression of the PCP trailing and leading edges
            #This also provides us with the standard deviation 
            #Calculating the standard deviation for the trailing (slope) and leading edge (slope 1) using density measurements
            slope, intercept, r_value, p_value, std_err = stats.linregress(MLAT[start:start_prop], Ne[start:start_prop])
            slope1, intercept1, r_value1, p_value1, std_err1 = stats.linregress(MLAT[end_prop:end], Ne[end_prop:end])
            
            #Calculating the standard deviation for the trailing (slope3) and leading edge (slope 4) using foreground density measurements
            slope3, intercept3, r_value3, p_value3, std_err2 = stats.linregress(MLAT[start:start_prop], Foreground[start:start_prop])
            slope4, intercept4, r_value4, p_value4, std_err3 = stats.linregress(MLAT[end_prop:end], Foreground[end_prop:end])

            #Excluding values that are zero or NaN
            if (np.isnan(std_err) == False) & (np.isnan(std_err1) == False) & \
                                              (np.isnan(std_err2) == False) & \
                                              (np.isnan(std_err3) == False) & \
                                              ((std_err1 != 0) == True) & \
                                              ((std_err3 != 0) == True):
                #Calculating the ratio for the standard deviation of the trailing and leading edge of individual polar cap patches
                f_Ne = std_err / std_err1
                f_Foreground = std_err2 / std_err3
                #Splitting up the calculations of the standard deviation ratio for different intervals regarding magnetic local time
                if (12 >= MLT[start] >= 9) & (9 <= MLT[end] <= 12):
                    f_list_Ne_9_12.append(f_Ne)
                    f_list_Fg_9_12.append(f_Foreground)

                    f_list_PCP_index_9_12.append(start)
                    f_list_PCP_index_9_12.append(end)

                elif (15 >= MLT[start] >= 12) & (12 <= MLT[end] <= 15):
                    f_list_Ne_12_15.append(f_Ne)
                    f_list_Fg_12_15.append(f_Foreground)

                    f_list_PCP_index_12_15.append(start)
                    f_list_PCP_index_12_15.append(end)

                elif (24 >= MLT[start] >= 21) & (21 <= MLT[end] <= 24):
                    f_list_Ne_21_24.append(f_Ne)
                    f_list_Fg_21_24.append(f_Foreground)

                    f_list_PCP_index_21_24.append(start)
                    f_list_PCP_index_21_24.append(end)

                elif (3 >= MLT[start] >= 0) & (0 <= MLT[end] <= 3):
                    f_list_Ne_0_03.append(f_Ne)
                    f_list_Fg_0_03.append(f_Foreground)

                    f_list_PCP_index_0_03.append(start)
                    f_list_PCP_index_0_03.append(end)

                elif (18 > MLT[start] > 15) & (15 <= MLT[end] < 18):
                    f_list_Ne_15_18.append(f_Ne)
                    f_list_Fg_15_18.append(f_Foreground)

                    f_list_PCP_index_15_18.append(start)
                    f_list_PCP_index_15_18.append(end)

                elif (9 > MLT[start] > 6) & (6 < MLT[end] < 9):
                    f_list_Ne_6_9.append(f_Ne)
                    f_list_Fg_6_9.append(f_Foreground)

                    f_list_PCP_index_6_9.append(start)
                    f_list_PCP_index_6_9.append(end)
                
                elif (21 > MLT[start] > 18) & (18 <= MLT[end] < 21):
                    f_list_Ne_18_21.append(f_Ne)
                    f_list_Fg_18_21.append(f_Foreground)

                    f_list_PCP_index_18_21.append(start)
                    f_list_PCP_index_18_21.append(end)

                elif (6 > MLT[start] > 3) & (3 < MLT[end] < 6):
                    f_list_Ne_3_6.append(f_Ne)
                    f_list_Fg_3_6.append(f_Foreground)

                    f_list_PCP_index_3_6.append(start)
                    f_list_PCP_index_3_6.append(end)
                
                
                PCP_count +=1

#Empty lists for appending the calculated standard deviation ratios
#Two lists for every MLT interval, one calculated using density measurements and one using foreground density
#MLT 9-12
f_list_Ne_9_12  = []
f_list_Fg_9_12  = []
#MLT 12-15
f_list_Ne_12_15 = []
f_list_Fg_12_15 = []
#MLT 21-24
f_list_Ne_21_24 = []
f_list_Fg_21_24 = []
#MLT 0-03
f_list_Ne_0_03  = []
f_list_Fg_0_03  = []
#MLT 15-18
f_list_Ne_15_18 = []
f_list_Fg_15_18 = []
#MLT 6-9
f_list_Ne_6_9   = []
f_list_Fg_6_9   = []
#MLT 18-21
f_list_Ne_18_21 = []
f_list_Fg_18_21 = []
#MLT 3-6
f_list_Ne_3_6   = []
f_list_Fg_3_6   = []

#Index for the PCP used in calculating the ratio
f_list_PCP_index_9_12   = []
f_list_PCP_index_12_15  = []
f_list_PCP_index_21_24  = []
f_list_PCP_index_0_03   = []
f_list_PCP_index_15_18  = []
f_list_PCP_index_6_9    = []
f_list_PCP_index_18_21  = []
f_list_PCP_index_3_6    = []

#Making the calcuations using predetermined MLT intervals
MLT_max_list = np.array([9, 12, 15, 18, 21, 24, 3, 6])
MLT_min_list = np.array([6, 9,  12, 15, 18, 21, 0, 3])
for sat in sat_list:
    for i in range(len(MLT_max_list)):
        MLT_max = MLT_max_list[i]
        MLT_min = MLT_min_list[i]
        exec(f'PCP_std(PCP_index_{sat}, MLT_{sat}, MLT_max, MLT_min, MLAT_{sat}, Ne_{sat}, Timestamp_{sat}, sat, Foreground_Ne_{sat}, PCP_flag_{sat}, PCP_proper_{sat})')
        plt.close()

# print('PCPs used in the calculations:')
# print(len(np.array(f_list_Ne_9_12)) + len(np.array(f_list_Ne_12_15)) + len(np.array(f_list_Ne_21_24)) + len(np.array(f_list_Ne_0_03)) \
#       + len(np.array(f_list_Ne_15_18)) + len(np.array(f_list_Ne_6_9)) + len(np.array(f_list_Ne_18_21)) + len(np.array(f_list_Ne_3_6)))

# quit()

#Saving arrays containing the calculated standard deviation ratios
print(f'### Currently saving the f ratio data... ###')
np.save(path + "Data_fratio_NH_Ne_9_12", np.array(f_list_Ne_9_12))
np.save(path + "Data_fratio_NH_Fg_9_12", np.array(f_list_Fg_9_12))

np.save(path + "Data_fratio_NH_Ne_12_15", np.array(f_list_Ne_12_15))
np.save(path + "Data_fratio_NH_Fg_12_15", np.array(f_list_Fg_12_15))

np.save(path + "Data_fratio_NH_Ne_21_24", np.array(f_list_Ne_21_24))
np.save(path + "Data_fratio_NH_Fg_21_24", np.array(f_list_Fg_21_24))

np.save(path + "Data_fratio_NH_Ne_0_03", np.array(f_list_Ne_0_03))
np.save(path + "Data_fratio_NH_Fg_0_03", np.array(f_list_Fg_0_03))

np.save(path + "Data_fratio_NH_Ne_15_18", np.array(f_list_Ne_15_18))
np.save(path + "Data_fratio_NH_Fg_15_18", np.array(f_list_Fg_15_18))

np.save(path + "Data_fratio_NH_Ne_6_9", np.array(f_list_Ne_6_9))
np.save(path + "Data_fratio_NH_Fg_6_9", np.array(f_list_Fg_6_9))

np.save(path + "Data_fratio_NH_Ne_18_21", np.array(f_list_Ne_18_21))
np.save(path + "Data_fratio_NH_Fg_18_21", np.array(f_list_Fg_18_21))

np.save(path + "Data_fratio_NH_Ne_3_6", np.array(f_list_Ne_3_6))
np.save(path + "Data_fratio_NH_Fg_3_6", np.array(f_list_Fg_3_6))

#Saving arrays contaiing the indices for the calculations
np.save(path + "Data_fratio_NH_array_index_9_12", np.array(f_list_PCP_index_9_12))
np.save(path + "Data_fratio_NH_array_index_12_15", np.array(f_list_PCP_index_12_15))
np.save(path + "Data_fratio_NH_array_index_21_24", np.array(f_list_PCP_index_21_24))
np.save(path + "Data_fratio_NH_array_index_0_03", np.array(f_list_PCP_index_0_03))
np.save(path + "Data_fratio_NH_array_index_15_18", np.array(f_list_PCP_index_15_18))
np.save(path + "Data_fratio_NH_array_index_6_9", np.array(f_list_PCP_index_6_9))
np.save(path + "Data_fratio_NH_array_index_18_21", np.array(f_list_PCP_index_18_21))
np.save(path + "Data_fratio_NH_array_index_3_6", np.array(f_list_PCP_index_3_6))


print('PCPs used in the calculations:')
print(len(np.array(f_list_Ne_9_12)) + len(np.array(f_list_Ne_12_15)) + len(np.array(f_list_Ne_21_24)) + len(np.array(f_list_Ne_0_03)) \
      + len(np.array(f_list_Ne_15_18)) + len(np.array(f_list_Ne_6_9)) + len(np.array(f_list_Ne_18_21)) + len(np.array(f_list_Ne_3_6)))

