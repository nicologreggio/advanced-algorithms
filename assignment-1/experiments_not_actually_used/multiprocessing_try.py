from concurrent.futures import ThreadPoolExecutor
import multiprocessing as mp
from time import perf_counter_ns as cns

base=10000
N=100

def sth(n):
    for i in range(N):
        for j in range(i):
            i*j*n


if __name__ == '__main__':
    s=cns()
    for i in range(base):
        sth(50)
    e=cns()
    t1=(e-s)/10**9

    pool=mp.Pool()
    s=cns()
    pool.map(sth, range(base))
    e=cns()
    t2=(e-s)/10**9


    print("t1: ", t1, "\tt2: ", t2)