import numpy as np
from tqdm import tqdm, trange
#testtest
#path mac
# #path hjemme
#path = 'D:\\Git_Codes\\Data\\'

# #path UiO
# path = 'C:/Users/krisfau/Desktop/VSCode/Data/'

data_list = ['PCP_flag']
sat_list = ['A', 'B', 'C']


for sat in tqdm(sat_list, desc = 'Loading satellite data'):
    for name in data_list:
        exec(f'{name}_{sat} = np.load("{path}Data_{sat}_{name}.npy", allow_pickle = True)')


a= np.random.randint(0,4,20)


a = np.array([0,0,0,0,0,0,1,1,1,1,1,1,4,4,4,4,4,4,4,4,4,4,4,1,1,1,1,1,0,0,0,0,0,0,1,1,1,4,4,4,1,1,1,0,0,0])
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
en = np.where((PCP_flag_A == 0) & (PCP_flag_A != np.roll(PCP_flag_A,1)))[0]
to = np.where((PCP_flag_A == 0) & (PCP_flag_A != np.roll(PCP_flag_A,-1)))[0]

array = np.concatenate((en, to))
array1 = np.sort(array)
print(array1)

print(len(array1) / 2)