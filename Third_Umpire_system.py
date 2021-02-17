import tkinter
import cv2
import numpy as np
import PIL.Image, PIL.ImageTk
from functools import partial
import threading
import imutils
import time


stream = cv2.VideoCapture("clip.mp4")
flag = True
def play(speed):
    global flag
    print(f"You clicked on Play,Speed is {speed}")
    
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES,frame1 + speed)
    
    grabbed, frame = stream.read()
    if not grabbed:
        exit()
    
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT) 
    frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))    
    canvas.image = frame
    canvas.create_image(0, 0, image = frame, anchor = tkinter.NW)
    if flag:
      canvas.create_text(194, 24, fill = "black", font = "Times 27 bold", text= "Decision Pending...")
    flag = not flag
    
def pending(decision):
    frame = cv2.cvtColor(cv2.imread("pending.png"),cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height= SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image = frame, anchor = tkinter.NW)
    time.sleep(2)
    frame = cv2.cvtColor(cv2.imread("sponsor.png"),cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height= SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image = frame, anchor = tkinter.NW)
    time.sleep(2)
#     devfolio
# hackerearth    GFG
    if decision == 'out':
        decisionImg = 'out.png'
    else:
        decisionImg = 'not_out.png'
    frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
    frame = imutils.resize(frame, width=SET_WIDTH, height= SET_HEIGHT)
    canvas.image = frame
    canvas.create_image(0, 0, image = frame, anchor = tkinter.NW)

def out():
    thread = threading.Thread(target=pending, args=("out",))
    thread.daemon = 1
    thread.start()
    print("Player is OUT!")

def not_out():
    thread = threading.Thread(target=pending, args=("not out",))
    thread.daemon = 1
    thread.start()
    print("Player is NOT OUT!")
    
SET_WIDTH = 650
SET_HEIGHT = 368

window = tkinter.Tk()
window.title("@utkr.sh Third Umpire Decision Review Kit") 
cv_img = cv2.cvtColor(cv2.imread("3rd Umpire.png"), cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(window, width = SET_WIDTH, height = SET_HEIGHT)
photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0, 0, anchor = tkinter.NW, image = photo)
canvas.pack()

btn = tkinter.Button(window, text = "<< Previous (Fast)", width = 50, command = partial(play, -25))
btn.pack()

btn = tkinter.Button(window, text = "<< Previous (Slow)", width = 50, command = partial(play, -2))
btn.pack()

btn = tkinter.Button(window, text = " Next (Slow) >>", width = 50, command = partial(play, 2))
btn.pack()

btn = tkinter.Button(window, text = " Next (Fast) >>", width = 50, command = partial(play, 25))
btn.pack()

btn = tkinter.Button(window, text = "** OUT ** ", width = 50, command = out)
btn.pack()

btn = tkinter.Button(window, text = "** NOT OUT ** ", width = 50, command = not_out)
btn.pack()



window.mainloop()
