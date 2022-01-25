from time import time

def main():
    total = 0
    number_list = [x for x in range(1, 100000001)]
    start = time()
    for number in number_list:
        total+=number
    print(total)
    end = time()
    print('Execution time: %.3fs' % (end - start))

'''
    with multiprocessing
'''
from multiprocessing import Process, Queue
from random import randint
from time import time

def task_handler(curr_list, result_queue):
    total = 0
    for number in curr_list:
        total+=number
    result_queue.put(total)

def main_with_process():
    processes = []
    number_list = [x for x in range(1, 100000001)]
    result_queue = Queue()
    index = 0
    #啟動8個行程(process)將數據切片後進行運算
    for _ in range(4):
        p = Process(target = task_handler, args = (number_list[index:index+25000000], result_queue))
        index += 25000000
        processes.append(p)
        p.start()
    
    #開始記錄所有行程(process)執行完成花費的時間
    start = time()
    for p in processes:
        p.join()

    #執行結果
    total = 0
    while not result_queue.empty():
        total+=result_queue.get()
    print(total)
    end = time()
    print('Execution time: ',(end-start), 's', sep='')

if __name__ == '__main__':
    main_with_process()