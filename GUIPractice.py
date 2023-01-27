import tkinter as tk
import os
import time

#Creates a GUI Window
window = tk.Tk()

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

