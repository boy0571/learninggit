__author__ = 'AA'
from dtw import dtw
from numpy import *
import numpy as np
import pandas as pd
import time
import threading
import thread
from time import ctime,sleep
data = pd.DataFrame(np.random.randint(0,40,(1000,30)))
dists = pd.DataFrame(np.zeros((1000,1000)))
#print data
#print dists

time0=time.time()
data=data.apply(lambda x: (x - np.min(x)) / (np.max(x) - np.min(x)),axis=1)
time0=time.time()
#print data
#dist, cost, acc, path = dtw(x, y, dist=lambda x, y:np.linalg.norm(x - y, ord=1))
'''
for i in range(len(data)-1,-1,-1):
    for j in range(i,-1,-1):
        print i,j
        x = data.loc[i,].reshape(-1,1)
        y = data.loc[j,].reshape(-1,1)
        dist, cost, acc, path = dtw(x, y, dist=lambda x, y:np.linalg.norm(x - y, ord=1))
        print dist
        dists.loc[i,j]=dist
print dists
print time.time()-time0


'''
def row(end,start):
    for i in range(end,start,-1):
        for j in range(i,-1,-1):
            print i,j
            x = data.loc[i,].reshape(-1,1)
            y = data.loc[j,].reshape(-1,1)
            dist, cost, acc, path = dtw(x, y, dist=lambda x, y:np.linalg.norm(x - y, ord=1))
            print dist
            dists.loc[i,j]=dist
    print time.time()-time0


from multiprocessing import Process


if __name__ == '__main__':
    p1 = Process(target=row, args=(1000-1,930-1,))
    p1.start()
    p2 = Process(target=row, args=(930-1,850-1,))
    p2.start()
    p3 = Process(target=row, args=(850-1,780-1,))
    p3.start()
    p4 = Process(target=row, args=(780-1,690-1,))
    p4.start()
    p5 = Process(target=row, args=(690-1,590-1,))
    p5.start()
    p6 = Process(target=row, args=(590-1,450-1,))
    p6.start()
    p7 = Process(target=row, args=(450-1,350-1,))
    p7.start()
    p8 = Process(target=row, args=(350-1,-1,))
    p8.start()
    #print time.time()-time0