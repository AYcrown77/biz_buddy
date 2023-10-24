from tkinter import *
import time
import ttkthemes
from tkinter import ttk,messagebox,filedialog
import sqlite3
import pandas

#functionality part
count = 0
txt = ''

nameField = ['custId','custName','phoneNo','address','paymentBal']

con = sqlite3.connect('alan_pharm_supermarket.db')
myCursor = con.cursor()
query = 'CREATE TABLE IF NOT EXISTS customer (\
            custId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,\
            custName VARCHAR(50) NOT NULL,\
            phoneNo INTEGER NOT NULL,\
            address VARCHAR(100) NOT NULL,\
            paymentBal FLOAT NOT NULL)'
myCursor.execute(query)

#con.commit()
#con.close()

def toplevel_data(title,button_text,command):
    global custId,custNameEntry,phoneNoEntry,addressEntry,entryWindow,indexing,paymentBalEntry
    
    if title == 'Update Customer':
        indexing = customerTable.focus()
        if indexing:
            entryWindow = Toplevel()
            entryWindow.title(title)
            entryWindow.grab_set()
            entryWindow.resizable(False,False)
        
            custNameLabel = Label(entryWindow,text='Name',font=('times new roman',20,'bold'))
            custNameLabel.grid(row=0,column=0,padx=30,pady=15,sticky=W)
            custNameEntry = Entry(entryWindow,font=('roman',15,'bold'))
            custNameEntry.grid(row=0,column=1,pady=15,padx=10)

            phoneNoLabel = Label(entryWindow,text='Phone No',font=('times new roman',20,'bold'))
            phoneNoLabel.grid(row=1,column=0,padx=30,pady=15,sticky=W)
            phoneNoEntry = Entry(entryWindow,font=('roman',15,'bold'))
            phoneNoEntry.grid(row=1,column=1,pady=15,padx=10)

            addressLabel = Label(entryWindow,text='Address',font=('times new roman',20,'bold'))
            addressLabel.grid(row=2,column=0,padx=30,pady=15,sticky=W)
            addressEntry = Entry(entryWindow,font=('roman',15,'bold'))
            addressEntry.grid(row=2,column=1,pady=15,padx=10)

            paymentBalLabel = Label(entryWindow,text='Payment Bal',font=('times new roman',20,'bold'))
            paymentBalLabel.grid(row=3,column=0,padx=30,pady=15,sticky=W)
            paymentBalEntry = Entry(entryWindow,font=('roman',15,'bold'))
            paymentBalEntry.grid(row=3,column=1,pady=15,padx=10)

            custButton = ttk.Button(entryWindow,text=button_text,command=command)
            custButton.grid(row=4,columnspan=2,pady=10)

            content = customerTable.item(indexing)
            listData = content['values']
            custId = listData[0]
            custNameEntry.insert(0,listData[1])
            phoneNoEntry.insert(0,listData[2])
            addressEntry.insert(0,listData[3])
            paymentBalEntry.insert(0,listData[4])
        else:
            messagebox.showerror('Error', f'No customer selected')
            return

    if title != 'Update Customer':
        entryWindow = Toplevel()
        entryWindow.title(title)
        entryWindow.grab_set()
        entryWindow.resizable(False,False)

        custNameLabel = Label(entryWindow,text='Name',font=('times new roman',20,'bold'))
        custNameLabel.grid(row=0,column=0,padx=30,pady=15,sticky=W)
        custNameEntry = Entry(entryWindow,font=('roman',15,'bold'))
        custNameEntry.grid(row=0,column=1,pady=15,padx=10)

        phoneNoLabel = Label(entryWindow,text='Phone No',font=('times new roman',20,'bold'))
        phoneNoLabel.grid(row=1,column=0,padx=30,pady=15,sticky=W)
        phoneNoEntry = Entry(entryWindow,font=('roman',15,'bold'))
        phoneNoEntry.grid(row=1,column=1,pady=15,padx=10)

        addressLabel = Label(entryWindow,text='Address',font=('times new roman',20,'bold'))
        addressLabel.grid(row=2,column=0,padx=30,pady=15,sticky=W)
        addressEntry = Entry(entryWindow,font=('roman',15,'bold'))
        addressEntry.grid(row=2,column=1,pady=15,padx=10)

        paymentBalLabel = Label(entryWindow,text='Payment Balance',font=('times new roman',20,'bold'))
        paymentBalLabel.grid(row=3,column=0,padx=30,pady=15,sticky=W)
        paymentBalEntry = Entry(entryWindow,font=('roman',15,'bold'))
        paymentBalEntry.grid(row=3,column=1,pady=15,padx=10)

        custButton = ttk.Button(entryWindow,text=button_text,command=command)
        custButton.grid(row=4,columnspan=2,pady=10)

def add_data():
    if custNameEntry.get()=='' or phoneNoEntry.get()=='' or addressEntry.get()=='' or paymentBalEntry.get()=='':
        messagebox.showerror('Error','All fields are required',parent=entryWindow)
    else:
        try:
            query = 'SELECT MAX(custId) FROM customer'
            myCursor.execute(query)
            max_id = myCursor.fetchone()[0]
            new_customer_id = max_id + 1 if max_id else 1
            query = 'INSERT into customer (custId,custName,phoneNo,address,paymentBal) VALUES (?,?,?,?,?)'
            myCursor.execute(query,(new_customer_id,custNameEntry.get(),phoneNoEntry.get(),addressEntry.get(),paymentBalEntry.get()))
            con.commit()
            result = messagebox.askyesno('Confirm','Data added successfully. Do you want to clean the form?')
            if result:
                custNameEntry.delete(0, END)
                phoneNoEntry.delete(0, END)
                addressEntry.delete(0, END)
                paymentBalEntry.delete(0, END)
            else:
                pass
        except:
            messagebox.showerror('Error','An error occurred while adding data',parent=entryWindow)
            return
        show_data()
            
def search_data():
    query = 'SELECT * FROM customer where custName=? or phoneNo=? or address=? or paymentBal=?'
    myCursor.execute(query,(custNameEntry.get(),phoneNoEntry.get(),addressEntry.get(),paymentBalEntry.get()))
    customerTable.delete(*customerTable.get_children())
    fetchedData = myCursor.fetchall()
    if not fetchedData:
        messagebox.showerror('Error', f'No match')
    for data in fetchedData:
        customerTable.insert('',END,values=data)

def delete_data():
    result = messagebox.askyesno('Confirm','Do you want to delete?')
    if result:
        try:
            indexing = customerTable.focus()
            content = customerTable.item(indexing)
            contentId = content['values'][0]
            contentIdInt = int(contentId)
            query = 'DELETE FROM customer WHERE custId = ?'
            myCursor.execute(query,(contentIdInt,))
            con.commit()
            messagebox.showinfo('Deleted',f'The customer with customer Id {contentIdInt} is deleted succesfully')
            query = 'SELECT * FROM customer'
            myCursor.execute(query)
            fetchedData = myCursor.fetchall()
            customerTable.delete(*customerTable.get_children())
            for data in fetchedData:
                customerTable.insert('',END,values=data)
        except Exception as e:
            messagebox.showerror('Error', f'No customer selected')
    else:
        pass

def show_data():
    query = 'SELECT * FROM customer'
    myCursor.execute(query)
    fetchedData = myCursor.fetchall()
    customerTable.delete(*customerTable.get_children())
    for data in fetchedData:
        customerTable.insert('',END,values=data)

def update_data():
    query = 'UPDATE customer SET custName=?,phoneNo=?,address=?,paymentBal=? where custId=?'
    myCursor.execute(query,(custNameEntry.get(),phoneNoEntry.get(),addressEntry.get(),paymentBalEntry.get(),custId))
    con.commit()
    messagebox.showinfo('Success',f'Customer {custNameEntry.get()} is modified successfully',parent=entryWindow)
    entryWindow.destroy()
    show_data()

def export_data():
    url = filedialog.asksaveasfilename(defaultextension='.csv')
    indexing = customerTable.get_children()
    newList = []
    for index in indexing:
        content = customerTable.item(index)
        dataList = content['values']
        newList.append(dataList)
    table = pandas.DataFrame(newList,columns=['Id','Name','Phone no','Address','Payment Bal'])
    table.to_csv(url,index=False)
    messagebox.showinfo('Success','Data saved successfully')

def to_exit():
    result = messagebox.askyesno('Confirm','Do you want to exit?')
    if result:
        root.destroy()
    else:
        pass

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
root.title('Customers')
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
 
addCustButton = ttk.Button(leftFrame,text='Add Customer',width=20,command=lambda :toplevel_data('Add Customer','Add Customer',add_data))
addCustButton.grid(row=1,column=0,pady=10)

searchCustButton = ttk.Button(leftFrame,text='Search Customer',width=20,command=lambda :toplevel_data('Search Customer','Search Customer',search_data))
searchCustButton.grid(row=2,column=0,pady=10)

updateCustButton = ttk.Button(leftFrame,text='Update Customer',width=20,command=lambda :toplevel_data('Update Customer','Update Customer',update_data))
updateCustButton.grid(row=3,column=0,pady=10)

showCustButton = ttk.Button(leftFrame,text='Show Supplier',width=20,command=show_data)
showCustButton.grid(row=4,column=0,pady=10)

exportDataButton = ttk.Button(leftFrame,text='Export data',width=20,command=export_data)
exportDataButton.grid(row=5,column=0,pady=10)

deleteCustButton = ttk.Button(leftFrame,text='Delete Supplier',width=20,command=delete_data)
deleteCustButton.grid(row=6,column=0,pady=10)

exitButton = ttk.Button(leftFrame,text='Exit',width=20,command=to_exit)
exitButton.grid(row=7,column=0,pady=10)

rightFrame = Frame(root)
rightFrame.place(x=350,y=80,width=1000,height=600)

scrollBarX = Scrollbar(rightFrame,orient=HORIZONTAL)
scrollBarY = Scrollbar(rightFrame,orient=VERTICAL)

customerTable = ttk.Treeview(rightFrame,columns=('custId','custName','phoneNo','address','paymentBal'),
                    xscrollcommand=scrollBarX.set,yscrollcommand=scrollBarY.set)

scrollBarX.config(command=customerTable.xview)
scrollBarY.config(command=customerTable.yview)

scrollBarX.pack(side=BOTTOM,fill=X)
scrollBarY.pack(side=RIGHT,fill=Y)

customerTable.pack(fill=BOTH,expand=1)

for i in range(0, len(nameField)):
    customerTable.heading(nameField[i],text=nameField[i])
customerTable.config(show='headings')

customerTable.column('custId',width=100,anchor=CENTER)
customerTable.column('custName',width=300,anchor=CENTER)
customerTable.column('phoneNo',width=200,anchor=CENTER)
customerTable.column('address',width=500,anchor=CENTER)
customerTable.column('paymentBal',width=120,anchor=CENTER)

style = ttk.Style()
style.configure('Treeview',rowheight=25,font=('arial',12,'bold'),
                foreground='green',background='black',fieldbackground='green')
style.configure('Treeview.Heading',font=('arial',14,'bold'),foreground='green')

root.mainloop()