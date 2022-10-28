# 創建Python Tkinter 畫布（Canvas）
import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        # 建立一個tk功能中的Canvas
        canvas1 = tk.Canvas(self,width=400,height=250,background='#BF6766')
        # 線條是利用座標格式去畫
        # 創建長方形方法
        canvas1.create_rectangle(30,10,120,80,outline='#000')
        canvas1.create_rectangle(150, 10, 240, 80, outline="#000", fill="#f50")
        canvas1.create_rectangle(270, 10, 370, 80, outline="#000", fill="#05f")
        # 創建曲線方法
        canvas1.create_arc(1,1,10,10)
        # tk的YES就是true
        canvas1.pack(fill=tk.BOTH,expand=tk.YES)

def main():
    window = Window()
    window.title('Canvas')
    window.geometry('400x250+300+200')
    # 不知道為何不用給mainloop，也能執行
    window.mainloop()


if __name__ == '__main__':
    main()