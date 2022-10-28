# 創建Python Tkinter 畫布（Canvas）
import tkinter as tk
from PIL import Image,ImageTk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        # 畫圖片
        # 建立開燈的圖片
        image  = Image.open("light_open.png")
        self.lightImage = ImageTk.PhotoImage(image)
        print(image.size)
        canvas = tk.Canvas(self,width=image.size[0]+20,height=image.size[1]+20)
        canvas.create_image(10,10,anchor=tk.NW,image=self.lightImage)
        # 關閉開燈的圖片(畫布清除)
        canvas.delete("all")
        # 建立關燈的圖片
        image1  = Image.open("light_close.png")
        self.lightImage1 = ImageTk.PhotoImage(image1)
        canvas.create_image(10,10,anchor=tk.NW,image=self.lightImage1)
        # tk的YES就是true
        canvas.pack()

def main():
    window = Window()
    window.title('Canvas')
    window.geometry('400x250+300+200')
    # 不知道為何不用給mainloop，也能執行
    window.mainloop()


if __name__ == '__main__':
    main()