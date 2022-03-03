import time
from playsound import playsound
from tkinter import *
import datetime

root = Tk()
root.title('timer')
dwell_time = dict()
dtime = dict()

def update_time():
    dtime1 = datetime.datetime.now()
    dwell_time1 = 0
    curr_time = datetime.datetime.now()
    old_time = dtime1
    time_diff = curr_time - old_time
    dtime1 = datetime.datetime.now()
    sec = time_diff.total_seconds()
    dwell_time1 += sec
    string = countdown(t)
    l.config(text=string)
    l.after(1000,update_time)

def countdown(t):
    for i in range(t):
        print(str(t - i) + " seconds remaining")
        # str(t - i)
        time.sleep(1)

t = int(15)
# countdown(int(t))
print("Sound the siren")
# playsound('play.mp3')
l = Label(root,font=('calibri', 50, 'bold'), background='blue', foreground='white')
l.pack(anchor='center')
update_time()
mainloop()