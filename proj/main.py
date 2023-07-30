from tkinter import *
from tkinter import messagebox
import time,sys
from pygame import mixer
#from PIL import Image,ImageTk

def alarm():
    alarm_time=user.get()
    if alarm_time=="":
        messagebox.askretrycancel("error messae","please enter value")
    else:
        while True:
            time.sleep(1)
            if (alarm_time==time.strftime("%H:%M")):
                playmusic()
def playmusic():
    mixer.init()
    mixer.music.load('Bones.mp3')
    mixer.music.play()
    while mixer.music.get_busy():
        time.sleep(30)
        mixer.music.stop()
        sys.exit()

root=Tk()
root.title("alarm")
root.geometry("600x380")
canvas=Canvas(root,width=600,height=380)
#image=ImageTk.PhotoImage(Image.open("bgimg.jpg"))
#canvas.create_image(0,0,anchor=NW,image=image)
canvas.pack()
header=Frame(root)

box1=Frame(root)
box1.place(x=200,y=150)
box2=Frame(root)
box2.place(x=250,y=260)
user=Entry(box1,font=('Arial Narrow',20),width=18)
user.grid(row=10,column=20)
start_button=Button(box2,text="set alarm",font=('Arail Narrow',16,'bold'),command=alarm)
start_button.grid(row=10,column=2)
root.mainloop()