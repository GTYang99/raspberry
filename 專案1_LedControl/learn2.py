# 創建Python Tkinter 畫布（Canvas）
import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        # 建立一個tk功能中的Canvas
        canvas1 = tk.Canvas(self,width=400,height=250,background='#BF6766')
        # 線條是利用座標格式去畫
        # 創建一條橫實線
        # canvas1.create_line(15,30,200,30)
        # 創建一條直虛線
        # canvas1.create_line(300,35,300,200,dash=(4,2))
        # 創建一個三角形
        # canvas1.create_line(55, 85, 155,85,105,180,55, 85,fill="#FFBA84")
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