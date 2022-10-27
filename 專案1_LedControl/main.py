import tkinter as tk
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("private/raspberry1-45ee2-firebase-adminsdk-5h0yc-149b6394cf.json")
firebase_admin.initialize_app(cred,{
    # 這邊databasURL的URL要大寫
    'databaseURL':'https://raspberry1-45ee2-default-rtdb.firebaseio.com/'
})
ref = db.reference('ledcontrol')

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        #建立title
        self.title("LED Controller")
        #建立按鈕
        # btn = tk.Button(self,text="開關",padx=50,pady=30,font=('arial',18),command=self.userClick)
        # btn.pack(padx=50,pady=30)
        self.btn = tk.Button(self,text="開關",padx=50,pady=30,font=('arial',18),command=self.userClick)
        self.btn.pack(padx=50,pady=30)
        currentState = led.get()['led']
        if currentState:
            self.btn.config(text="關")
        else:
            self.btn.config(text="開")

    def userClick(self):
        # print("user click")
        # print(ref.get())
        currentState = ref.get()['led']
        ref.update({'led':not currentState})
        if currentState:
            self.btn.config(text="開")
        else:
            self.btn.config(text="關")

def main():
    pass

if __name__ == "__main__":
    main()