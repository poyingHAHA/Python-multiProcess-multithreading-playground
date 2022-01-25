import time
import tkinter
import tkinter.messagebox

'''
    如果不使用多線程 (Multithreading)，當點擊'下載'按鈕後整個程序的其他部分都被這個耗時間的任務阻塞而無法執行。
'''

def download():
    #模擬下載任務需要花費10s
    time.sleep(10)
    tkinter.messagebox.showinfo('提示', '下載完成')

def show_about():
    tkinter.messagebox.showinfo('關於', 'welcome')

def main():
    top = tkinter.Tk()
    top.title('單線程')  #視窗標題
    top.geometry('250x150')  #視窗大小
    top.wm_attributes('-topmost', True)  #視窗彈出至頂

    panel = tkinter.Frame(top)
    button1 = tkinter.Button(panel, text='download', command=download)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='about', command=show_about)
    button2.pack(side='right')
    panel.pack(side='bottom')

    tkinter.mainloop()


'''
    使用多線程 (Multithreading) 將耗時間的任務放到一個獨立的線程 (thread) 中執行，
    這樣就不會因為執行耗時間的任務而阻塞了主線程 (thread) 。
'''
from threading import Thread

def main_with_threading():
    class DowloadTaskHandler(Thread):
        
        def run(self):
            time.sleep(10)
            tkinter.messagebox.showinfo('Hint', 'Done')
            #啟用下載按鈕
            button1.config(state=tkinter.NORMAL)

    def download():
        #禁用下載按鈕
        button1.config(state=tkinter.DISABLED)
        # 透過daemon參數將線程(thread)設為守護線程(thread),
        # 主程式退出就不再保留執行
        # 在線程中處理耗時間的下載任務
        DowloadTaskHandler(daemon=True).start()

    def show_about():
        tkinter.messagebox.showinfo('About', 'welcome')

    top = tkinter.Tk()
    top.title('單線程')  #視窗標題
    top.geometry('250x150')  #視窗大小
    top.wm_attributes('-topmost', True)  #視窗彈出至頂

    panel = tkinter.Frame(top)
    button1 = tkinter.Button(panel, text='download', command=download)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='about', command=show_about)
    button2.pack(side='right')
    panel.pack(side='bottom')

    tkinter.mainloop()
        

if __name__=='__main__':
    main_with_threading()