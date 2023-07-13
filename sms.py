from tkinter import *
import time
import ttkthemes

#functionality part
count = 0
txt = ''

def slider():
    global text, count
    if count == len(slide):
        count = 0
        text=''
    txt = txt + slide[count]
    sliderLabel.config(text=txt)
    count += 1
    sliderLabel.after(300,slider)

def clock():
    date = time.strftime('%d/%m/%Y')
    currentTime = time.strftime('%H:%M:%S')
    datetimeLabel.config(text=f'   Date: {date}\nTime: {currentTime}')
    datetimeLabel.after(1000, clock)

#Gui part
root=Tk()

root.geometry('1174x680+50+20')

root.title('Main page')
root.resizable(False, False)

datetimeLabel = Label(root,font=('times new roman',18,'bold'))
datetimeLabel.place(x=5,y=5)
clock()

slide = 'RA4 Gas Concept'
sliderLabel = Label(root,font=('aerial',18,'italic bold'),width=50)
sliderLabel.place(x=200,y=0)
slider()

connectButton = Button(root,text='Connect database')
connectButton.place(x=980,y=0)


root.mainloop()