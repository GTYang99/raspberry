import tkinter as tk
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from PIL import Image,ImageTk

cred = credentials.Certificate("private/raspberry1-45ee2-firebase-adminsdk-5h0yc-149b6394cf.json")
firebase_admin.initialize_app(cred,{
    # 這邊databasURL的URL要大寫
    'databaseURL':'https://raspberry1-45ee2-default-rtdb.firebaseio.com/'
})
ref = db.reference('ledcontrol')

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

    def open(self):
        self.config(image=self.open_photo)

    def close(self):
        self.config(image=self.close_photo);   


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        #建立title
        self.title("LED Controller")
        #建立按鈕
        self.btn = LightButton(self,padx=50,pady=30,font=('arial',18),command=self.userClick)
        # btn = tk.Button(self,text="開關",padx=50,pady=30,font=('arial',18),command=self.userClick)
        # btn.pack(padx=50,pady=30)
        # self.btn = tk.Button(self,text="開關",padx=50,pady=30,font=('arial',18),command=self.userClick)
        # 建立圖片
        close_image = Image.open('light_close.png')
        self.close_photo = ImageTk.PhotoImage(close_image)
        open_image = Image.open('light_open.png')
        self.open_photo = ImageTk.PhotoImage(open_image)
        self.btn = tk.Button(self,image=self.close_photo,padx=50,pady=30,font=('arial',18),command=self.userClick)
        self.btn.pack(padx=50,pady=30)
        currentState = ref.get()['led']
        if currentState:
            self.btn.close()
        else:
            self.btn.open()

    def userClick(self):
        # print("user click")
        # print(ref.get())
        currentState = ref.get()['led']
        ref.update({'led':not currentState})
        if currentState:
            self.btn.open()
        else:
            self.btn.close()
def main():
    pass

if __name__ == "__main__":
    main()