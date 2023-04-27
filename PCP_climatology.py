import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from tqdm import tqdm, trange
from scipy import stats
from  datetime import date
import datetime

data_list = ['Timestamp', 'MLAT']
sat_list = ['A', 'C']
hemisphere_indicator = ['NH', 'SH']

# path mac
path_mac = 'Data/'
savepath_mac = 'Figures/'

# path hjemme
path_hjemme = 'D:/Git_Codes/Data/'
savepath_hjemme = 'D:/Git_Codes/Figures/'
path_hjemme_test = 'D:/Git_Codes/NyData/'


# path UiO
path_UiO = 'C:/Users/krisfau/Desktop/VSCode/Data/'
savepath_UiO = 'C:/Users/krisfau/Desktop/VSCode/FIGURES/'


savepath = savepath_mac
path = path_mac

#Loading satellite data
for sat in tqdm(sat_list, desc = 'Loading locally stored data'):
    for name in data_list:
        exec(f'{name}_{sat} = np.load("{path}Data_{sat}_{name}.npy", allow_pickle = True)')

#Loading locally stored data
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

#Function to find where the indices starts to indicate data for satellite C and not A 
# - this is used to indicate where the timestamp data needs to be changed
def find_index(array):
    index = -1
    for i in range(1, len(array)):
        if array[i] < array[i-1]:
            index = i 
            break 
    return index


def Hour_date_NH(timestamps, latitudes):
    ###Function to find the time spent above |MLAT| = 77 degrees###
    #Define the latitude threshold
    LAT_THRESHOLD = 77
   
    #Empty dictionary to store the total time spent over the latitude threshold for each day
    time_over_lat = {}

    #Initialize the start time to the first timestamp if the first latitude measurement is above the threshold
    if latitudes[0] >= LAT_THRESHOLD:
        start_time = timestamps[0]
    else:
        start_time = None

    for i in range(1, len(timestamps)):
        #Check if the current latitude measurement is above the threshold
        if latitudes[i] >= LAT_THRESHOLD:
            #Additionally check the previous latitude
            if latitudes[i-1] >= LAT_THRESHOLD:
                continue 
            else:
                #Record start time of the passage above the threshold
                start_time = timestamps[i]
        else:
            #Check if the previous latitude measurement was above the threshold
            if latitudes[i-1] >= LAT_THRESHOLD:
                #Record the end time of the passage above the threshold
                end_time = timestamps[i]

                #Time difference in hours
                time_diff = (end_time - start_time).total_seconds() / 3600
                #Adding the time difference to the total time spent over the threshold for the corresponding day
                day = start_time.date()

                if day not in time_over_lat:
                    time_over_lat[day] = time_diff
                else:
                    time_over_lat[day] += time_diff

    return time_over_lat

def Hour_date_SH(timestamps, latitudes):
    ###Function to find the time spent under MLAT = -77 degrees###
    #Define the latitude threshold
    LAT_THRESHOLD = -77
   
    #Empty dictionary to store the total time spent under the latitude threshold for each day
    time_under_lat = {}

    #Initialize the start time to the first timestamp if the first latitude measurement is below the threshold
    if latitudes[0] <= LAT_THRESHOLD:
        start_time = timestamps[0]
    else:
        start_time = None

    for i in range(1, len(timestamps)):
        #Check if the current latitude measurement is below the threshold
        if latitudes[i] <= LAT_THRESHOLD:
            #Check the previous latitude aswell
            if latitudes[i-1] <= LAT_THRESHOLD:
                continue 
            else:
                #Record the start time of the passage below the threshold
                start_time = timestamps[i]
        else:
            #Check if the previous latitude measurement was below the threshold
            if latitudes[i-1] <= LAT_THRESHOLD:
                #Record the end time of the passage below the threshold
                end_time = timestamps[i]

                #Time difference in hours
                time_diff = (end_time - start_time).total_seconds() / 3600
                #Adding the time difference to the total time spent below the threshold for the corresponding day
                day = start_time.date()

                if day not in time_under_lat:
                    time_under_lat[day] = time_diff
                else:
                    time_under_lat[day] += time_diff

    return time_under_lat

    
    
    

def PCP_climatology_PCP_index(index_array):
    ###Function for finding the PCP index for swarm A and swarm C###

    PCP_index_list_A = []
    PCP_index_list_C = []

    #Finding the index for when each PCP occurred
    for i in range(0, len(index_array), 2):
        #Satellite A
        if i <= find_index(index_array) - 1:
            PCP_index_A = int((index_array[i+1] + index_array[i]) / 2)
            PCP_index_list_A.append(PCP_index_A)
            #Satellite C
        elif i > find_index(index_array) - 1:
            PCP_index_C = int((index_array[i+1] + index_array[i]) / 2)
            PCP_index_list_C.append(PCP_index_C)

    return PCP_index_list_A, PCP_index_list_C


#Northern hemisphere, index arrays separated into Swarm A and Swarm C
NH_9_12_A, NH_9_12_C = PCP_climatology_PCP_index(N_index_9_12)
NH_12_15_A, NH_12_15_C = PCP_climatology_PCP_index(N_index_12_15)
NH_21_24_A, NH_21_24_C = PCP_climatology_PCP_index(N_index_21_24)
NH_0_03_A, NH_0_03_C = PCP_climatology_PCP_index(N_index_0_03)
NH_3_6_A, NH_3_6_C = PCP_climatology_PCP_index(N_index_3_6)
NH_6_9_A, NH_6_9_C = PCP_climatology_PCP_index(N_index_6_9)
NH_15_18_A, NH_15_18_C = PCP_climatology_PCP_index(N_index_15_18)
NH_18_21_A, NH_18_21_C = PCP_climatology_PCP_index(N_index_18_21)

#Southern hemisphere, index arrays separated into Swarm A and Swarm C
SH_9_12_A, SH_9_12_C = PCP_climatology_PCP_index(S_index_9_12)
SH_12_15_A, SH_12_15_C = PCP_climatology_PCP_index(S_index_12_15)
SH_21_24_A, SH_21_24_C = PCP_climatology_PCP_index(S_index_21_24)
SH_0_03_A, SH_0_03_C = PCP_climatology_PCP_index(S_index_0_03)
SH_3_6_A, SH_3_6_C = PCP_climatology_PCP_index(S_index_3_6)
SH_6_9_A, SH_6_9_C = PCP_climatology_PCP_index(S_index_6_9)
SH_15_18_A, SH_15_18_C = PCP_climatology_PCP_index(S_index_15_18)
SH_18_21_A, SH_18_21_C = PCP_climatology_PCP_index(S_index_18_21)

#Adding the arrays together in order to find the PCP occurence for each date in the northern and southern hemisphere
NH_Swarm_A = NH_9_12_A + NH_12_15_A + NH_21_24_A + NH_0_03_A + NH_3_6_A + NH_6_9_A + NH_15_18_A + NH_18_21_A
NH_Swarm_C = NH_9_12_C + NH_12_15_C + NH_21_24_C + NH_0_03_C + NH_3_6_C + NH_6_9_C + NH_15_18_C + NH_18_21_C

SH_Swarm_A = SH_9_12_A + SH_12_15_A + SH_21_24_A + SH_0_03_A + SH_3_6_A + SH_6_9_A + SH_15_18_A + SH_18_21_A
SH_Swarm_C = SH_9_12_C + SH_12_15_C + SH_21_24_C + SH_0_03_C + SH_3_6_C + SH_6_9_C + SH_15_18_C + SH_18_21_C

NH_Swarm_A_time = Hour_date_NH(Timestamp_A, MLAT_A)
NH_Swarm_C_time = Hour_date_NH(Timestamp_C, MLAT_C)

SH_Swarm_A_time = Hour_date_SH(Timestamp_A, MLAT_A)
SH_Swarm_C_time = Hour_date_SH(Timestamp_C, MLAT_C)


def PCP_occurrence_rate(Hemisphere, index_list_A, index_list_C):
    ###Funtion for plotting the PCP climatology study, i.e. PCP occurrence rate in the northern and southern hemisphere###
    
    counts_A = {}
    counts_C = {}

    for index in index_list_A:
        #Converting the date string to a datetime object
        date_obj_A = Timestamp_A[index].date()
        #Use the date as the key in the dictionary and increment the PCP count for that date
        counts_A[date_obj_A] = counts_A.get(date_obj_A, 0) + 1
        
    for index in index_list_C:
         #Converting the date string to a datetime object
        date_obj_C = Timestamp_C[index].date()
        #Use the date as the key in the dictionary and increment the PCP count for that date
        counts_C[date_obj_C] = counts_C.get(date_obj_C, 0) + 1

    
    if Hemisphere == 'NH':
        Hours_A = NH_Swarm_A_time
        Hours_C = NH_Swarm_C_time
    
    elif Hemisphere == 'SH':
        Hours_A = SH_Swarm_A_time
        Hours_C = SH_Swarm_C_time

    
    Set_Dates_A = set(counts_A.keys())
    Set_Hours_A = set(Hours_A.keys())

    Set_Dates_C = set(counts_C.keys())
    Set_Hours_C = set(Hours_C.keys())

    common_dates_A = sorted(Set_Dates_A.intersection(Set_Hours_A))
    common_dates_C = sorted(Set_Dates_C.intersection(Set_Hours_C))

    ratios_A = [counts_A[date] / Hours_A[date] for date in common_dates_A]
    ratios_C = [counts_C[date] / Hours_C[date] for date in common_dates_C]

    
    plt.scatter(common_dates_A, ratios_A, label = 'Swarm A', s=20)
    plt.scatter(common_dates_C, ratios_C, label = 'Swarm C', s=20)
    plt.xlabel('Year')
    plt.ylabel('Occurrence rate')
    plt.xticks(rotation=45)
    plt.legend()
    if Hemisphere == 'NH':
        plt.title('NH climatology')
        plt.savefig(savepath + 'NH_climatology.png')
    elif Hemisphere == 'SH':
        plt.title('SH climatology')
        plt.savefig(savepath + 'SH_climatology.png')

    plt.close()
    return common_dates_A, common_dates_C, ratios_A, ratios_C


NH_common_dates_A, NH_common_dates_C, NH_ratios_A, NH_ratios_C = PCP_occurrence_rate('NH', NH_Swarm_A, NH_Swarm_C)
SH_common_dates_A, SH_common_dates_C, SH_ratios_A, SH_ratios_C = PCP_occurrence_rate('SH', SH_Swarm_A, SH_Swarm_C)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(16, 8))

# Plot the data on the first subplot
ax1.set_title('Northern Hemisphere')
ax1.set_ylim(0, 3)
ax1.scatter(NH_common_dates_A, NH_ratios_A, label = 'Swarm A', s=20, color = 'red')
ax1.scatter(NH_common_dates_C, NH_ratios_C, label = 'Swarm C', s=20, color = 'blue')





#Plot the data on the second subplot
ax2.set_title('Southern Hemisphere')
ax2.set_ylim(0, 3)
ax2.scatter(SH_common_dates_A, SH_ratios_A, label = 'Swarm A', s=20, color = 'red')
ax2.scatter(SH_common_dates_C, SH_ratios_C, label = 'Swarm C', s=20, color = 'blue')


for year in range(2014, 2020):
    ax1.axvspan(datetime.date(year, 3, 21), datetime.date(year, 9, 23), facecolor='yellow', alpha=0.3)
    ax1.axvspan(datetime.date(year, 9, 24), datetime.date(year + 1, 3, 20), facecolor='blue', alpha=0.3)

    ax2.axvspan(datetime.date(year, 3, 21), datetime.date(year, 9, 23), facecolor='yellow', alpha=0.3)
    ax2.axvspan(datetime.date(year, 9, 24), datetime.date(year + 1, 3, 20), facecolor='blue', alpha=0.3)



fig.suptitle('PCP climatology study. \n PCP occurrence rate from 2014 to 2019.')
plt.xlabel('Year')
ax1.set_ylabel('Occurrence rate NH \n (#/$h_{PC}$)')
ax2.set_ylabel('Occurrence rate SH \n (#/$h_{PC}$)')
plt.legend()

plt.savefig(savepath + 'Total_climatology.png')
plt.close()

