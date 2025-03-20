import tkinter as tk
from tkinter import messagebox
# Create the main application window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x500")
tasks = []  # List to store tasks
# Function to add a new task
def add_task():
    task = entry_task.get()
    if task:
        tasks.append(task)
        update_listbox()
        entry_task.delete(0, tk.END)  # Clear input field
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")
# Function to delete a selected task
def delete_task():
    try:
        selected_task = listbox_tasks.curselection()[0]  # Get selected index
        tasks.pop(selected_task)
        update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "No task selected!")
# Function to update a selected task
def update_task():
    try:
        selected_task = listbox_tasks.curselection()[0]
        new_task = entry_task.get()
        if new_task:
            tasks[selected_task] = new_task
            update_listbox()
            entry_task.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")
    except IndexError:
        messagebox.showwarning("Warning", "No task selected!")
# Function to refresh the task list in the Listbox
def update_listbox():
    listbox_tasks.delete(0, tk.END)  # Clear the listbox
    for task in tasks:
        listbox_tasks.insert(tk.END, task)
# Create UI elements
entry_task = tk.Entry(root, width=40)
entry_task.pack(pady=10)
btn_add = tk.Button(root, text="Add Task", command=add_task)
btn_add.pack(pady=5)
btn_update = tk.Button(root, text="Update Task", command=update_task)
btn_update.pack(pady=5)
btn_delete = tk.Button(root, text="Delete Task", command=delete_task)
btn_delete.pack(pady=5)
listbox_tasks = tk.Listbox(root, width=50, height=15)
listbox_tasks.pack(pady=10)
# Run the Tkinter event loop
root.mainloop()