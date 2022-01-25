
from multiprocessing import Process
from os import getpid
from random import randint
from time import time, sleep
'''
    子進程要執行的code
    注意: 使用windows系統沒辦法直接print出來
    重點:
        1. os.getpid(): return current process ID
        2. os.getppid(): return parent process ID
        3. Process(task, args): create process
        4. 創建子進程時，只需要傳入一個執行函數和函數的參數，創建一個Process實例，用start()方法啟動，這樣創建進程比fork()還要簡單。
        5. join()方法可以等待子進程結束後再繼續往下運行，通常用於進程間的同步。
'''
def download_task(filename):
    print('start processing, ID[ %d ].' % getpid())
    print('downloading %s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s done %d s' % (filename, time_to_download))

def download_without_multiprocessing():
    start = time()
    download_task('Python.pdf')
    download_task('Hot.avi')
    end = time()
    print('total %.2f s.' % (end - start))

def download_with_multiprocessing():
    start = time()
    # 利用 Process 類別創建了行程物件
    # 透過 target 參數傳入一個函數來表示進程啟動後要執行的程式碼
    # 後面的 args 代表傳遞給函數的參數
    # Process 物件的 start 方法 (method) 用來啟動行程 (process)
    # 而 join 方法 (method) 表示等待行程 (process) 執行結束。
    p1 = Process (target = download_task, args = ('Python.pdf', ))

    p1.start()
    p2 = Process (target = download_task, args = ('Hot.avi', ))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print('total %.2f s.' % (end - start))

if __name__ == '__main__':
    download_without_multiprocessing()
    download_with_multiprocessing()
