
import tkinter as tk
from PIL import Image,ImageTk

class LightButton(tk.Button):
    def __init__(self,parent,**kwargs):
        super().__init__(parent,**kwargs)
        #建立圖片
        ##建立close的圖片
        close_image = Image.open('light_close.png')
        self.close_photo = ImageTk.PhotoImage(close_image)
        ##建立open的圖片
        open_image = Image.open('light_open.png')
        self.open_photo = ImageTk.PhotoImage(open_image)
        self.config(borderwidth=0)
        self.config(font=('arial',18))
        # 把圖片原始定義為靠左邊
        self.config(compound=tk.LEFT)
        self.__light_state = None

    # 開關內容(open、close)修改為封裝的值(light_state)，建立一個屬性(light_state)與setter(重新設置)來調整
    # def open(self):
    #     self.config(image=self.open_photo)
    #     self.config(text="關")

    # def close(self):
    #     self.config(image=self.close_photo)
    #     self.config(text="開")

    @property
    def light_state(self):
        return self.__state

    @light_state.setter
    def light_state(self,s):
        self.__light_state = s
        if s == True:            
            self.config(image=self.open_photo)
            self.config(text="關")
        else:
            self.config(image=self.close_photo);
            self.config(text="開")  