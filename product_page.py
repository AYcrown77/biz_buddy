from tkinter import *
import time
import ttkthemes
from tkinter import ttk,messagebox,filedialog
import sqlite3
import pandas

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
        
            productNameLabel = Label(entryWindow,text='Product Name',font=('times new roman',20,'bold'))
            productNameLabel.grid(row=0,column=0,padx=30,pady=15,sticky=W)
            productNameEntry = Entry(entryWindow,font=('roman',15,'bold'))
            productNameEntry.grid(row=0,column=1,pady=15,padx=10)

            retailPriceLabel = Label(entryWindow,text='Retail Price',font=('times new roman',20,'bold'))
            retailPriceLabel.grid(row=1,column=0,padx=30,pady=15,sticky=W)
            retailPriceEntry = Entry(entryWindow,font=('roman',15,'bold'))
            retailPriceEntry.grid(row=1,column=1,pady=15,padx=10)

            wholesalesPriceLabel = Label(entryWindow,text='Wholesales Price',font=('times new roman',20,'bold'))
            wholesalesPriceLabel.grid(row=2,column=0,padx=30,pady=15,sticky=W)
            wholesalesPriceEntry = Entry(entryWindow,font=('roman',15,'bold'))
            wholesalesPriceEntry.grid(row=2,column=1,pady=15,padx=10)

            quantityLabel = Label(entryWindow,text='Quantity',font=('times new roman',20,'bold'))
            quantityLabel.grid(row=3,column=0,padx=30,pady=15,sticky=W)
            quantityEntry = Entry(entryWindow,font=('roman',15,'bold'))
            quantityEntry.grid(row=3,column=1,pady=15,padx=10)

            expiryDateLabel = Label(entryWindow,text='Expiry Date',font=('times new roman',20,'bold'))
            expiryDateLabel.grid(row=4,column=0,padx=30,pady=15,sticky=W)
            expiryDateEntry = Entry(entryWindow,font=('roman',15,'bold'))
            expiryDateEntry.grid(row=4,column=1,pady=15,padx=10)

            productCategoryLabel = Label(entryWindow,text='Product Category',font=('times new roman',20,'bold'))
            productCategoryLabel.grid(row=5,column=0,padx=30,pady=15,sticky=W)
            productCategoryEntry = Entry(entryWindow,font=('roman',15,'bold'))
            productCategoryEntry.grid(row=5,column=1,pady=15,padx=10)

            ProductButton = ttk.Button(entryWindow,text=button_text,command=command)
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

    if title != 'Update Product':
        entryWindow = Toplevel()
        entryWindow.title(title)
        entryWindow.grab_set()
        entryWindow.resizable(False,False)

        productNameLabel = Label(entryWindow,text='Product Name',font=('times new roman',20,'bold'))
        productNameLabel.grid(row=0,column=0,padx=30,pady=15,sticky=W)
        productNameEntry = Entry(entryWindow,font=('roman',15,'bold'))
        productNameEntry.grid(row=0,column=1,pady=15,padx=10)

        retailPriceLabel = Label(entryWindow,text='Retail Price',font=('times new roman',20,'bold'))
        retailPriceLabel.grid(row=1,column=0,padx=30,pady=15,sticky=W)
        retailPriceEntry = Entry(entryWindow,font=('roman',15,'bold'))
        retailPriceEntry.grid(row=1,column=1,pady=15,padx=10)

        wholesalesPriceLabel = Label(entryWindow,text='Wholesales Price',font=('times new roman',20,'bold'))
        wholesalesPriceLabel.grid(row=2,column=0,padx=30,pady=15,sticky=W)
        wholesalesPriceEntry = Entry(entryWindow,font=('roman',15,'bold'))
        wholesalesPriceEntry.grid(row=2,column=1,pady=15,padx=10)

        quantityLabel = Label(entryWindow,text='Quantity',font=('times new roman',20,'bold'))
        quantityLabel.grid(row=3,column=0,padx=30,pady=15,sticky=W)
        quantityEntry = Entry(entryWindow,font=('roman',15,'bold'))
        quantityEntry.grid(row=3,column=1,pady=15,padx=10)

        expiryDateLabel = Label(entryWindow,text='Expiry Date',font=('times new roman',20,'bold'))
        expiryDateLabel.grid(row=4,column=0,padx=30,pady=15,sticky=W)
        expiryDateEntry = Entry(entryWindow,font=('roman',15,'bold'))
        expiryDateEntry.grid(row=4,column=1,pady=15,padx=10)

        productCategoryLabel = Label(entryWindow,text='Product Category',font=('times new roman',20,'bold'))
        productCategoryLabel.grid(row=5,column=0,padx=30,pady=15,sticky=W)
        productCategoryEntry = Entry(entryWindow,font=('roman',15,'bold'))
        productCategoryEntry.grid(row=5,column=1,pady=15,padx=10)

        ProductButton = ttk.Button(entryWindow,text=button_text,command=command)
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
            
def search_data():
    query = 'SELECT * FROM products where productName=? or retailPrice=? or wholesalesPrice=? or quantity=? \
            or expiryDate=? or productCategory=?'
    myCursor.execute(query,(productNameEntry.get(),retailPriceEntry.get(),wholesalesPriceEntry.get(),\
                            quantityEntry.get(),expiryDateEntry.get(),productCategoryEntry.get()))
    productTable.delete(*productTable.get_children())
    fetchedData = myCursor.fetchall()
    if not fetchedData:
        messagebox.showerror('Error', f'No match')

    for data in fetchedData:
        productTable.insert('',END,values=data)

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
            query = 'SELECT * FROM products'
            myCursor.execute(query)
            fetchedData = myCursor.fetchall()
            productTable.delete(*productTable.get_children())
            for data in fetchedData:
                productTable.insert('',END,values=data)
        except Exception as e:
            messagebox.showerror('Error', f'No product selected')
    else:
        pass

def show_product():
    query = 'SELECT * FROM products'
    myCursor.execute(query)
    fetchedData = myCursor.fetchall()
    productTable.delete(*productTable.get_children())
    for data in fetchedData:
        productTable.insert('',END,values=data)

def update_data():
    query = 'update products set productName=?,retailPrice=?,wholesalesPrice=?,quantity=?,expiryDate=? \
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
root.title('Products')
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
 
addProductButton = ttk.Button(leftFrame,text='Add product',width=20,command=lambda :toplevel_data('Add Product','Add product',add_data))
addProductButton.grid(row=1,column=0,pady=10)

searchProductButton = ttk.Button(leftFrame,text='Search product',width=20,command=lambda :toplevel_data('Search Product','Search Product',search_data))
searchProductButton.grid(row=2,column=0,pady=10)

updateProductButton = ttk.Button(leftFrame,text='Update product',width=20,command=lambda :toplevel_data('Update Product','Update Product',update_data))
updateProductButton.grid(row=3,column=0,pady=10)

showProductButton = ttk.Button(leftFrame,text='Show product',width=20,command=show_product)
showProductButton.grid(row=4,column=0,pady=10)

exportDataButton = ttk.Button(leftFrame,text='Export data',width=20,command=export_data)
exportDataButton.grid(row=5,column=0,pady=10)

deleteProductButton = ttk.Button(leftFrame,text='Delete product',width=20,command=delete_product)
deleteProductButton.grid(row=6,column=0,pady=10)

exitButton = ttk.Button(leftFrame,text='Exit',width=20,command=to_exit)
exitButton.grid(row=7,column=0,pady=10)

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

productTable.column('Product Id',width=100,anchor=CENTER)
productTable.column('Product Name',width=300,anchor=CENTER)
productTable.column('Retail Price',anchor=CENTER)
productTable.column('Wholesales Price',anchor=CENTER)
productTable.column('Quantity',anchor=CENTER)
productTable.column('Expiry Date',anchor=CENTER)
productTable.column('Product Category',anchor=CENTER)

style = ttk.Style()
style.configure('Treeview',rowheight=25,font=('arial',12,'bold'),
                foreground='green',background='black',fieldbackground='green')
style.configure('Treeview.Heading',font=('arial',14,'bold'),foreground='green')

root.mainloop()