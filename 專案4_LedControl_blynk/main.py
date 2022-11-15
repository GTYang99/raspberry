import tkinter as tk
# 引用這項功能的Class被移到tools.py去，因此會變暗色，表示main.py內容沒有使用到
# from PIL import Image,ImageTk
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import RPi.GPIO as GPIO
# 確認載入的模塊是使用物件導向或者是function導向寫的
from tools import LightButton

cred = credentials.Certificate("private/raspberry1-45ee2-firebase-adminsdk-5h0yc-acdceb5727.json")
firebase_admin.initialize_app(cred,{
    # 這邊databasURL的URL要大寫
    'databaseURL':'https://raspberry1-45ee2-default-rtdb.firebaseio.com/'
})
ref = db.reference('ledcontrol')
# print(ref)


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
            # GPIO BVM25設定為開啟時，給出高的電壓
            # self.btn.open()
            GPIO.output(25,GPIO.HIGH)
            # self.btn.config(image=self.close_photo)
            self.btn.light_state = True
        else:
            # self.btn.close()
            # GPIO BVM25設定為關閉時，給出低的電壓
            GPIO.output(25,GPIO.LOW)
            # self.btn.config(image=self.open_photo)
            self.btn.light_state = False

    def userClick(self):
        # 收集led的資料
        # print(ref.get())
        currentState = ref.get()['led']
        ref.update({'led':not currentState})
        if currentState:
            # self.btn.close()
            GPIO.output(25,GPIO.LOW)
            # self.btn.config(image=self.close_photo)
            self.btn.light_state = False
        else:
            # self.btn.open()
            GPIO.output(25,GPIO.HIGH)
            # self.btn.config(image=self.open_photo)
            self.btn.light_state = True

def main():
    # GPIO的基礎設定模式，
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(25,GPIO.OUT)
    windows = window()
    windows.mainloop()

if __name__ == "__main__":
    main()