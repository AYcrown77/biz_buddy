from tkinter import ttk
import tkinter as tk
from  datetime import date
import sqlite3
from tkinter import *
import tkinter as tk

con = sqlite3.connect('alan_pharm_supermarket.db')
myCursor = con.cursor()
query = '''
    CREATE TABLE IF NOT EXISTS invoice (
        inv_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        total FLOAT NOT NULL,
        date DATE NOT NULL
    );
    CREATE TABLE IF NOT EXISTS invoice_dtl (
        dtl_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        inv_id INT(6) NOT NULL,
        p_id INT(4) NOT NULL,
        product VARCHAR(50) NOT NULL,
        qty INT(3) NOT NULL,
        price FLOAT NOT NULL
    );
'''
myCursor.executescript(query)


root = tk.Tk()
root.title('Sales page')
root.geometry('1200x670')
root.iconphoto(False, tk.PhotoImage(file='images/billing.png'))
font1 =['Times',16,'normal'] # font size and style 
font2 = ['Times',22,'normal']
headingLabel = Label(root,text='Retail Billing System',font=('times new roman',30,'bold')
                     ,bg='lime green',bd=12,relief=GROOVE)
headingLabel.pack(fill=X,pady=1)

customerDetailsFrame = LabelFrame(root,text='Customer Details',font=('times new roman',15,'bold')
                                    ,bd=8,relief=GROOVE,bg='lime green')
customerDetailsFrame.pack(fill=X)

nameLabel = Label(customerDetailsFrame, text='Name',font=('times new roman',15,'bold')
                  ,bg='lime green',fg='white')
nameLabel.grid(row=0,column=0,padx=20)

nameEntry = Entry(customerDetailsFrame,font=('arial',15),bd=4,width=18)
nameEntry.grid(row=0,column=1,padx=8)

phoneLabel = Label(customerDetailsFrame, text='Phone No',font=('times new roman',15,'bold')
                  ,bg='lime green',fg='white')
phoneLabel.grid(row=0,column=2,padx=20,pady=2)

phoneEntry = Entry(customerDetailsFrame,font=('arial',15),bd=4,width=18)
phoneEntry.grid(row=0,column=3,padx=8)

billNumberLabel = Label(customerDetailsFrame, text='Bill No',font=('times new roman',15,'bold')
                  ,bg='lime green',fg='white')
billNumberLabel.grid(row=0,column=4,padx=20,pady=2)

billNumberEntry = Entry(customerDetailsFrame,font=('arial',15),bd=4,width=18)
billNumberEntry.grid(row=0,column=5,padx=8)

searchButton = Button(customerDetailsFrame,text='SEARCH',font=('arial',12,'bold'),bd=3,width=10)
searchButton.grid(row=0,column=6,padx=20,pady=8)

#Product display frame in treeview
leftFrame = Frame(root)
leftFrame.place(x=20,y=160,width=1000,height=700)

l1=tk.Label(leftFrame,text='Product',font=font1)
l1.grid(row=0,column=0,padx=10,pady=5)
p_list=['Moniter','Mouse','Keyboard','Pen Drive','CPU','Power Unit'] # product list
product=tk.StringVar(leftFrame)
cb_product = ttk.Combobox(leftFrame, values=p_list,textvariable=product,width=10)
cb_product.grid(row=0,column=1)
##
l2=tk.Label(leftFrame,text='Quantity',font=font1)
l2.grid(row=0,column=2,padx=20,pady=10)
qty=tk.IntVar(value=1)
quantity = tk.Entry(leftFrame, textvariable=qty,width=5)
quantity.grid(row=0,column=3)
##
l3=tk.Label(leftFrame,text='Price',font=font1)
l3.grid(row=0,column=4,padx=20,pady=10)
prc=tk.DoubleVar()
price = tk.Entry(leftFrame,textvariable=prc,width=10)
price.grid(row=0,column=5)
##
b1=tk.Button(leftFrame,text='Add',font=14,command=lambda:my_add())
b1.grid(row=0,column=6,padx=10)
##
style = ttk.Style(leftFrame)
style.theme_use("clam") # set theam to clam
style.configure("Treeview", background="azure2", 
                fieldbackground="lightyellow", foreground="black",font=font1)
style.configure('Treeview.Heading', background="PowderBlue") 
# Using treeview widget
trv = ttk.Treeview(leftFrame, selectmode ='browse')
trv.grid(row=1,column=0,columnspan=7,rowspan=2,padx=10,pady=2)
# number of columns
trv["columns"] = ("1", "2", "3","4","5")
trv['show'] = 'headings'
trv.column("1", width = 40, anchor ='c') # width & alignment
trv.column("2", width = 250, anchor ='c')
trv.column("3", width = 70, anchor ='c')
trv.column("4", width = 90, anchor ='c')
trv.column("5", width = 100, anchor ='c')
trv.heading("1", text ="Sl No") # Heading text 
trv.heading("2", text ="Product")
trv.heading("3", text ="Quantity")
trv.heading("4", text ="Rate")  
trv.heading("5", text ="Total")
l5=tk.Label(leftFrame,text='Total :',fg='blue',font=font1,anchor='e')
l5.grid(row=3,column=4)
l6=tk.Label(leftFrame,text='0',fg='blue',font=font1,anchor='e')
l6.grid(row=3,column=5)
l7=tk.Label(leftFrame,text='Tax 10 % :',fg='blue',font=font1,anchor='e')
l7.grid(row=4,column=4)
l8=tk.Label(leftFrame,text='0',fg='blue',font=font1,anchor='e')
l8.grid(row=4,column=5)
l9=tk.Label(leftFrame,text='Total :',fg='red',font=font2,anchor='e')
l9.grid(row=5,column=4)
l10=tk.Label(leftFrame,text='0',fg='red',font=font2,anchor='e')
l10.grid(row=5,column=5,pady=20)
    
b2=tk.Button(leftFrame,text='Delete',state='disabled',command=lambda:data_delete())
b2.grid(row=3,column=1)
b3=tk.Button(leftFrame,text='Del All',command=lambda:my_reset())
b3.grid(row=3,column=2)
b4=tk.Button(leftFrame,text='Confirm',font=font2,bg='lightyellow',command=lambda:insert_data())
b4.grid(row=5,column=2)
l_msg=tk.Label(leftFrame,text='',fg='red',font=12)
l_msg.grid(row=6,column=3,columnspan=2)
total,iid=0,0

#Invoice frame

rightFrame = Frame(root,bd=8,relief=GROOVE)
rightFrame.place(x=800,y=160,width=500,height=550)

billAreaLabel = Label(rightFrame,text='Bill Area',font=('times new roman',15,'bold'),bd=7,relief=GROOVE)
billAreaLabel.pack(fill=X)

scrollbar = Scrollbar(rightFrame,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)
textArea = Text(rightFrame,height=18,width=55,yscrollcommand=scrollbar.set)
textArea.pack()
scrollbar.config(command=textArea.yview)

billMenu = Frame(rightFrame,bd=7,relief=GROOVE)
billMenu.pack(pady=10)

totalButton = Button(billMenu,text='Total',font=('arial',16,'bold'),bg='lime green'
                     ,bd=5,width=8,pady=5)
totalButton.grid(row=0,column=0,padx=5,pady=10)

billButton = Button(billMenu,text='Bill',font=('arial',16,'bold'),bg='lime green'
                     ,bd=5,width=8,pady=5)
billButton.grid(row=0,column=1,pady=10)

emailButton = Button(billMenu,text='Email',font=('arial',16,'bold'),bg='lime green'
                     ,bd=5,width=8,pady=5)
emailButton.grid(row=0,column=2,pady=10)

printButton = Button(billMenu,text='Print',font=('arial',16,'bold'),bg='lime green'
                     ,bd=5,width=8,pady=5)
printButton.grid(row=1,columnspan=2,pady=5)

clearButton = Button(billMenu,text='Clear',font=('arial',16,'bold'),bg='lime green'
                     ,bd=5,width=8,pady=5)
clearButton.grid(row=1,column=2,pady=5)
#Add functionality
def my_add():
    global iid
    iid=iid+1  # Serial number to display 
    total=round(qty.get()*prc.get(),2) # row wise total 
    trv.insert("", 'end',iid=iid, values =(iid,product.get(),qty.get(),prc.get(),total))
    my_upd(trv)

def my_upd(trv):
    global total 
    total,sub_total=0,0
    for child in trv.get_children():
        sub_total=round(sub_total+float(trv.item(child)["values"][4]),2)
    l6.config(text=str(sub_total)) # shows sub total 
    tax=round(0.1*sub_total,2)  # 10 % tax rate, update here
    l8.config(text=str(tax))  # tax amount is displayed 
    total=round(sub_total+tax,2) # tax added to sub total 
    l10.config(text=str(total))  # Final price is displayed
    product.set('') # reset the combobox 
    qty.set(1)  # reset quantity to 1
    prc.set(0.0) # reset price to 0.0 

def my_select(self):
    b2.config(state='active') # Delete button is active now 

def data_delete():
    p_id = trv.selection()[0] # collect selected row id
    trv.delete(p_id)  # remove the selected row from Treeview
    b2['state']='disabled' # disable the button 
    my_upd(trv) # Update the total 

def my_reset():
    for item in trv.get_children():
        trv.delete(item) # remove row 
    global total
    total=0
    product.set('') # reset combobox
    qty.set(1) # Update quantity to 1 
    prc.set(0.0) # Update price to 0.0
    l6.config(text='0')  # Update display sub total
    l8.config(text='0')  # Update display for tax
    l10.config(text='0') # Update display for total


def insert_data():
    global total 
    dt = date.today() # Today's date 
    data=(total,dt) # Data for parameterized query
    query="INSERT INTO invoice ( total, dt) values(%s,%s)"
    #print(query)
    id=con.execute(query,data)
    inv_id=id.lastrowid # get the bill or invoice number after adding data
    
    query="INSERT INTO  plus2_invoice_dtl (inv_id,p_id,product,qty,price) \
         VALUES(%s,%s,%s,%s,%s)"
    my_data=[] # list to store multiple rows of data
    # In all rows inventory id is same
    for line in trv.get_children():
        my_list=trv.item(line)['values']
        my_data.append([inv_id,my_list[0],my_list[1],my_list[2],my_list[3]])
    id=con.execute(query,my_data) # adding list of products to table
    #print("Rows Added  = ",id.rowcount)
    l_msg.config(text='Bill No:'+str(inv_id)+',Products:'+str(id.rowcount))
    l_msg.after(3000, lambda: l_msg.config(text='') )
    my_reset() # reset function 
trv.bind("<<TreeviewSelect>>", my_select)  # User selection of row

root.mainloop()