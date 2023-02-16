import numpy as np
from tqdm import trange


a= np.random.randint(0,4,20)


a = np.array([0,0,0,0,0,0,1,1,1,1,1,1,4,4,4,4,4,4,4,4,4,4,4,1,1,1,1,1,0,0,0,0,0,0,1,1,1,4,4,4,1,1,1,0,0,0])
print(a)

#hvorfor funker disse alene
print(np.where((a[:-1] != a[1:]))[0])
print(np.where(a == 0)[0])

print('###########')
#MEN IKKE DENNE.... POKKER HELLER
print(np.where((a[:-1] == 0) & (a[:-1] != a[1:]) & (a[1:] != a[:-1]))[0])
#test 123456
    # print(np.where(a == 0)[0]) hei
