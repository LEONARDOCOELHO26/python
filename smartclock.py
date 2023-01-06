import sys 
from tkinter import *   
import time

def DClock():
    curr_time= time.strftime("%H:%M:%S")
    clock.config(text=curr_time)
    clock.after(100,DClock)
window=Tk()
window.title('Digital Clock') 
message= Label(window, font=("display",150,"bold"), text="Time", fg="black")
message.grid(row=0,column=0)
clock= Label(window, font=("display",150,"bold"),fg="lightblue" ,bg="black")
clock.grid(row=1,column=0)
DClock()
mainloop() 