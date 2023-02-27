import numpy as np
from tqdm import tqdm, trange
import matplotlib.pyplot as plt
#testtest
#path mac
path = 'Data/'
# #path hjemme
#path = 'D:\\Git_Codes\\Data\\'

# #path UiO
# path = 'C:/Users/krisfau/Desktop/VSCode/Data/'

data_list = ['PCP_flag', 'MLAT', 'MLT', 'Ne', 'Timestamp']
#data_list = ['PCP_flag']
sat_list = ['A', 'B', 'C']


for sat in tqdm(sat_list, desc = 'Loading satellite data'):
    for name in data_list:
        exec(f'{name}_{sat} = np.load("{path}Data_{sat}_{name}.npy", allow_pickle = True)')


a= np.random.randint(0,4,20)

path = 'C:/Users/krisfau/Desktop/VSCode/Data/'


PCP = np.load(f"{path}Data_A_PCP_flag.npy", allow_pickle = True)

a = np.array([0,0,0,0,0,0,1,1,4,4,4,1,1,0,0,0,1,1,1,4,4,4,1,1,1,0,0,0])
print(a)
"""
PCP_flag_A
#DETTE FUNGERER FAKTISK
print(np.where((a == 0) & (a != np.roll(a,1)))[0])
print(np.where((a == 0) & (a != np.roll(a,-1)))[0])

en = np.where((a == 0) & (a != np.roll(a,1)))[0]
to = np.where((a == 0) & (a != np.roll(a,-1)))[0]

array = np.concatenate((en, to))
array1 = np.sort(array)
print(array1)
"""
PCP_flag_A = PCP_flag_A
en = np.where((PCP_flag_A == 0) & (PCP_flag_A != np.roll(PCP_flag_A,1)))[0]
to = np.where((PCP_flag_A == 0) & (PCP_flag_A != np.roll(PCP_flag_A,-1)))[0]

array = np.concatenate((en, to))
array1 = np.sort(array)
print(PCP_flag_A)
print(array1)
#test
print(len(array1) / 2)

count = 0
for i in trange(0, len(array1), 2):
    
    if MLAT_A[array1[i]] > MLAT_A[array1[i+1]]:
        start = array1[i+1]
        end = array1[i]
    elif MLAT_A[array1[i]] < MLAT_A[array1[i+1]]:
        start = array1[i]
        end = array1[i+1]
    #if MLT_A[start] > 9  and MLT_A[end] < 15:
    count += 1
    plt.title('Northern Hemisphere')
    plt.plot(np.arange(0,end - start), Ne_A[start:end], label = f'Patch_{count}')
        #MLAT_A[start:end]

    print(array1[i])
    print(array1[i+1])

    if count ==20:
        break
plt.legend()
plt.show()
print(count)
"""
plt.scatter(MLAT_A[850:950], Ne_A[850:950], label = 'Ne over MLAT')
plt.legend()
plt.show()

plt.scatter(Timestamp_A[850:950], Ne_A[850:950], label = 'Ne over time')
plt.legend()
plt.show()

"""