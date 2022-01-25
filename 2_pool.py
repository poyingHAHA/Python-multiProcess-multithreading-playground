'''
    如果要啟動大量的子進程，可以用進程池的方式批量創建子進程：
'''

from multiprocessing import Pool
import os
import time
import random

def long_time_task(name):
    print(f'Run task {name} ({os.getpid()})... ')
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print(f"Task {name} done")


if __name__=='__main__':
    long_time_task("0")
    print(f"Parent process {os.getpid()}.")
    p = Pool(10)
    for i in range(5):
        p.apply_async(long_time_task, args=(i+1,))

    print("waiting for all subprocess done...")
    p.close()
    p.join()
    print("All subprocess done.")