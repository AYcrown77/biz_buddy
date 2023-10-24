import tkinter as tk
import ttkbootstrap as ttk
from tkinter import *
import sqlite3

my_w = tk.Tk()
my_w.geometry("560x450")  # Size of the window
my_w.title("www.plus2net.com")  # Adding a title

con = sqlite3.connect('alan_pharm_supermarket.db')
myCursor = con.cursor()

query = 'CREATE TABLE IF NOT EXISTS product_purchase (\
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,\
            p_id INTEGER NOT NULL,\
            product VARCHAR(20) NOT NULL,\
            price FLOAT NOT NULL,\
            qty INTEGER NOT NULL,\
            dt DATE NOT NULL)'
myCursor.execute(query)

query = "SELECT productId,productName FROM products"
my_data = list(myCursor.execute(query))
my_dict = {}
p_id, p_name = 0, ""

for row in my_data:
    my_dict[row[0]] = row[1]  # dictionay with key as p_id

def my_upd(*args):
    my_dict = {}
    query = ("SELECT productId,productName FROM products WHERE productName like :e1")
    # data=cb1.get()
    print(query)
    my_data = list(myCursor.execute(query, e1="?" + cb1.get() + "?"))
    cb1["values"] = []
    for row in my_data:
        my_dict[row[0]] = row[1]
    print(my_data)
    cb1["values"] = list(my_dict.values())
    l1.config(text="Number records : " + str(len(my_data)))


def my_disp(*args):
    global p_id, p_name
    l1.config(text="")
    for i, j in my_dict.items():
        if j == sel.get():
            p_id, p_name = i, j
            l1.config(text=" Product ID: " + str(i) + " \n Product: " + j)
            break


def my_insert():
    global p_id, p_name
    query = "INSERT INTO product_purchase (p_id,product,price,qty,dt) \
           VALUES(?,?,?,?,?)"
    data = (p_id, p_name, price_v.get(), quantity_v.get(), dt.entry.get())
    # print(query,my_data)
    id = myCursor.execute(query, data)
    l1.config(text="Data inserted ID: " + str(id.lastrowid), bootstyle="success")
    l1.after(3000, lambda: my_reset())


def my_reset():
    cb1.delete(0, "end")
    price_v.set(0)
    quantity_v.set(1)
    l1.config(text="Ready", bootstyle="inverse-warning")


font1 = ["Times", 50, "normal"]
l_top = ttk.Label(
    my_w,
    text="Procurement",
    bootstyle="inverse-info",
    font=font1,
    anchor="center",
    width=15,
)
l_top.grid(row=0, column=1, columnspan=3, padx=20, pady=10)
l_product = ttk.Label(
    text="Product", bootstyle="inverse-primary", anchor="sw", width=15, font=20
)
l_product.grid(row=1, column=1, padx=10, pady=10)

l_price = ttk.Label(
    text="Price", bootstyle="inverse-primary", anchor="sw", width=15, font=20
)
l_price.grid(row=2, column=1, padx=10, pady=10)

l_qty = ttk.Label(
    text="Quantity", bootstyle="inverse-primary", anchor="sw", width=15, font=20
)
l_qty.grid(row=3, column=1, padx=10, pady=10)

l_date = ttk.Label(
    text="Date", bootstyle="inverse-primary", anchor="sw", width=15, font=20
)
l_date.grid(row=4, column=1, padx=10, pady=10)

sel = tk.StringVar()
cb1 = ttk.Combobox(
    my_w, textvariable=sel, values=list(my_dict.values()), bootstyle="success"
)
cb1.grid(row=1, column=2, padx=5, pady=10)
price_v = ttk.DoubleVar(value=0)
price = ttk.Entry(my_w, textvariable=price_v, bootstyle="success")
price.grid(row=2, column=2, padx=10, pady=10)
quantity_v = ttk.IntVar(value=1)
quantity = ttk.Entry(my_w, textvariable=quantity_v, bootstyle="success")
quantity.grid(row=3, column=2, padx=10, pady=10)
dt = ttk.DateEntry(my_w, dateformat="%Y-%m-%d", bootstyle="success")
dt.grid(row=4, column=2, padx=10, pady=10)

l1 = ttk.Label(my_w, text="Details", bootstyle="inverse-warning", font=12, width=20)
l1.grid(row=1, column=3)

b1 = ttk.Button(my_w, text="Submit", command=lambda: my_insert(), bootstyle="success")
b1.grid(row=5, column=2, padx=10, pady=20)
#sel.trace("w", my_upd)  # trigger on change event of Combobox
cb1.bind("<KeyRelease>", my_upd)
cb1.bind("<FocusOut>", my_disp)
my_w.mainloop()  # Keep the window open