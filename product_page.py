from tkinter import *
import time
import tkinter as tk
from tkinter import ttk,messagebox,filedialog
import sqlite3
import pandas
from tkcalendar import DateEntry

#functionality part
count = 0
txt = ''

nameField = ['Product Id','Product Name','Retail Price','Wholesales Price',
             'Quantity','Expiry Date','Product Category']

con = sqlite3.connect('alan_pharm_supermarket.db')
myCursor = con.cursor()
query = 'CREATE TABLE IF NOT EXISTS products (\
            productId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,\
            productName VARCHAR(50) NOT NULL,\
            retailPrice DOUBLE NOT NULL,\
            wholesalesPrice DOUBLE NOT NULL,\
            quantity INTEGER NOT NULL,\
            expiryDate DATE NOT NULL,\
            productCategory VARCHAR(15) NOT NULL)'
myCursor.execute(query)

#con.commit()
#con.close()


def toplevel_data(title,button_text,command):
    global productId,productNameEntry,retailPriceEntry,wholesalesPriceEntry,\
        quantityEntry,expiryDateEntry,productCategoryEntry,entryWindow,indexing
    
    if title == 'Update Product':
        indexing = productTable.focus()
        if indexing:
            entryWindow = Toplevel()
            entryWindow.title(title)
            entryWindow.grab_set()
            entryWindow.resizable(False,False)
            entryWindow.configure(bg='lightgreen')
        
            productNameLabel = Label(entryWindow,text='Product Name',font=('times new roman',20,'bold'),bg='lightgreen')
            productNameLabel.grid(row=0,column=0,padx=30,pady=15,sticky=W)
            productNameEntry = Entry(entryWindow,font=('roman',15,'bold'))
            productNameEntry.grid(row=0,column=1,pady=15,padx=10)

            retailPriceLabel = Label(entryWindow,text='Retail Price',font=('times new roman',20,'bold'),bg='lightgreen')
            retailPriceLabel.grid(row=1,column=0,padx=30,pady=15,sticky=W)
            retailPriceEntry = Entry(entryWindow,font=('roman',15,'bold'))
            retailPriceEntry.grid(row=1,column=1,pady=15,padx=10)

            wholesalesPriceLabel = Label(entryWindow,text='Wholesales Price',font=('times new roman',20,'bold'),bg='lightgreen')
            wholesalesPriceLabel.grid(row=2,column=0,padx=30,pady=15,sticky=W)
            wholesalesPriceEntry = Entry(entryWindow,font=('roman',15,'bold'))
            wholesalesPriceEntry.grid(row=2,column=1,pady=15,padx=10)

            quantityLabel = Label(entryWindow,text='Quantity',font=('times new roman',20,'bold'),bg='lightgreen')
            quantityLabel.grid(row=3,column=0,padx=30,pady=15,sticky=W)
            quantityEntry = Entry(entryWindow,font=('roman',15,'bold'))
            quantityEntry.grid(row=3,column=1,pady=15,padx=10)

            expiryDateLabel = Label(entryWindow,text='Expiry Date',font=('times new roman',20,'bold'),bg='lightgreen')
            expiryDateLabel.grid(row=4,column=0,padx=30,pady=15,sticky=W)
            expiryDateEntry = DateEntry(entryWindow,font=('roman',15,'bold'),width=12,date_pattern="yyyy-mm-dd")
            expiryDateEntry.grid(row=4,column=1,pady=15,padx=10)

            productCategoryLabel = Label(entryWindow,text='Product Category',font=('times new roman',20,'bold'),bg='lightgreen')
            productCategoryLabel.grid(row=5,column=0,padx=30,pady=15,sticky=W)
            productCategoryEntry = ttk.Combobox(entryWindow,values=['Drug','Supermarket'],font=('roman',15,'bold'))
            productCategoryEntry.grid(row=5,column=1,pady=15,padx=10)

            ProductButton = tk.Button(entryWindow,text=button_text,font=('roman',15,'bold'),bg="green",command=command)
            ProductButton.grid(row=6,columnspan=2,pady=10)

            content = productTable.item(indexing)
            listData = content['values']
            productId = listData[0]
            productNameEntry.insert(0,listData[1])
            retailPriceEntry.insert(0,listData[2])
            wholesalesPriceEntry.insert(0,listData[3])
            quantityEntry.insert(0,listData[4])
            expiryDateEntry.insert(0,listData[5])
            productCategoryEntry.insert(0,listData[6])
        else:
            messagebox.showerror('Error', f'No product selected')
            return

    if title == 'Add Product':
        entryWindow = Toplevel()
        entryWindow.title(title)
        entryWindow.grab_set()
        entryWindow.resizable(False,False)
        entryWindow.configure(bg='lightgreen')

        productNameLabel = Label(entryWindow,text='Product Name',font=('times new roman',20,'bold'),bg='lightgreen')
        productNameLabel.grid(row=0,column=0,padx=30,pady=15,sticky=W)
        productNameEntry = Entry(entryWindow,font=('roman',15,'bold'))
        productNameEntry.grid(row=0,column=1,pady=15,padx=10)

        retailPriceLabel = Label(entryWindow,text='Retail Price',font=('times new roman',20,'bold'),bg='lightgreen')
        retailPriceLabel.grid(row=1,column=0,padx=30,pady=15,sticky=W)
        retailPriceEntry = Entry(entryWindow,font=('roman',15,'bold'))
        retailPriceEntry.grid(row=1,column=1,pady=15,padx=10)

        wholesalesPriceLabel = Label(entryWindow,text='Wholesales Price',font=('times new roman',20,'bold'),bg='lightgreen')
        wholesalesPriceLabel.grid(row=2,column=0,padx=30,pady=15,sticky=W)
        wholesalesPriceEntry = Entry(entryWindow,font=('roman',15,'bold'))
        wholesalesPriceEntry.grid(row=2,column=1,pady=15,padx=10)

        quantityLabel = Label(entryWindow,text='Quantity',font=('times new roman',20,'bold'),bg='lightgreen')
        quantityLabel.grid(row=3,column=0,padx=30,pady=15,sticky=W)
        quantityEntry = Entry(entryWindow,font=('roman',15,'bold'))
        quantityEntry.grid(row=3,column=1,pady=15,padx=10)

        expiryDateLabel = Label(entryWindow,text='Expiry Date',font=('times new roman',20,'bold'),bg='lightgreen')
        expiryDateLabel.grid(row=4,column=0,padx=30,pady=15,sticky=W)
        expiryDateEntry = DateEntry(entryWindow,font=('roman',15,'bold'),date_pattern="yyyy-mm-dd")
        expiryDateEntry.grid(row=4,column=1,pady=15,padx=10)

        productCategoryLabel = Label(entryWindow,text='Product Category',font=('times new roman',20,'bold'),bg='lightgreen')
        productCategoryLabel.grid(row=5,column=0,padx=30,pady=15,sticky=W)
        productCategoryEntry = ttk.Combobox(entryWindow,values=['Drug','Supermarket'],font=('roman',15,'bold'))
        productCategoryEntry.grid(row=5,column=1,pady=15,padx=10)

        ProductButton = tk.Button(entryWindow,text=button_text,font=('roman',15,'bold'),bg="green",command=command)
        ProductButton.grid(row=6,columnspan=2,pady=10)

def add_data():
    if productNameEntry.get()=='' or retailPriceEntry.get()=='' or wholesalesPriceEntry.get()=='' \
        or quantityEntry.get()=='' or expiryDateEntry.get()=='' or productCategoryEntry.get()=='':
        messagebox.showerror('Error','All fields are required',parent=entryWindow)
    else:
        try:
            query = 'SELECT MAX(productId) FROM products'
            myCursor.execute(query)
            max_id = myCursor.fetchone()[0]
            new_product_id = max_id + 1 if max_id else 1

            query = 'INSERT into products (productId,productName,retailPrice,wholesalesPrice,quantity,expiryDate,\
                productCategory) VALUES (?,?,?,?,?,?,?)'
            myCursor.execute(query, (new_product_id,productNameEntry.get(),retailPriceEntry.get(),\
                     wholesalesPriceEntry.get(), quantityEntry.get(), expiryDateEntry.get(),productCategoryEntry.get()))
            con.commit()
            
            result = messagebox.askyesno('Confirm','Data added successfully. Do you want to clean the form?')
            if result:
                productNameEntry.delete(0, END)
                retailPriceEntry.delete(0, END)
                wholesalesPriceEntry.delete(0, END)
                quantityEntry.delete(0, END)
                expiryDateEntry.delete(0, END)
                productCategoryEntry.delete(0, END)
            else:
                pass
        except:
            messagebox.showerror('Error','An error occurred while adding data',parent=entryWindow)
            return
        show_product()

def search_by_name():
    def enter():
        query = 'SELECT * FROM products WHERE LOWER(productName) LIKE LOWER(?)'
        myCursor.execute(query, ('%' + nameSearchEntry.get()+ '%',))
        productTable.delete(*productTable.get_children())
        fetchedData = myCursor.fetchall()
        if not fetchedData:
            messagebox.showerror('Error', 'No match')
        for data in fetchedData:
            productTable.insert('', END, values=data)

    entryWindow = Toplevel()
    entryWindow.title("Search product by name")
    entryWindow.grab_set()
    entryWindow.resizable(False,False)
    entryWindow.configure(bg='lightgreen')

    nameSearchLabel = Label(entryWindow,text='Enter Name',font=('times new roman',20,'bold'),bg='lightgreen')
    nameSearchLabel.grid(row=0,column=0,padx=30,pady=15,sticky=W)
    nameSearchEntry = Entry(entryWindow,font=('roman',15,'bold'))
    nameSearchEntry.grid(row=0,column=1,pady=15,padx=10)
    enterButton = tk.Button(entryWindow,text='Enter',width=20,font=('arial',12,'bold'),bg='green',command=enter)
    enterButton.grid(row=1,column=1,pady=15,padx=10)

def expiry_check():
    def enter():
        query ='SELECT * from products where julianday(expiryDate) - julianday() <= ?;'
        myCursor.execute(query, (int(expiringEntry.get()),))
        productTable.delete(*productTable.get_children())
        fetchedData = myCursor.fetchall()
        if not fetchedData:
            messagebox.showerror('Error', 'No match')
        for data in fetchedData:
            productTable.insert('', END, values=data)

    entryWindow = Toplevel()
    entryWindow.title("Expiring product")
    entryWindow.grab_set()
    entryWindow.resizable(False,False)
    entryWindow.configure(bg='lightgreen')

    expiringLabel = Label(entryWindow,text='No of days',font=('times new roman',20,'bold'),bg='lightgreen')
    expiringLabel.grid(row=0,column=0,padx=30,pady=15,sticky=W)
    expiringEntry = Entry(entryWindow,font=('roman',15,'bold'))
    expiringEntry.grid(row=0,column=1,pady=15,padx=10)
    enterButton = tk.Button(entryWindow,text='Enter',width=20,font=('arial',12,'bold'),bg='green',command=enter)
    enterButton.grid(row=1,column=1,pady=15,padx=10)

def check_stock():
    def enter():
        query = 'SELECT * FROM products WHERE quantity<=?'
        myCursor.execute(query,(quantitySearchEntry.get(),))
        productTable.delete(*productTable.get_children())
        fetchedData = myCursor.fetchall()
        if not fetchedData:
            messagebox.showerror('Error', 'No match')
        for data in fetchedData:
            productTable.insert('', END, values=data)

    entryWindow = Toplevel()
    entryWindow.title("Search product by quantity")
    entryWindow.grab_set()
    entryWindow.resizable(False,False)
    entryWindow.configure(bg='lightgreen')

    quantitySearchLabel = Label(entryWindow,text='Enter Quantity',font=('times new roman',20,'bold'),bg='lightgreen')
    quantitySearchLabel.grid(row=0,column=0,padx=30,pady=15,sticky=W)
    quantitySearchEntry = Entry(entryWindow,font=('roman',15,'bold'))
    quantitySearchEntry.grid(row=0,column=1,pady=15,padx=10)
    enterButton = tk.Button(entryWindow,text='Enter',width=20,font=('arial',12,'bold'),bg='green',command=enter)
    enterButton.grid(row=1,column=1,pady=15,padx=10)

def delete_product():
    result = messagebox.askyesno('Confirm','Do you want to delete?')
    if result:
        try:
            indexing = productTable.focus()
            content = productTable.item(indexing)
            contentId = content['values'][0]
            contentIdInt = int(contentId)
            query = 'DELETE FROM products WHERE productId = ?'
            myCursor.execute(query,(contentIdInt,))
            con.commit()
            messagebox.showinfo('Deleted',f'The product with product Id {contentIdInt} is deleted succesfully')
            show_product()
        except Exception as e:
            messagebox.showerror('Error', f'No product selected')

def show_product():
    query = 'SELECT * FROM products'
    myCursor.execute(query)
    fetchedData = myCursor.fetchall()
    productTable.delete(*productTable.get_children())
    for data in fetchedData:
        productTable.insert('',END,values=data)

def view_product():
    indexing = productTable.focus()
    contents = productTable.item(indexing)
    if indexing:
        # product info window
        popInfo = Toplevel()
        popInfo.title('Product info')
        popInfo.grab_set()
        #popInfo.geometry("500x300")
        popInfo.resizable(False,False)
        popInfo.configure(bg='lightgreen')

        # Display the product info
        l1=tk.Label(popInfo,font=('Times',22,'bold'),fg='black',bg='lightgreen')
        l1.grid(row=1,column=0,pady=5,sticky=W)
        l2=tk.Label(popInfo,font=('Times',22,'bold'),fg='black',bg='lightgreen')
        l2.grid(row=2,column=0,pady=5,sticky=W)
        l3=tk.Label(popInfo,font=('Times',22,'bold'),fg='black',bg='lightgreen')
        l3.grid(row=3,column=0,pady=5,sticky=W)
        l4=tk.Label(popInfo,font=('Times',22,'bold'),fg='black',bg='lightgreen')
        l4.grid(row=4,column=0,pady=5,sticky=W)
        l5=tk.Label(popInfo,font=('Times',22,'bold'),fg='black',bg='lightgreen')
        l5.grid(row=5,column=0,pady=5,sticky=W)
        l6=tk.Label(popInfo,font=('Times',22,'bold'),fg='black',bg='lightgreen')
        l6.grid(row=6,column=0,pady=5,sticky=W)

        # Display the right values of the product
        l1.config(text=f"{nameField[1]}: {contents['values'][1]}")
        l2.config(text=f"{nameField[2]}: #{contents['values'][2]}")
        l3.config(text=f"{nameField[3]}: #{contents['values'][3]}")
        l4.config(text=f"{nameField[4]}: {contents['values'][4]}")
        l5.config(text=f"{nameField[5]}: {contents['values'][5]}")
        l6.config(text=f"{nameField[6]}: {contents['values'][6]}")
        
    else:
        messagebox.showerror('Error', f'No product selected')

def update_data():
    query = 'UPDATE products SET productName=?,retailPrice=?,wholesalesPrice=?,quantity=?,expiryDate=? \
            ,productCategory=? where productId=?'
    myCursor.execute(query,(productNameEntry.get(),retailPriceEntry.get(),wholesalesPriceEntry.get(),\
                        quantityEntry.get(),expiryDateEntry.get(),productCategoryEntry.get(),productId))
    con.commit()
    messagebox.showinfo('Success',f'Product {productNameEntry.get()} is modified successfully',parent=entryWindow)
    entryWindow.destroy()
    show_product()

def export_data():
    url = filedialog.asksaveasfilename(defaultextension='.csv')
    indexing = productTable.get_children()
    newList = []
    for index in indexing:
        content = productTable.item(index)
        dataList = content['values']
        newList.append(dataList)
    table = pandas.DataFrame(newList,columns=['Product Id','Product Name','Retail Price','Wholesales Price','Quantity',
                                                'Expiry Date','Product Category'])
    table.to_csv(url,index=False)
    messagebox.showinfo('Success','Data saved successfully')


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

#====================================================================================

#Gui part
root = tk.Toplevel()
root.geometry('1174x700')
root.title('Products')
root.configure(bg='lightgreen')

datetimeLabel = Label(root,font=('times new roman',18,'bold'),fg="green",bg='lightgreen')
datetimeLabel.place(x=5,y=5)
clock()

slide = 'Alan Pharmacy and Supermarket'
sliderLabel = Label(root,font=('aerial',18,'italic bold'),width=50,fg="green",bg='lightgreen')
sliderLabel.place(x=200,y=0)
slider()

#Sidebar menu frame
leftFrame = Frame(root,bg='lightgreen')
leftFrame.place(x=50,y=80,width=300,height=600)

logoImage = PhotoImage(file='images/work.png')
logoLabel = Label(leftFrame,image=logoImage,bg='lightgreen')
logoLabel.grid(row=0,column=0)
 
addProductButton = tk.Button(leftFrame,text='Add product',width=20,font=('arial',12,'bold'),bg='green',command=lambda :toplevel_data('Add Product','Add product',add_data))
addProductButton.grid(row=1,column=0,pady=10)

searchProductButton = tk.Button(leftFrame,text='Search product by name',width=20,font=('arial',12,'bold'),bg='lime green',command=(search_by_name))
searchProductButton.grid(row=2,column=0,pady=10)

updateProductButton = tk.Button(leftFrame,text='Update product',width=20,font=('arial',12,'bold'),bg='green',command=lambda :toplevel_data('Update Product','Update Product',update_data))
updateProductButton.grid(row=3,column=0,pady=10)

showProductButton = tk.Button(leftFrame,text='Show products',width=20,font=('arial',12,'bold'),bg='lime green',command=show_product)
showProductButton.grid(row=4,column=0,pady=10)

viewProductButton = tk.Button(leftFrame,text='View product',width=20,font=('arial',12,'bold'),bg='green',command=view_product)
viewProductButton.grid(row=5,column=0,pady=10)

exportDataButton = tk.Button(leftFrame,text='Export data',width=20,font=('arial',12,'bold'),bg='lime green',command=export_data)
exportDataButton.grid(row=6,column=0,pady=10)

deleteProductButton = tk.Button(leftFrame,text='Delete product',width=20,font=('arial',12,'bold'),bg='red',command=delete_product)
deleteProductButton.grid(row=7,column=0,pady=10)

expProdButton = tk.Button(leftFrame,text='Expiring product',width=20,font=('arial',12,'bold'),bg='green',command=expiry_check)
expProdButton.grid(row=8,column=0,pady=10)

exitButton = tk.Button(leftFrame,text='Check Stock',width=20,font=('arial',12,'bold'),bg='lime green',command=check_stock)
exitButton.grid(row=9,column=0,pady=10)

# Treeview Frame
rightFrame = Frame(root)
rightFrame.place(x=350,y=80,width=1000,height=600)

scrollBarX = Scrollbar(rightFrame,orient=HORIZONTAL)
scrollBarY = Scrollbar(rightFrame,orient=VERTICAL)

productTable = ttk.Treeview(rightFrame,columns=('Product Id','Product Name','Retail Price','Wholesales Price',
                                'Quantity','Expiry Date','Product Category'),
                            xscrollcommand=scrollBarX.set,yscrollcommand=scrollBarY.set)

scrollBarX.config(command=productTable.xview)
scrollBarY.config(command=productTable.yview)

scrollBarX.pack(side=BOTTOM,fill=X)
scrollBarY.pack(side=RIGHT,fill=Y)

productTable.pack(fill=BOTH,expand=1)

for i in range(0, len(nameField)):
    productTable.heading(nameField[i],text=nameField[i])
productTable.config(show='headings')
productTable.column('Product Id',width=90,anchor='w')
productTable.column('Product Name',width=450,anchor='w')
productTable.column('Retail Price',anchor='w')
productTable.column('Wholesales Price',anchor='w')
productTable.column('Quantity',anchor='w')
productTable.column('Expiry Date',anchor='w')
productTable.column('Product Category',anchor='w')

style = ttk.Style(rightFrame)
style.theme_use("clam") # set theme to clam
style.configure("Treeview", background="azure2", 
                fieldbackground="lightyellow", foreground="black",font='black')
style.configure('Treeview.Heading', background="lime green")

root.mainloop()