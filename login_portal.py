import tkinter as tk
from tkinter import messagebox
import sqlite3

#============================ Create the root window===========================
root = tk.Tk()
#------------------------------- Set window title------------------------------
root.title("Login Portal")
#-------------------------------- Set window size------------------------------
root.geometry("400x200")
#------------------------------- Create the frames-----------------------------
frame1 = tk.Frame(root)
frame2 = tk.Frame(root)
#------------------------------- Create the labels-----------------------------
label1 = tk.Label(frame1, text="Username:")
label2 = tk.Label(frame1, text="Password:")
# -----------------------------Create the entry boxes--------------------------
entry1 = tk.Entry(frame1)
entry2 = tk.Entry(frame1, show="*")
#-------------------------------- Create the buttons---------------------------

button1 = tk.Button(frame2, text="Login", command=lambda: login())
button2 = tk.Button(frame2, text="Sign Up", command=lambda: signup())

#==============================Create the database=============================
users = {
    "admin": "123456789"
}
#============================= Create the functions============================
def login():
    username = entry1.get()
    password = entry2.get()

    if username in users and users[username] == password:
        messagebox.showinfo("Login Successful", "Welcome!")
        root.destroy()
        shop()
    else:
        messagebox.showerror("Login Failed", "Incorrect username or password")
#------------------------------ sign up       
def signup():
    
    username = entry1.get()
    password = entry2.get()
    if username not in users:
        users[username] = password
        messagebox.showinfo("Sign Up Successful", "Welcome!")
    else:
        messagebox.showerror("Sign Up Failed", "Username already taken")
#================================ shop ========================================
def shop():
    #--------- -----------Create the root window
    shop = tk.Tk()
    #----------------------- Set window title
    shop.title("Shop")
    # ------------------------Set window size
    shop.geometry("400x400")
    # -----------------------Create the frames
    shop_frame1 = tk.Frame(shop)
    shop_frame2 = tk.Frame(shop)
    # ------------------------Create the labels
    shop_label1 = tk.Label(shop_frame1, text="Welcome to the shop!")
    #----------------------- Create the buttons
    shop_button1 = tk.Button(shop_frame2, text="Browse Products")
    shop_button2 = tk.Button(shop_frame2, text="Checkout")
    #-------------------------- Pack the frames
    shop_frame1.pack()
    shop_frame2.pack()
    # --------------------------Pack the labels
    shop_label1.pack()
    #------------------------ Pack the buttons
    shop_button1.pack(side="left")
    shop_button2.pack(side="right")
    # -------------------------Run the main loop
    shop.mainloop()
#------------------------------- Pack the frames-------------------------------
frame1.pack()
frame2.pack()
# -------------------------------Pack the labels-------------------------------
label1.pack()
label2.pack()
#----------------------------- Pack the entry boxes----------------------------
entry1.pack()
entry2.pack()
# ------------------------------Pack the buttons-------------------------------
button1.pack(side="left")
button2.pack(side="right")
#------------------------------ Run the main loop------------------------------
root.mainloop()
#############################  Cinas Coreopratio  #############################
#############################  just for training  #############################
#############################  Cinas Coreopratio  #############################
#------------------------------------------ Create a connection to the database
conn = sqlite3.connect('database.db')
# --------------------------------Create a cursor to interact with the database
c = conn.cursor()
# --------------------------------------------------------------Create a window
window = tk.Tk()
window.title("Database App")
window.geometry("400x400")

#--------------------------------------------------------------- Create a label
label = tk.Label(text="Welcome to the Database App!")
label.pack()

# --------------------------------Create a function to add data to the database
def add_data():
    #------------------------------------------------------ Create a new window
    add_window = tk.Toplevel(window)
    add_window.title("Add Data")
    add_window.geometry("400x400")

    #-------------------------------------------- Create labels and entry boxes
    name_label = tk.Label(add_window, text="Name")
    name_label.pack()
    name_entry = tk.Entry(add_window)
    name_entry.pack()

    age_label = tk.Label(add_window, text="Age")
    age_label.pack()
    age_entry = tk.Entry(add_window)
    age_entry.pack()

    # ----------------------------Create a function to add data to the database
    def add_data_to_database():
        # ------------------------------------Get the data from the entry boxes
        name = name_entry.get()
        age = age_entry.get()

        #----------------------------------------- Add the data to the database
        c.execute("INSERT INTO people (name, age) VALUES (?, ?)", (name, age))
        conn.commit()

        #--------------------------------------------------- Show a message box
        messagebox.showinfo("Success", "Data added successfully!")

    # ------------------------------Create a button to add data to the database
    add_data_button = tk.Button(add_window, text="Add Data", command=add_data_to_database)
    add_data_button.pack()

#--------------------------- Create a function to delete data from the database
def delete_data():
    #------------------------------------------------------ Create a new window
    delete_window = tk.Toplevel(window)
    delete_window.title("Delete Data")
    delete_window.geometry("400x400")

    #-------------------------------------------- Create labels and entry boxes
    name_label = tk.Label(delete_window, text="Name")
    name_label.pack()
    name_entry = tk.Entry(delete_window)
    name_entry.pack()

    #----------------------- Create a function to delete data from the database
    def delete_data_from_database():
        # --------------------------------------Get the data from the entry box
        name = name_entry.get()

        # ------------------------------------Delete the data from the database
        c.execute("DELETE FROM people WHERE name=?", (name,))
        conn.commit()

        #--------------------------------------------------- Show a message box
        messagebox.showinfo("Success", "Data deleted successfully!")

    # -------------------------Create a button to delete data from the database
    delete_data_button = tk.Button(delete_window, text="Delete Data", command=delete_data_from_database)
    delete_data_button.pack()

#------------------------------- Create a function to edit data in the database
def edit_data():
    #------------------------------------------------------ Create a new window
    edit_window = tk.Toplevel(window)
    edit_window.title("Edit Data")
    edit_window.geometry("400x400")

    # --------------------------------------------Create labels and entry boxes
    name_label = tk.Label(edit_window, text="Name")
    name_label.pack()
    name_entry = tk.Entry(edit_window)
    name_entry.pack()

    age_label = tk.Label(edit_window, text="Age")
    age_label.pack()
    age_entry = tk.Entry(edit_window)
    age_entry.pack()

    #--------------------------- Create a function to edit data in the database
    def edit_data_in_database():
        # Get the data from the entry boxes
        name = name_entry.get()
        age = age_entry.get()

        #---------------------------------------- Edit the data in the database
        c.execute("UPDATE people SET age=? WHERE name=?", (age, name))
        conn.commit()

        #--------------------------------------------------- Show a message box
        messagebox.showinfo("Success", "Data edited successfully!")

    #----------------------------- Create a button to edit data in the database
    edit_data_button = tk.Button(edit_window, text="Edit Data", command=edit_data_in_database)
    edit_data_button.pack()

#----------------------------- Create a function to load data from the database
def load_data():
    #------------------------------------------------------- Clear the list box
    list_box.delete(0, tk.END)
#--------------------------------------------------------------- Create buttons
    #------------------------------------------- Get the data from the database
    c.execute("SELECT * FROM people")
    data = c.fetchall()
    # -------------------------Loop through the data and add it to the list box
    for row in data:
        list_box.insert(tk.END, row)
# ------------------------------------------------------------Create a list box
list_box = tk.Listbox(window)
list_box.pack()

add_data_button = tk.Button(window, text="Add Data", command=add_data)
add_data_button.pack()
delete_data_button = tk.Button(window, text="Delete Data", command=delete_data)
delete_data_button.pack()
edit_data_button = tk.Button(window, text="Edit Data", command=edit_data)
edit_data_button.pack()
load_data_button = tk.Button(window, text="Load Data", command=load_data)
load_data_button.pack()
#=============================================================== Run the window
window.mainloop()
############################## Cinas Corporation ##############################
