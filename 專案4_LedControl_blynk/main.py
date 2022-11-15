import tkinter as tk
# 引用這項功能的Class被移到tools.py去，因此會變暗色，表示main.py內容沒有使用到
from PIL import Image,ImageTk
import RPi.GPIO as GPIO
# 確認載入的模塊是使用物件導向或者是function導向寫的
from tools import LightButton

BLYNK_AUTH_TOKEN = '0wdpF3047cAv4kU738sPvpPlBmCyVtR_'

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
        
    def open(self):
        self.config(image=self.open_photo)
        
    def close(self):
        self.config(image=self.close_photo)
    


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
        self.btn = LightButton(self,padx=50,pady=30)
        self.btn.pack(padx=50,pady=30)
        # self.btn.open()
        self.repeat_run()

    def delete_delay(self):
        # 設置清除GPIO接口電源
        GPIO.cleanup()
        self.after_cancel(self.windows_id)
        self.destroy()

    def repeat_run(self):
        print('run')
        self.windows_id = self.after(1000,self.repeat_run)
        # 建立讀取數據庫的資料，改變開關字樣
        '''
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
        '''
def main():
    # GPIO的基礎設定模式，
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(25,GPIO.OUT)
    windows = window()
    # 呼叫協議，清除GPIO接口電源
    windows.protocol("WM_DELETE_WINDOW",windows.delete_delay)
    windows.mainloop()

if __name__ == "__main__":
    main()