import numpy as np

import matplotlib.pyplot as plt
import time
import datetime as dt
import pandas as pd
import apexpy
from time import sleep
from tqdm import tqdm, trange
"""
data_list = ['Longitude', 'Timestamp', 'Latitude', 'Radius']
sat_list = ['C']


path = 'C:/Users/krisfau/Desktop/VSCode/Data/'

for sat in sat_list:
    for name in data_list:
        exec(f'{name} = np.load("{path}Data_{sat}_{name}.npy", allow_pickle = True)')

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



data_list = ['MLT']
sat_list = ['A', 'B', 'C']


path = 'C:/Users/krisfau/Desktop/VSCode/Data/'

for sat in sat_list:
    for name in data_list:
        exec(f'{name}_{sat} = np.load("{path}Data_{sat}_{name}.npy", allow_pickle = True)')

count_A = 0
count_B = 0
count_C = 0
for i in trange(len(MLT_A)):
    if np.isnan(MLT_A[i]):
        count_A +=1

for i in trange(len(MLT_B)):
    if np.isnan(MLT_B[i]):
        count_B +=1

for i in trange(len(MLT_C)):
    if np.isnan(MLT_C[i]):
        count_C +=1

print('A:', len(MLT_A) - count_A)
print('B:', len(MLT_B) - count_B)
print('C:', len(MLT_C) - count_C)