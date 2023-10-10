from tkinter import *
from tkinter import ttk
import tkinter as tk
import subprocess
from tkinter import messagebox 
from  datetime import date
import time
import sqlite3
import os,tempfile
from invoice_products import my_dict,my_list
import platform
from tkcalendar import DateEntry

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
nameEntry.insert(0,'Default')

paymentLabel = Label(customerDetailsFrame, text='Payment Method',font=('times new roman',15,'bold')
                  ,bg='lime green',fg='white')
paymentLabel.grid(row=0,column=2,padx=20,pady=2)

paymentEntry = Entry(customerDetailsFrame,font=('arial',15),bd=4,width=18)
paymentEntry.grid(row=0,column=3,padx=8)

billNumberLabel = Label(customerDetailsFrame, text='Bill No',font=('times new roman',15,'bold')
                  ,bg='lime green',fg='white')
billNumberLabel.grid(row=0,column=4,padx=20,pady=2)

billNumberEntry = Entry(customerDetailsFrame,font=('arial',15),bd=4,width=18)
billNumberEntry.grid(row=0,column=5,padx=8)

searchButton = Button(customerDetailsFrame,text='SEARCH',
                      font=('arial',12,'bold'),bd=3,width=10,command=lambda:search_bill())
searchButton.grid(row=0,column=6,padx=20,pady=8)

#functionality part of invoice/bill frame
def clear_text():
    messagebox.askyesno('Confirm', 'Are you sure you want to clear text?')
    textArea.delete(1.0,END)

def print_bill():
    if textArea.get(1.0,END)=='\n':
        messagebox.showerror('Error','Bill is empty')
    else:
        pfile=tempfile.mktemp('.txt')
        open(pfile,'w').write(textArea.get(1.0,END))
    system_platform = platform.system()
    if system_platform == "Windows":
        try:
            os.startfile(pfile, "print")
        except AttributeError:
            messagebox.showerror('Error','Printing not supported on this platform.')
    elif system_platform == "Linux":
        try:
            subprocess.run(["lp", pfile])
        except FileNotFoundError:
            messagebox.showerror('Error',"Printing utility 'lp' not found. Please install it and try again.")
    else:
        messagebox.showerror('Error',f"Printing not supported on {system_platform}.")

def search_bill():
    for i in os.listdir('bills/'):
        if i.split('.')[0].strip()==billNumberEntry.get():
            f=open(f'bills/{i}','r')
            textArea.delete(1.0,END)
            for data in f:
                textArea.insert(END,data)
            f.close()
            break
    else:
        messagebox.showerror('Error','Invalid Bill Number')

def bill_area():
    global billNumber
    billNumber = str(inv_id)
    todayDate = time.strftime('%d/%m/%Y')
    currentTime = time.strftime('%H:%M:%S')
    textArea.delete(1.0,END)
    if total == 0:
        messagebox.showerror('Error', 'No product purchased')
    else:
        textArea.insert(END,'\t  **ALAN PHAMACEUTICALS(NIG) LTD.**')
        textArea.insert(END,'\n    Opp. Iwo city hall, Ibadan road, Iwo, Osun state.')
        textArea.insert(END,'\n\t\t    08035896001')
        textArea.insert(END,'\n')
        textArea.insert(END,f'\nDate: {todayDate} {currentTime}')
        textArea.insert(END,f'\nBill Number: {billNumber}')
        textArea.insert(END,'\nCustomer: Default')
        textArea.insert(END,'\nPayment Method: Cash')
        textArea.insert(END,'\n=======================================================')
        textArea.insert(END,'\nProduct\t\t\t\tQty\t\tPrice')
        textArea.insert(END,'\n=======================================================')
        for line in trv.get_children():
            my_lst = trv.item(line)['values']
            textArea.insert(END,f'\n{my_lst[2]}\t\t\t\t{my_lst[3]}\t\t{my_lst[5]}')
        textArea.insert(END,'\n=======================================================')
        textArea.insert(END,f'\n\t\t\t\t\t\t\t\t\t\t\t\tTotal: #{total}')
        #textArea.insert(END,'\n=======================================================')
        textArea.insert(END,'\n\n\t\t**Thanks for your patronage**')
        save_bill()

def save_bill():
    if not os.path.exists('bills'):
        os.mkdir('bills')
    result = messagebox.askyesno('Confirm', 'Do you want to save the bill?' )
    if result:
        bill_content = textArea.get(1.0,END)
        file = open(f'bills/ {billNumber}.txt', 'w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('Success', f'Bill number {billNumber} saved succefully')

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

#totalButton = Button(billMenu,text='Total',font=('arial',16,'bold'),bg='lime green'
#                     ,bd=5,width=8,pady=5)
#totalButton.grid(row=0,column=0,padx=5,pady=10)

#billButton = Button(billMenu,text='Bill',font=('arial',16,'bold'),bg='lime green'
                     #,bd=5,width=8,pady=5,command=bill_area)
#billButton.grid(row=0,column=0,pady=10,padx=5)

#emailButton = Button(billMenu,text='Email',font=('arial',16,'bold'),bg='lime green'
#                     ,bd=5,width=8,pady=5)
#emailButton.grid(row=0,column=2,pady=10)

printButton = Button(billMenu,text='Print',font=('arial',16,'bold'),bg='lime green'
                     ,bd=5,width=8,pady=5,command=lambda:print_bill())
printButton.grid(row=0,column=1,pady=5,padx=5)

clearButton = Button(billMenu,text='Clear',font=('arial',16,'bold'),bg='lime green'
                     ,bd=5,width=8,pady=5,command=lambda:clear_text())
clearButton.grid(row=0,column=2,pady=5,padx=5)

#Product display frame in treeview
leftFrame = Frame(root)
leftFrame.place(x=20,y=160,width=700,height=700)

l1=tk.Label(leftFrame,text='Product',font=font1)
l1.grid(row=0,column=0,padx=10,pady=5)

product=tk.StringVar(leftFrame)
cb_product = ttk.Combobox(leftFrame, values=my_list,textvariable=product,width=20)
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
style.theme_use("clam") # set theme to clam
style.configure("Treeview", background="azure2", 
                fieldbackground="lightyellow", foreground="black",font=font1)
style.configure('Treeview.Heading', background="lime green") 
# Using treeview widget
trv = ttk.Treeview(leftFrame, selectmode ='browse')
trv.grid(row=1,column=0,columnspan=7,rowspan=2,padx=10,pady=2)
# number of columns
trv["columns"] = ("1","2","3","4","5","6")
trv['show'] = 'headings'
trv.column("1", width = 40, anchor ='c') # width & alignment
trv.column("2", width=40, anchor="w")
trv.column("3", width = 250, anchor ='c')
trv.column("4", width = 70, anchor ='c')
trv.column("5", width = 90, anchor ='c')
trv.column("6", width = 100, anchor ='c')
trv.heading("1", text ="Sl No") # Heading text
trv.heading("2", text="p_id")  # Heading text
trv.heading("3", text ="Product")
trv.heading("4", text ="Quantity")
trv.heading("5", text ="Rate")  
trv.heading("6", text ="Total")
l5=tk.Label(leftFrame,text='Total :',fg='blue',font=font1,anchor='e')
l5.grid(row=3,column=4)
l6=tk.Label(leftFrame,text='0',fg='blue',font=font1,anchor='e')
l6.grid(row=3,column=5)
#l7=tk.Label(leftFrame,text='Tax 10 % :',fg='blue',font=font1,anchor='e')
#l7.grid(row=4,column=4)
#l8=tk.Label(leftFrame,text='0',fg='blue',font=font1,anchor='e')
#l8.grid(row=4,column=5)
l9=tk.Label(leftFrame,text='Total :',fg='red',font=font2,anchor='e')
l9.grid(row=4,column=4)
l10=tk.Label(leftFrame,text='0',fg='red',font=font2,anchor='e')
l10.grid(row=4,column=5,pady=20)
    
b2=tk.Button(leftFrame,text='Delete',state='disabled',command=lambda:data_delete())
b2.grid(row=3,column=1)
b3=tk.Button(leftFrame,text='Del All',command=lambda:my_reset())
b3.grid(row=3,column=2)
b4=tk.Button(leftFrame,text='Confirm',font=font2,bg='lightyellow',command=lambda:insert_data())
b4.grid(row=5,column=2)
l_msg=tk.Label(leftFrame,text='',fg='red',font=12)
l_msg.grid(row=6,column=3,columnspan=2)
b4=tk.Button(leftFrame,text='Sales Report',font=font2,bg='lightyellow',command=lambda:sales_report())
b4.grid(row=7,columnspan=2)
total,iid,p_id=0,0,0

#Add functionality
def my_price(*args):  # *args is used to pass any number of arguments
    l1.config(text="")  # Clear the label
    global p_id
    p_id=0 # If product is not selected from the options then id is 0 
    for i, j in my_dict.items():  # Loop through the dictionary
        if j[1] == product.get():  # match the product name
            prc.set(j[2]) # price is collected. 
            p_id=j[0]  # Product id is collected

def my_add():
    global iid, p_id
    iid = iid+1  # Serial number to display 
    total = round(qty.get()*prc.get(),2) # row wise total 
    trv.insert("", 'end',iid=iid, values =(iid,p_id,product.get(),qty.get(),prc.get(),total))
    my_upd(trv)

def my_upd(trv):
    global total 
    total,sub_total = 0,0
    for child in trv.get_children():
        sub_total = round(sub_total+float(trv.item(child)["values"][5]),2)
    l6.config(text=str(sub_total)) # shows sub total 
    #tax=round(0.1*sub_total,2)  # 10 % tax rate, update here
    #l8.config(text=str(tax))  # tax amount is displayed 
    total=round(sub_total,2) # tax added to sub total 
    l10.config(text=str(total))  # Final price is displayed
    product.set('') # reset the combobox 
    qty.set(1)  # reset quantity to 1
    prc.set(0.0) # reset price to 0.0 

def my_select(self):
    b2.config(state='active') # Delete button is active now 

def data_delete():
    try:
        p_id = trv.selection()[0] # collect selected row id
        trv.delete(p_id)  # remove the selected row from Treeview
        b2['state'] = 'disabled' # disable the button 
        my_upd(trv) # Update the total 
    except Exception as e:
        messagebox.showerror('Error', f'No product selected')

def my_reset():
    for item in trv.get_children():
        trv.delete(item) # remove row 
    global total
    total = 0
    product.set('') # reset combobox
    qty.set(1) # Update quantity to 1 
    prc.set(0.0) # Update price to 0.0
    l6.config(text='0')  # Update display sub total
    #l8.config(text='0')  # Update display for tax
    l10.config(text='0') # Update display for total

def insert_data():
    global total, inv_id, id
    dt = date.today() # Today's date
    data = (total,dt) # Data for parameterized query
    query = "INSERT INTO invoice (total,date) VALUES(?,?)"
    id = myCursor.execute(query,data)
    con.commit()
    inv_id = id.lastrowid # get the bill or invoice number after adding data
    query = "INSERT INTO invoice_dtl (inv_id,p_id,product,qty,price) \
                VALUES(?,?,?,?,?)"
    my_data = [] # list to store multiple rows of data
    # In all rows invoice id is same
    for line in trv.get_children():
        my_list = trv.item(line)['values']
        my_data.append([inv_id,my_list[1],my_list[2],my_list[3],my_list[4]])
    i = 0
    for datum in my_data:
        myCursor.execute(query,datum)# adding list of products to table
        con.commit()
        i = i + 1
    #print("Rows Added  = ",id.rowcount)
    l_msg.config(text='Bill No:'+str(inv_id)+', Products:'+str(i))
    l_msg.after(3000, lambda: l_msg.config(text=''))
    bill_area() # generate bill
    my_reset() # reset function

def sales_report():
    popSales = Toplevel()
    popSales.title('Sales report')
    popSales.grab_set()
    #popSales.geometry("700x500")
    popSales.resizable(False,False)
    sel=tk.StringVar()
    prompt = Label(popSales,text='Choose Date',font=('times new roman',20,'bold'))
    prompt.grid(row=0,column=0,padx=30,pady=15,sticky=W)
    cal=DateEntry(popSales,selectmode='day',textvariable=sel)
    cal.grid(row=0,column=1,padx=20,pady=30)
    def updte(*args): # triggered when value of string varaible changes
        sales = []
        if(len(sel.get())>4):
            dt=cal.get_date() # get selected date object from calendar
            dt1=dt.strftime("%Y-%m-%d") #format for MySQL date column 
            dt2=dt.strftime("%d-%B-%Y") #format to display at label 
            l1.config(text=dt2) # display date at Label
            query="SELECT total from invoice WHERE date=?"
            sales = con.execute(query,(dt1,)) # execute query with data
            total_sales = 0
            for sale in sales:
                total_sales = round((total_sales + int(sale[0])), 2)
            l2.config(text="Total Sales: " + str(total_sales)) # show total value
    sel.trace('w',updte)
    l1=tk.Label(popSales,font=('Times',22,'bold'),fg='blue')
    l1.grid(row=1,column=0)
    l2=tk.Label(popSales,font=('Times',22,'bold'),fg='red')
    l2.grid(row=2,column=0)

trv.bind("<<TreeviewSelect>>", my_select)  # User selection of row
product.trace("w", my_price)  # Call the function on change

root.mainloop()