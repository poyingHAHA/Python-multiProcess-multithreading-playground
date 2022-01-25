'''
    因為多個線程 (thread) 可以共享行程 (process) 的內存空間，
    因此要實現多個線程間的通訊相對簡單，最直接的辦法就是設置一個全域變數，
    多個線程共享這個全域變數即可。
    
    但當多個線程共享同一個變數（通常稱之為'資源'）時，
    很有可能產生不可控的結果從而導致程序失效甚至崩潰。

    下面的例子展示 100 個線程向同一個銀行帳戶轉賬（轉入 1 元錢）的場景。
    銀行帳戶是一個臨界資源，在沒有保護的情況下很有可能會得到錯誤的結果。
'''

from time import sleep
from threading import Thread, Lock

class Account(object):
    def __init__(self):
        self._balance = 0

    def deposit(self, money):
        new_balance = self._balance + money # 存款後餘額
        sleep(0.01)                         # 模擬受理存款需要 0.01 秒的時間
        self._balance = new_balance         # 修改帳戶餘額

    @property
    def balance(self):
        return self._balance

class AddMoneyThread(Thread):
    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.deposit(self._money)

def main():
    account = Account()
    threads = []
    # 創建100個存款的線程(thread)向同一個帳戶中存錢
    for _ in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()
    
    #等所有存款線程都執行完畢
    for t in threads:
        t.join()
    
    print(f"Balance: {account.balance}$")

# if __name__ == '__main__':
#     main()

'''
    運行上面的程式碼，100 個線程 (thread) 分別向帳戶中轉入 1 元錢，
    結果居然小於 100元。之所以出現這種情況是因為沒有對銀行帳戶這'臨界資源'加以保護，
    多個線程 (thread) 同時向帳戶中存錢時，會一起執行到 new_balance = self._balance + money 
    這行，多個線程 (thread) 得到的帳戶餘額都是初始狀態下的 0，所以都是 0 做了 +1 ，
    因此得到了錯誤的結果。
'''

'''
在這種情況下，可以透過'鎖'來保護'臨界資源'，只有獲得'鎖'的線程 (thread) 才能訪問'臨界資源'，
而其他沒有得到'鎖'的線程 (thread) 只能被阻塞起來，直到獲得鎖的線程 (thread) 釋放了'鎖'，
其他線程才有機會獲得'鎖'，進而訪問被保護的'臨界資源'。
下面的程式碼展示如何使用'鎖'來保護對銀行帳戶的操作，從而獲得正確的結果。
'''

class Account_with_lock(object):
    def __init__(self):
        self._balance = 0
        self._lock = Lock()

    def deposit(self, money):
        #先獲取鎖才能執行後續的程式碼
        self._lock.acquire()
        try:
            new_balance = self._balance + money
            sleep(0.01)
            self._balance = new_balance
        finally:
            #在 finally 中執行釋放鎖保證正常異常鎖都能釋放
            self._lock.release()

    @property
    def balance(self):
        return self._balance

def main2():
    account = Account_with_lock()
    threads = []
    for _ in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print(f'Total Balance: {account.balance}$')

if __name__ == "__main__":
    main2()