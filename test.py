import numpy as np
from tqdm import trange


a= np.random.randint(0,4,20)

path = 'C:/Users/krisfau/Desktop/VSCode/Data/'


PCP = np.load(f"{path}Data_A_PCP_flag.npy", allow_pickle = True)

a = np.array([0,0,0,0,0,0,1,1,4,4,4,1,1,0,0,0,1,1,1,4,4,4,1,1,1,0,0,0])
print(a)
print(len(a))
#hvorfor funker disse alene
print(np.where((a[:-1] != a[1:]))[0])
print(np.where(a[:-1] == 0)[0])

print('###########')
#MEN IKKE DENNE.... POKKER HELLER
print(np.where((PCP[:-1] == 0) & (PCP[:-1] != PCP[1:]))[0])

    # print(np.where(a == 0)[0])


