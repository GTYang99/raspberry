import tkinter as tk
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("private/raspberry1-45ee2-firebase-adminsdk-5h0yc-149b6394cf.json")
firebase_admin.initialize_app(cred,{
    # 這邊databasURL的URL要大寫
    'databaseURL':'https://raspberry1-45ee2-default-rtdb.firebaseio.com/'
})
ref = db.reference('ledControl/led')

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        #建立title
        self.title("LED Controller")
        #建立按鈕
        btn = tk.Button(self,text="開關",padx=50,pady=30,font=('arial',18),command=self.userClick)
        btn.pack(padx=50,pady=30)

    def userClick(self):
        # print("user click")
        print(ref.get())

def main():
    pass

if __name__ == "__main__":
    main()