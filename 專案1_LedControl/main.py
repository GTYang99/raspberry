import tkinter as tk
from PIL import Image,ImageTk
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("private/raspberry1-45ee2-firebase-adminsdk-5h0yc-149b6394cf.json")
firebase_admin.initialize_app(cred,{
    # 這邊databasURL的URL要大寫
    'databaseURL':'https://raspberry1-45ee2-default-rtdb.firebaseio.com/'
})
ref = db.reference('ledcontrol')
# print(ref)

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

    def open(self):
        self.config(image=self.open_photo)
        self.config(text="關")

    def close(self):
        self.config(image=self.close_photo)
        self.config(text="開")

class window(tk.Tk):
    def __init__(self):
        super().__init__()
        # 建立title
        self.title('LED Controller')
        # 建立圖片
        # close_image = Image.open('light_close.png')
        # self.close_photo = ImageTk.PhotoImage(close_image)
        # self.btn = tk.Button(self,image=self.close_photo,padx=50,pady=30,font=('arial',18),command=self.userClick)

        # open_image = Image.open('light_open.png')
        # self.open_photo = ImageTk.PhotoImage(open_image)
        # self.btn = tk.Button(self,image=self.open_photo,padx=50,pady=30,font=('arial',18),command=self.userClick)

        # 建立按鈕
        # self.btn = tk.Button(self,text='開關',padx=50,pady=30,font=('arial',18),command=self.userClick)
        self.btn = LightButton(self,padx=50,pady=30,command=self.userClick)
        self.btn.pack(padx=50,pady=30)
        # 建立讀取數據庫的資料，改變開關字樣
        currentState = ref.get()['led']
        if currentState:
            self.btn.open()
            # self.btn.config(image=self.close_photo)
        else:
            self.btn.close()
            # self.btn.config(image=self.open_photo)

    def userClick(self):
        # 收集led的資料
        # print(ref.get())
        currentState = ref.get()['led']
        ref.update({'led':not currentState})
        if currentState:
            self.btn.close()
            # self.btn.config(image=self.close_photo)
        else:
            self.btn.open()
            # self.btn.config(image=self.open_photo)

def main():
    windows = window()
    windows.mainloop()

if __name__ == "__main__":
    main()