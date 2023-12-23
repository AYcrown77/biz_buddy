import sqlite3

con = sqlite3.connect('alan_pharm_supermarket.db')
myCursor = con.cursor()

query = "SELECT * FROM products"
my_data = list(myCursor.execute(query))  # result set
my_dict = {}  # Create an empty dictionary
my_list = []  # Create an empty list
for row in my_data:
    my_dict[[row][0][0]] = row  # id as key
    my_list.append(row[1])  # name as list

query = "SELECT * FROM customer"
cust_data = list(myCursor.execute(query))  # result set
cust_dict = {}  # Create an empty dictionary
cust_list = []  # Create an empty list
for row in cust_data:
    cust_dict[[row][0][0]] = row  # id as key
    cust_list.append(row[1])  # name as list

query = "SELECT * FROM supplier"
sup_data = list(myCursor.execute(query))  # result set
sup_dict = {}  # Create an empty dictionary
sup_list = []  # Create an empty list
for row in sup_data:
    sup_dict[[row][0][0]] = row  # id as key
    sup_list.append(row[1])  # name as list
