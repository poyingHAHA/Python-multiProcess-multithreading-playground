
import os
from multiprocessing import Process
import multiprocessing as mp
'''
    子進程要執行的code
    注意: 使用windows系統沒辦法直接print出來
'''
def run_proc(arr, name):
    print(f'Run child process {name} ({os.getpid()})')
    arr.append(1)
    return

if __name__ == '__main__':
    arr = []
    print(f"Parent process {os.getpid()}.")
    p = Process(target=run_proc, args=(arr,'test_code'))
    print('Child process will start.')
    p.start()
    print(arr)
    p.join()
    print(arr)
    print('Child process end.')
