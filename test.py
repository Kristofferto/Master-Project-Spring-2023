import numpy as np
from tqdm import trange


a= np.random.randint(0,4,20)


a = np.array([0,0,0,0,0,0,1,1,1,1,1,1,4,4,4,4,4,4,4,4,4,4,4,1,1,1,1,1,0,0,0,0,0,0,1,1,1,4,4,4,1,1,1,0,0,0])
print(a)

#hvorfor funker disse alene
print(np.where((a[:-1] != a[1:]))[0])
print(np.where(a == 0)[0])
print(a[:-1])
print(a[1:])
print('###########')
#MEN IKKE DENNE.... POKKER HELLER
# print(np.where((a[:-1] == 0) & (a[:-1] != a[1:]) & (a[1:] != a[:-1]))[0])
#test 123456kjhfwekfhwefkh
    # print(np.where(a == 0)[0]) hei

#DETTE FUNGERER FAKTISK
print(np.where((a == 0) & (a != np.roll(a,1)))[0])
print(np.where((a == 0) & (a != np.roll(a,-1)))[0])

en = np.where((a == 0) & (a != np.roll(a,1)))[0]
to = np.where((a == 0) & (a != np.roll(a,-1)))[0]

array = np.concatenate((en, to))
array1 = np.sort(array)
print(array1)
