import tkinter as tk
from PIL import Image,ImageTk
import firebase_admin
import RPi.GPIO as GPIO
from firebase_admin import credentials
from firebase_admin import db

# cred = credentials.Certificate("private/raspberry1-45ee2-firebase-adminsdk-5h0yc-149b6394cf.json")
# firebase_admin.initialize_app(cred,{
#     # 這邊databasURL的URL要大寫
#     'databaseURL':'https://raspberry1-45ee2-default-rtdb.firebaseio.com/'
# })

# led = db.reference('ledcontrol')
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
        self.config(state="disabled")
        # self.config(font=('arial',18))
        # self.config(compound=tk.LEFT)
    def open(self):
        self.config(image=self.open_photo)
        # self.config(text="關")
    def close(self):
        self.config(image=self.close_photo);
        # self.config(text="開")  
class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        #建立firebase 連線
        cred = credentials.Certificate("private/raspberry1-45ee2-firebase-adminsdk-5h0yc-149b6394cf.json")
        firebase_admin.initialize_app(cred,{
            'databaseURL': 'https://raspberry1-45ee2-default-rtdb.firebaseio.com/'
        })

        led = db.reference('ledcontrol')
        # #註冊監聽
        # led.listen(self.firebaseDataChange)

        #建立title
        self.title("LED Controller")
        #建立按鈕
        # self.btn = LightButton(self,padx=50,pady=30,command=self.userClick)
        self.btn = LightButton(self,padx=50,pady=30)
        self.btn.pack(padx=50,pady=30)
        currentState = led.get()['led']
        if currentState:
            self.btn.open()
            GPIO.output(25,GPIO.HIGH)
        else:
            self.btn.close()
            GPIO.output(25,GPIO.LOW)
        #註冊監聽
        led.listen(self.firebaseDataChange)

    # def userClick(self):
    #     currentState = led.get()['led']
    #     led.update({'led':not currentState})
    #     if currentState:
    #        self.btn.close()
    #        GPIO.output(25,GPIO.LOW)
    #     else:
    #        self.btn.open()
    #        GPIO.output(25,GPIO.HIGH)
    def firebaseDataChange(self,event):
        print("內容被更改")
        print(f"資料內容:{event.data}")
        print(f"資料路徑:{event.path}")
        if event.path == "/":
            state = event.data['led']
        elif event.path ==  "/led":
            state = event.data

        if state:
            self.btn.open()
            GPIO.output(25,GPIO.HIGH)
        else:
            self.btn.close()
            GPIO.output(25,GPIO.LOW)


def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(25,GPIO.OUT)
    window = Window()
    window.mainloop()

if __name__ == "__main__":
    main()