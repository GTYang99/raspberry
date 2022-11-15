# 創建Python Tkinter 畫布（Canvas）
import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        # 建立一個tk功能中的Canvas
        canvas1 = tk.Canvas(self,width=400,height=250,background='#BF6766')
        # 線條是利用座標格式去畫
        # 創建圓形
        canvas1.create_oval(10,10,80,80,outline='#000')
        # 創建橢圓形
        canvas1.create_oval(110,10,300,80,outline='#000')
        # 創建座標點
        points = [150, 100, 200, 120, 240, 180, 210, 200, 150, 150, 100, 200]
        # 創建多邊形
        canvas1.create_polygon(points,outline='#000',fill='#ff1')
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