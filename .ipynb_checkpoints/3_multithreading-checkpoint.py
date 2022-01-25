from random import randint
from threading import Thread
from time import time, sleep

def download(filename):
    print(f'start downloading {filename}......')
    time_to_download = randint(5,10)
    sleep(time_to_download)
    print(f'{filename} done! {time_to_download}s')


def main():
    start = time()
    # 使用 threading 模組的 Thread 類別來創建線程 (thread) 
    t1 = Thread (target = download, args =('Python.pdf',))
    t1.start()
    t2 = Thread (target = download, args =('Hot.avi',))
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print(f'Total Time: {end-start}s')

if __name__ == '__main__':
    main()