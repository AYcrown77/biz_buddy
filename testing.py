import tkinter as tk
from tkinter import ttk

def on_select(event):
    # Get the current value in the combobox
    current_value = combobox.get()

    # Filter the list of items based on the current input
    filtered_items = [item for item in all_items if current_value.lower() in item.lower()]

    # Update the combobox with the filtered list
    combobox['values'] = filtered_items

root = tk.Tk()
root.title("Auto-Complete Combobox Example")

# Sample data
all_items = ["Apple", "Banana", "Cherry", "Date", "Grape", "Lemon", "Lime", "Orange"]

# Variable to store the current value in the combobox
current_value = tk.StringVar()

# Combobox with auto-complete feature
combobox = ttk.Combobox(root, textvariable=current_value)
combobox['values'] = all_items
combobox.pack(padx=10, pady=10)
combobox.bind('<KeyRelease>', on_select)

root.mainloop()