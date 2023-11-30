from tkinter import *
import time
import ttkthemes
from tkinter import ttk,messagebox,filedialog
import sqlite3
import pandas

#functionality part
count = 0
txt = ''

nameField = ['supId','supName','phoneNo','address']

con = sqlite3.connect('alan_pharm_supermarket.db')
myCursor = con.cursor()
query = 'CREATE TABLE IF NOT EXISTS supplier (\
            supId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,\
            supName VARCHAR(50) NOT NULL,\
            phoneNo INTEGER NOT NULL,\
            address VARCHAR(100) NOT NULL)'
myCursor.execute(query)

#con.commit()
#con.close()

def toplevel_data(title,button_text,command):
    global supId,supNameEntry,phoneNoEntry,addressEntry,entryWindow,indexing
    
    if title == 'Update Supplier':
        indexing = supplierTable.focus()
        if indexing:
            entryWindow = Toplevel()
            entryWindow.title(title)
            entryWindow.grab_set()
            entryWindow.resizable(False,False)
        
            supNameLabel = Label(entryWindow,text='Name',font=('times new roman',20,'bold'))
            supNameLabel.grid(row=0,column=0,padx=30,pady=15,sticky=W)
            supNameEntry = Entry(entryWindow,font=('roman',15,'bold'))
            supNameEntry.grid(row=0,column=1,pady=15,padx=10)

            phoneNoLabel = Label(entryWindow,text='Phone No',font=('times new roman',20,'bold'))
            phoneNoLabel.grid(row=1,column=0,padx=30,pady=15,sticky=W)
            phoneNoEntry = Entry(entryWindow,font=('roman',15,'bold'))
            phoneNoEntry.grid(row=1,column=1,pady=15,padx=10)

            addressLabel = Label(entryWindow,text='Address',font=('times new roman',20,'bold'))
            addressLabel.grid(row=2,column=0,padx=30,pady=15,sticky=W)
            addressEntry = Entry(entryWindow,font=('roman',15,'bold'))
            addressEntry.grid(row=2,column=1,pady=15,padx=10)

            supButton = ttk.Button(entryWindow,text=button_text,command=command)
            supButton.grid(row=6,columnspan=2,pady=10)

            content = supplierTable.item(indexing)
            listData = content['values']
            supId = listData[0]
            supNameEntry.insert(0,listData[1])
            phoneNoEntry.insert(0,listData[2])
            addressEntry.insert(0,listData[3])
        else:
            messagebox.showerror('Error', f'No supplier selected')
            return

    if title != 'Update Supplier':
        entryWindow = Toplevel()
        entryWindow.title(title)
        entryWindow.grab_set()
        entryWindow.resizable(False,False)

        supNameLabel = Label(entryWindow,text='Name',font=('times new roman',20,'bold'))
        supNameLabel.grid(row=0,column=0,padx=30,pady=15,sticky=W)
        supNameEntry = Entry(entryWindow,font=('roman',15,'bold'))
        supNameEntry.grid(row=0,column=1,pady=15,padx=10)

        phoneNoLabel = Label(entryWindow,text='Phone No',font=('times new roman',20,'bold'))
        phoneNoLabel.grid(row=1,column=0,padx=30,pady=15,sticky=W)
        phoneNoEntry = Entry(entryWindow,font=('roman',15,'bold'))
        phoneNoEntry.grid(row=1,column=1,pady=15,padx=10)

        addressLabel = Label(entryWindow,text='Address',font=('times new roman',20,'bold'))
        addressLabel.grid(row=2,column=0,padx=30,pady=15,sticky=W)
        addressEntry = Entry(entryWindow,font=('roman',15,'bold'))
        addressEntry.grid(row=2,column=1,pady=15,padx=10)

        supButton = ttk.Button(entryWindow,text=button_text,command=command)
        supButton.grid(row=6,columnspan=2,pady=10)

def add_data():
    if supNameEntry.get()=='' or phoneNoEntry.get()=='' or addressEntry.get()=='':
        messagebox.showerror('Error','All fields are required',parent=entryWindow)
    else:
        try:
            query = 'SELECT MAX(supId) FROM supplier'
            myCursor.execute(query)
            max_id = myCursor.fetchone()[0]
            new_supplier_id = max_id + 1 if max_id else 1
            query = 'INSERT into supplier (supId,supName,phoneNo,address) VALUES (?,?,?,?)'
            myCursor.execute(query,(new_supplier_id,supNameEntry.get(),phoneNoEntry.get(),addressEntry.get()))
            con.commit()
            result = messagebox.askyesno('Confirm','Data added successfully. Do you want to clean the form?')
            if result:
                supNameEntry.delete(0, END)
                phoneNoEntry.delete(0, END)
                addressEntry.delete(0, END)
            else:
                pass
        except:
            messagebox.showerror('Error','An error occurred while adding data',parent=entryWindow)
            return
        show_data()
            
def search_data():
    query = 'SELECT * FROM supplier where supName=? or phoneNo=? or address=?'
    myCursor.execute(query,(supNameEntry.get(),phoneNoEntry.get(),addressEntry.get()))
    supplierTable.delete(*supplierTable.get_children())
    fetchedData = myCursor.fetchall()
    if not fetchedData:
        messagebox.showerror('Error', f'No match')
    for data in fetchedData:
        supplierTable.insert('',END,values=data)

def delete_data():
    result = messagebox.askyesno('Confirm','Do you want to delete?')
    if result:
        try:
            indexing = supplierTable.focus()
            content = supplierTable.item(indexing)
            contentId = content['values'][0]
            contentIdInt = int(contentId)
            query = 'DELETE FROM supplier WHERE supId = ?'
            myCursor.execute(query,(contentIdInt,))
            con.commit()
            messagebox.showinfo('Deleted',f'The supplier with supplier Id {contentIdInt} is deleted succesfully')
            query = 'SELECT * FROM supplier'
            myCursor.execute(query)
            fetchedData = myCursor.fetchall()
            supplierTable.delete(*supplierTable.get_children())
            for data in fetchedData:
                supplierTable.insert('',END,values=data)
        except Exception as e:
            messagebox.showerror('Error', f'No supplier selected')
    else:
        pass

def show_data():
    query = 'SELECT * FROM supplier'
    myCursor.execute(query)
    fetchedData = myCursor.fetchall()
    supplierTable.delete(*supplierTable.get_children())
    for data in fetchedData:
        supplierTable.insert('',END,values=data)

def update_data():
    query = 'UPDATE supplier SET supName=?,phoneNo=?,address=? where supId=?'
    myCursor.execute(query,(supNameEntry.get(),phoneNoEntry.get(),addressEntry.get(),supId))
    con.commit()
    messagebox.showinfo('Success',f'Supplier {supNameEntry.get()} is modified successfully',parent=entryWindow)
    entryWindow.destroy()
    show_data()

def export_data():
    url = filedialog.asksaveasfilename(defaultextension='.csv')
    indexing = supplierTable.get_children()
    newList = []
    for index in indexing:
        content = supplierTable.item(index)
        dataList = content['values']
        newList.append(dataList)
    table = pandas.DataFrame(newList,columns=['Id','Name','Phone no','Address'])
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
root=ttkthemes.ThemedTk()

root.get_themes()
root.set_theme('radiance')

root.geometry('1174x700+0+0')
root.title('Suppliers')
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
 
addSupButton = ttk.Button(leftFrame,text='Add Supplier',width=20,command=lambda :toplevel_data('Add Supplier','Add Supplier',add_data))
addSupButton.grid(row=1,column=0,pady=10)

searchSupButton = ttk.Button(leftFrame,text='Search Supplier',width=20,command=lambda :toplevel_data('Search Supplier','Search Supplier',search_data))
searchSupButton.grid(row=2,column=0,pady=10)

updateSupButton = ttk.Button(leftFrame,text='Update Supplier',width=20,command=lambda :toplevel_data('Update Supplier','Update Supplier',update_data))
updateSupButton.grid(row=3,column=0,pady=10)

showSupButton = ttk.Button(leftFrame,text='Show Supplier',width=20,command=show_data)
showSupButton.grid(row=4,column=0,pady=10)

exportDataButton = ttk.Button(leftFrame,text='Export data',width=20,command=export_data)
exportDataButton.grid(row=5,column=0,pady=10)

deleteSupButton = ttk.Button(leftFrame,text='Delete Supplier',width=20,command=delete_data)
deleteSupButton.grid(row=6,column=0,pady=10)

exitButton = ttk.Button(leftFrame,text='Exit',width=20,command=to_exit)
exitButton.grid(row=7,column=0,pady=10)

backButton = ttk.Button(leftFrame,text='Back',width=20,command=back)
backButton.grid(row=8,column=0,pady=10)

rightFrame = Frame(root)
rightFrame.place(x=350,y=80,width=1000,height=600)

scrollBarX = Scrollbar(rightFrame,orient=HORIZONTAL)
scrollBarY = Scrollbar(rightFrame,orient=VERTICAL)

supplierTable = ttk.Treeview(rightFrame,columns=('supId','supName','phoneNo','address'),
                    xscrollcommand=scrollBarX.set,yscrollcommand=scrollBarY.set)

scrollBarX.config(command=supplierTable.xview)
scrollBarY.config(command=supplierTable.yview)

scrollBarX.pack(side=BOTTOM,fill=X)
scrollBarY.pack(side=RIGHT,fill=Y)

supplierTable.pack(fill=BOTH,expand=1)

for i in range(0, len(nameField)):
    supplierTable.heading(nameField[i],text=nameField[i])
supplierTable.config(show='headings')

supplierTable.column('supId',width=50,anchor=CENTER)
supplierTable.column('supName',width=300,anchor=CENTER)
supplierTable.column('phoneNo',width=100,anchor=CENTER)
supplierTable.column('address',width=500,anchor=CENTER)

style = ttk.Style()
style.configure('Treeview',rowheight=25,font=('arial',12,'bold'),
                foreground='green',background='black',fieldbackground='green')
style.configure('Treeview.Heading',font=('arial',14,'bold'),foreground='green')

root.mainloop()