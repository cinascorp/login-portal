
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
label1.pack(pady=5)
label2 = tk.Label(frame1, text="Password:")
label1.pack(pady=5)
# -----------------------------Create the entry boxes--------------------------
entry1 = tk.Entry(frame1)
entry2 = tk.Entry(frame1, show="*")
#-------------------------------- Create the buttons---------------------------
button1 = tk.Button(frame2, text="Login", command=lambda: login())
button2 = tk.Button(frame2, text="Sign Up", command=lambda: re_window())
button1.pack(pady=20)
#==============================Create the database=============================
users = {
    "admin": "123456789"
}
#==========================register window for submit==========================
#------------------submit function
def re_window():
    root.destroy()
    # Create a database if it does not exist
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    # Create a table if it does not exist
    c.execute("CREATE TABLE IF NOT EXISTS user_list (username TEXT, password TEXT, user_address TEXT, user_number INTEGER)")
    # Function to close the root window and open the register window    
    re_window = tk.Tk()
    re_window.title("Submit")
    re_window.geometry("280x180")
    # Create labels for the register window
    username_label = tk.Label(re_window, text="Username")
    username_label.grid(row=0, column=0)
    password_label = tk.Label(re_window, text="Password")
    password_label.grid(row=1, column=0)
    confirm_password_label = tk.Label(re_window, text="Confirm Password")
    confirm_password_label.grid(row=2, column=0)
    user_address_label = tk.Label(re_window, text="User Address")
    user_address_label.grid(row=3, column=0)
    user_number_label = tk.Label(re_window, text="User Number")
    user_number_label.grid(row=4, column=0)
    # Create entry boxes for the register window
    username_entry = tk.Entry(re_window)
    username_entry.grid(row=0, column=1)
    password_entry = tk.Entry(re_window)
    password_entry.grid(row=1, column=1)
    confirm_password_entry = tk.Entry(re_window)
    confirm_password_entry.grid(row=2, column=1)
    user_address_entry = tk.Entry(re_window)
    user_address_entry.grid(row=3, column=1)
    user_number_entry = tk.Entry(re_window)
    user_number_entry.grid(row=4, column=1)
    # Error for re_window
    error2_label = tk.Label(re_window, text='some thing is wrong')
    error2_label.grid(row=9, columnspan=1 )
    #======================== Function to get the values from the entry boxes and save them in the database
    def submit():
        try:
            # Get the values from the entry boxes
            username = username_entry.get()
            password = password_entry.get()
            confirm_password = confirm_password_entry.get()
            user_address = user_address_entry.get()
            user_number = user_number_entry.get()
            # Check if the passwords match and the user is not already in the database
            if password == confirm_password and (username) not in c.execute("SELECT * FROM user_list").fetchall():
                # Check if the user is not an admin
                if username != "admin":       
                    # Insert the values into the database
                    c.execute("INSERT INTO user_list VALUES (?, ?, ?, ?)", (username, password, user_address, user_number))
                    conn.commit()
                    conn.close()
            else:
                error2_label.config(re_window, text='  Error  :   Iwrong input',fg="red")
        except:
            error2_label.config(re_window, text='  Error  :   Iwrong input',fg="red")
            
    submit_button = tk.Button(re_window, text="Submit", command=submit)
    submit_button.grid(row=9, column=1)
#============================= Create the functions============================
def login():
    username = entry1.get()
    password = entry2.get()
    if username in users and users[username] == password:
        messagebox.showinfo("Login Successful", "Welcome!")
        #==============================sugn up===============
        re_window
    else:
        messagebox.showerror("Login Failed", "Incorrect username or password")
#------------------------------ sign up       
def signup():
   
    username = entry1.get()
    if username not in users:
        messagebox.showinfo("Sign Up Successful", "Welcome!")
        return re_window
    else:
        messagebox.showerror("Sign Up Failed", "Username already taken")   
#================================ shop ========================================
def edit():
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
            c.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
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
            c.execute("DELETE FROM users WHERE name=?", (name,))
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
            c.execute("UPDATE users SET age=? WHERE name=?", (age, name))
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
        c.execute("SELECT * FROM users")
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
def shop():
   
    #--------- -----------Create the root window
    shop = tk.Tk()
    #----------------------- Set window title
    shop.title("Shop")
    # ------------------------Set window size
    shop.geometry("400x200")
    # -----------------------Create the frames
    shop_frame1 = tk.Frame(shop)
    shop_frame2 = tk.Frame(shop)
    # ------------------------Create the labels
    shop_label1 = tk.Label(shop_frame1, text="Welcome to the candy shop!")
    #----------------------- Create the buttons
    shop_button1 = tk.Button(shop_frame2, text="Browse Products")
    shop_button2 = tk.Button(shop_frame2, text="Edit account ", command=lambda: edit())
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

