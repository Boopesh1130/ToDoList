import tkinter as tk
from tkinter import messagebox
import mysql.connector

def add_task():
    task = entry_work.get()

    if not task:
        messagebox.showinfo('Notify','Please Fill The Field !!')
        return


    if task != "":
        listbox.insert(tk.END, task)
        entry_work.delete(0, tk.END) 

    conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="todo_db"
        )
    cursor = conn.cursor()

    query= '''INSERT INTO to_do_list(tasks) VALUES(%s)'''
    cursor.execute(query,(task,))
    conn.commit()

    messagebox.showinfo("Success", "Added!")


    if cursor:
        cursor.close()
    if conn:
        conn.close()
'''

def add_task():
    task = entry_work.get()

    if not task:
        messagebox.showinfo('Notify', 'Please Fill The Field !!')
        return

    # Insert task into the listbox
    listbox.insert(tk.END, task)
    entry_work.delete(0, tk.END) 

    try:
        # Connect to the MySQL database
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # Make sure to use your actual password
            database="todo_db"
        )
        cursor = conn.cursor()

        # Insert into the database
        query = INSERT INTO to_do_list(tasks) VALUES(%s)  # Assuming s_no is auto-increment
        cursor.execute(query, (task,))  # Pass task as a tuple
        conn.commit()


    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
    
    finally:
        # Ensure the cursor and connection are closed
        if cursor:
            cursor.close()
        if conn:
            conn.close()'''


def clear_tasks():
    listbox.delete(0, tk.END)  

root = tk.Tk()
root.title("To Do List")
root.geometry("1000x700")
root.config(bg="#0baaea")

# Main Window
todolist = tk.Label(root, text="To Do List", font=("calibri", 25, "bold"), bg="#0baaea", fg="white")
todolist.pack(pady=50)

# Entry widget for tasks
entry_work = tk.Entry(root, font=("Arial", 14), width=30)
entry_work.pack(pady=5)  # Changed to pack

# Listbox to display tasks
listbox = tk.Listbox(root, font=("Arial", 14), width=50, height=10)
listbox.pack(pady=5)  # Changed to pack

# Buttons to add and clear tasks
add_button = tk.Button(root, text="Add Task", font=("Arial", 14), command=add_task)
add_button.pack(pady=5)  # Changed to pack

clear_button = tk.Button(root, text="Clear Tasks", font=("Arial", 14), command=clear_tasks)
clear_button.pack(pady=5)  # Changed to pack

root.mainloop()
