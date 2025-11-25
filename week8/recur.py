import numpy as np

step = 0.001
n = 0
def f(a):
    sum = 0
    for element in a:
        sum += element**2
    return sum

def integrate(f, rlist):
    area = 0.0
    for element in np.arange(rlist[n][0], rlist[n][1], step):
        n += 1
        
        area += f(element)*step**rlist.shape[0]
    return area