from tkinter import *
from PIL import ImageTk

window = Tk()

window.geometry('1280x700+0+0')

window.resizable(False, False)

backgroundImage = ImageTk.PhotoImage(file='images/keyboard.jpg')

bgLabel = Label(window, image=backgroundImage)

bgLabel.place(x=50, y=50)

loginFrame = Frame(window)
loginFrame.place(x=400, y=150)

logoImage = PhotoImage(file=)

window.mainloop()