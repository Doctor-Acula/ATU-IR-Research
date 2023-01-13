import tkinter as tk
import os

#Creates a GUI Window
window = tk.Tk()

#Creates a Widget
label1 = tk.Label(text="IR Camera")
label1.pack()

#Creates a functioning button
button1 = tk.Button(
    text='Press to start',
    width=25,
    height=5,
    bg="black",
    fg="Red",
)
button1.pack()

#Detects when button is pressed
def button1_detection():
    global buttonClicked 
    buttonClicked = not buttonClicked
buttonClicked = True #This may be backwards... Just work with it for now

'''def button1_pressed():
    if buttonClicked == True:
        print("Button Pressed")
        label1.config(text="Button Pressed")
    else:
        print("Button Not Pressed")
        label1.config(text="Button Not Pressed")
button1.config(command=button1_pressed)'''

def button1_pressed():
    if buttonClicked == True:
        print("Button Pressed")
        os.system('GUIOutput.py')
    else:
        print("Button Not Pressed")
button1.config(command=button1_pressed)


window.mainloop()

