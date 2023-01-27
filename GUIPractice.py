import tkinter as tk
import os
import time
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
from pygame import mixer

#Creates a GUI Window
window = tk.Tk()

w = 400 # width for the Tk root
h = 200 # height for the Tk root

# get screen width and height
ws = window.winfo_screenwidth() # width of the screen
hs = window.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# set the dimensions of the screen 
# and where it is placed
window.geometry('%dx%d+%d+%d' % (w, h, x, y))

#Creates a Widget
label1 = tk.Label(text="IR Camera")
label1.pack()

#Creates a functioning button
button1 = tk.Button(
    text='Access Main Security Grid',
    width=35,
    height=2,
    bg="black",
    fg="Red",
)
button1.pack()

#Detects when button is pressed
def button1_detection():
    global buttonClicked 
    buttonClicked = not buttonClicked
buttonClicked = True #This may be backwards... Just work with it for now

def button1_pressed():
    if buttonClicked == True:
        os.system('xdg-open nedry.mp3 &')
        time.sleep(0.5)
        os.system('python GUIOutput.py &')
        for i in range(0,30):
            print("YOU DIDN'T SAY THE MAGIC WORD!")
            time.sleep(0.5)
    else:
        print("Button Not Pressed")
button1.config(command=button1_pressed)

#Creates another functioning button
button2 = tk.Button(
    text='Initiate Thermal Camera',
    width=30,
    height=7,
    bg="black",
    fg="Red",
)
button2.pack()

#Detects when button is pressed
def button2_detection():
    global button2Clicked 
    button2Clicked = not button2Clicked
button2Clicked = True #This may be backwards... Just work with it for now

def button2_pressed():
    if button2Clicked == True:
        print("Button Pressed")
        os.system('python pedrotest.py')
    else:
        print("Button Not Pressed")
button2.config(command=button2_pressed)


window.mainloop()
