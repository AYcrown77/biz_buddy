from tkinter import *
import time
import ttkthemes
from tkinter import ttk,messagebox,filedialog
import sqlite3
import pandas

#functionality part
count = 0
txt = ''
date = time.strftime('%d/%m/%Y')
nameField = ['expId','reason','amount','date']

con = sqlite3.connect('alan_pharm_supermarket.db')
myCursor = con.cursor()
query = 'CREATE TABLE IF NOT EXISTS expenses (\
            expId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,\
            reason VARCHAR(100) NOT NULL,\
            amount FLOAT NOT NULL,\
            date DATE NOT NULL)'
myCursor.execute(query)

#con.commit()
#con.close()

def toplevel_data(title,button_text,command):
    global expId,reasonEntry,amountEntry,dateEntry,entryWindow,indexing
    
    if title == 'Update Expenses':
        indexing = expensesTable.focus()
        if indexing:
            entryWindow = Toplevel()
            entryWindow.title(title)
            entryWindow.grab_set()
            entryWindow.resizable(False,False)
        
            reasonLabel = Label(entryWindow,text='Reason',font=('times new roman',20,'bold'))
            reasonLabel.grid(row=0,column=0,padx=30,pady=15,sticky=W)
            reasonEntry = Entry(entryWindow,font=('roman',15,'bold'))
            reasonEntry.grid(row=0,column=1,pady=15,padx=10)

            amountLabel = Label(entryWindow,text='Amount',font=('times new roman',20,'bold'))
            amountLabel.grid(row=1,column=0,padx=30,pady=15,sticky=W)
            amountEntry = Entry(entryWindow,font=('roman',15,'bold'))
            amountEntry.grid(row=1,column=1,pady=15,padx=10)

            #dateLabel = Label(entryWindow,text='Date',font=('times new roman',20,'bold'))
            #dateLabel.grid(row=2,column=0,padx=30,pady=15,sticky=W)
            #dateEntry = Entry(entryWindow,font=('roman',15,'bold'))
            #dateEntry.grid(row=2,column=1,pady=15,padx=10)

            expButton = ttk.Button(entryWindow,text=button_text,command=command)
            expButton.grid(row=6,columnspan=2,pady=10)

            content = expensesTable.item(indexing)
            listData = content['values']
            expId = listData[0]
            reasonEntry.insert(0,listData[1])
            amountEntry.insert(0,listData[2])
            date = listData[3]
        else:
            messagebox.showerror('Error', f'No data selected')
            return

    if title != 'Update Expenses':
        entryWindow = Toplevel()
        entryWindow.title(title)
        entryWindow.grab_set()
        entryWindow.resizable(False,False)

        reasonLabel = Label(entryWindow,text='Reason',font=('times new roman',20,'bold'))
        reasonLabel.grid(row=0,column=0,padx=30,pady=15,sticky=W)
        reasonEntry = Entry(entryWindow,font=('roman',15,'bold'))
        reasonEntry.grid(row=0,column=1,pady=15,padx=10)

        amountLabel = Label(entryWindow,text='Amount',font=('times new roman',20,'bold'))
        amountLabel.grid(row=1,column=0,padx=30,pady=15,sticky=W)
        amountEntry = Entry(entryWindow,font=('roman',15,'bold'))
        amountEntry.grid(row=1,column=1,pady=15,padx=10)

        dateLabel = Label(entryWindow,text='Date',font=('times new roman',20,'bold'))
        dateLabel.grid(row=2,column=0,padx=30,pady=15,sticky=W)
        dateEntry = Entry(entryWindow,font=('roman',15,'bold'))
        dateEntry.grid(row=2,column=1,pady=15,padx=10)

        expButton = ttk.Button(entryWindow,text=button_text,command=command)
        expButton.grid(row=6,columnspan=2,pady=10)

def add_data():
    if reasonEntry.get()=='' or amountEntry.get()=='': #or dateEntry.get()=='':
        messagebox.showerror('Error','All fields are required',parent=entryWindow)
    else:
        try:
            query = 'SELECT MAX(expId) FROM expenses'
            myCursor.execute(query)
            max_id = myCursor.fetchone()[0]
            new_expenses_id = max_id + 1 if max_id else 1
            query = 'INSERT into expenses (expId,reason,amount,date) VALUES (?,?,?,?)'
            myCursor.execute(query,(new_expenses_id,reasonEntry.get(),amountEntry.get(),date))
            con.commit()
            result = messagebox.askyesno('Confirm','Data added successfully. Do you want to clean the form?')
            if result:
                reasonEntry.delete(0, END)
                amountEntry.delete(0, END)
                #dateEntry.delete(0, END)
            else:
                pass
        except:
            messagebox.showerror('Error','An error occurred while adding data',parent=entryWindow)
            return
        show_data()
            
def search_data():
    query = 'SELECT * FROM expenses WHERE reason=? or amount=? or date=?'
    myCursor.execute(query,(reasonEntry.get(),amountEntry.get(),date))
    expensesTable.delete(*expensesTable.get_children())
    fetchedData = myCursor.fetchall()
    if not fetchedData:
        messagebox.showerror('Error', f'No match')
    for data in fetchedData:
        expensesTable.insert('',END,values=data)

def delete_data():
    result = messagebox.askyesno('Confirm','Do you want to delete?')
    if result:
        try:
            indexing = expensesTable.focus()
            content = expensesTable.item(indexing)
            contentId = content['values'][0]
            contentIdInt = int(contentId)
            query = 'DELETE FROM expenses WHERE expId = ?'
            myCursor.execute(query,(contentIdInt,))
            con.commit()
            messagebox.showinfo('Deleted',f'The expenses with expenses Id {contentIdInt} is deleted succesfully')
            query = 'SELECT * FROM expenses'
            myCursor.execute(query)
            fetchedData = myCursor.fetchall()
            expensesTable.delete(*expensesTable.get_children())
            for data in fetchedData:
                expensesTable.insert('',END,values=data)
        except Exception as e:
            messagebox.showerror('Error', f'No expenses selected')
    else:
        pass

def show_data():
    query = 'SELECT * FROM expenses'
    myCursor.execute(query)
    fetchedData = myCursor.fetchall()
    expensesTable.delete(*expensesTable.get_children())
    for data in fetchedData:
        expensesTable.insert('',END,values=data)

def update_data():
    query = 'UPDATE expenses SET reason=?,amount=?,date=? where expId=?'
    myCursor.execute(query,(reasonEntry.get(),amountEntry.get(),date,expId))
    con.commit()
    messagebox.showinfo('Success',f'Expenses is modified successfully',parent=entryWindow)
    entryWindow.destroy()
    show_data()

def export_data():
    url = filedialog.asksaveasfilename(defaultextension='.csv')
    indexing = expensesTable.get_children()
    newList = []
    for index in indexing:
        content = expensesTable.item(index)
        dataList = content['values']
        newList.append(dataList)
    table = pandas.DataFrame(newList,columns=['Id','Reason','Amount','Date'])
    table.to_csv(url,index=False)
    messagebox.showinfo('Success','Data saved successfully')

def to_exit():
    result = messagebox.askyesno('Confirm','Do you want to exit?')
    if result:
        root.destroy()
    else:
        pass

def back():
    root.destroy()
    import main_page

def slider():
    global txt, count
    if count == len(slide):
        count = 0
        txt = ''
    txt = txt + slide[count]
    sliderLabel.config(text=txt)
    count += 1
    sliderLabel.after(300,slider)

def clock():
    global date,currentTime
    date = time.strftime('%d/%m/%Y')
    currentTime = time.strftime('%H:%M:%S')
    datetimeLabel.config(text=f'   Date: {date}\nTime: {currentTime}')
    datetimeLabel.after(1000, clock)

#Gui part
root = Toplevel()
#root.get_themes()
#root.set_theme('radiance')

root.geometry('1174x700+0+0')
root.title('Expenses')
#root.resizable(False,False)

datetimeLabel = Label(root,font=('times new roman',18,'bold'))
datetimeLabel.place(x=5,y=5)
clock()

slide = 'Alan Pharmacy and Supermarket'
sliderLabel = Label(root,font=('aerial',18,'italic bold'),width=50)
sliderLabel.place(x=200,y=0)
slider()

#connectButton = ttk.Button(root,text='Connect database',command=connect_database)
#connectButton.place(x=980,y=0)

leftFrame = Frame(root)
leftFrame.place(x=50,y=80,width=300,height=600)

logoImage = PhotoImage(file='images/work.png')
logoLabel = Label(leftFrame,image=logoImage)
logoLabel.grid(row=0,column=0)
 
addexpButton = ttk.Button(leftFrame,text='Add Expenses',width=20,command=lambda :toplevel_data('Add Expenses','Add Expenses',add_data))
addexpButton.grid(row=1,column=0,pady=10)

searchexpButton = ttk.Button(leftFrame,text='Search Expenses',width=20,command=lambda :toplevel_data('Search Expenses','Search Expenses',search_data))
searchexpButton.grid(row=2,column=0,pady=10)

updateexpButton = ttk.Button(leftFrame,text='Update Expenses',width=20,command=lambda :toplevel_data('Update Expenses','Update Expenses',update_data))
updateexpButton.grid(row=3,column=0,pady=10)

showexpButton = ttk.Button(leftFrame,text='Show Expenses',width=20,command=show_data)
showexpButton.grid(row=4,column=0,pady=10)

exportDataButton = ttk.Button(leftFrame,text='Export data',width=20,command=export_data)
exportDataButton.grid(row=5,column=0,pady=10)

deleteexpButton = ttk.Button(leftFrame,text='Delete Expenses',width=20,command=delete_data)
deleteexpButton.grid(row=6,column=0,pady=10)

exitButton = ttk.Button(leftFrame,text='Exit',width=20,command=to_exit)
exitButton.grid(row=7,column=0,pady=10)

backButton = ttk.Button(leftFrame,text='Back',width=20,command=back)
backButton.grid(row=8,column=0,pady=10)

rightFrame = Frame(root)
rightFrame.place(x=350,y=80,width=1000,height=600)

scrollBarX = Scrollbar(rightFrame,orient=HORIZONTAL)
scrollBarY = Scrollbar(rightFrame,orient=VERTICAL)

expensesTable = ttk.Treeview(rightFrame,columns=('expId','reason','amount','date'),
                    xscrollcommand=scrollBarX.set,yscrollcommand=scrollBarY.set)

scrollBarX.config(command=expensesTable.xview)
scrollBarY.config(command=expensesTable.yview)

scrollBarX.pack(side=BOTTOM,fill=X)
scrollBarY.pack(side=RIGHT,fill=Y)

expensesTable.pack(fill=BOTH,expand=1)

for i in range(0, len(nameField)):
    expensesTable.heading(nameField[i],text=nameField[i])
expensesTable.config(show='headings')

expensesTable.column('expId',width=50,anchor=CENTER)
expensesTable.column('reason',width=500,anchor=CENTER)
expensesTable.column('amount',width=100,anchor=CENTER)
expensesTable.column('date',width=50,anchor=CENTER)

style = ttk.Style()
style.configure('Treeview',rowheight=25,font=('arial',12,'bold'),
                foreground='green',background='black',fieldbackground='green')
style.configure('Treeview.Heading',font=('arial',14,'bold'),foreground='green')

root.mainloop()