import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.ttk import Progressbar
import subprocess

def add_new_member():
    main_frame.pack_forget()
    add_member_frame.pack()

def continue_recognition():
    root.destroy()
    subprocess.run(['python', 'webcam.py'])

def delete_backup_files():
        backup_files = ['encoded-images-data.csv.bak', 'classifier.pkl.bak']
        for file in backup_files:
            file_path = os.path.join(os.getcwd(), file)
            if os.path.exists(file_path):
                os.remove(file_path)

def upload_images():
    files_selected = filedialog.askopenfilenames(
        filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    
    if len(files_selected) < 5:
        messagebox.showerror("Error", "Please select at least 5 images.")
        return
    
    username = username_entry.get().strip()
    if not username:
        messagebox.showerror("Error", "Please enter a valid username.")
        return
    
    user_folder = os.path.join('training-images', username)
    if not os.path.exists(user_folder):
        os.makedirs(user_folder)

    for i, file in enumerate(files_selected):
        file_extension = os.path.splitext(file)[1]
        dest_file = os.path.join(user_folder, f"{username}_{i}{file_extension}")
        shutil.copy(file, dest_file)
    
    # Delete files encoded-images-data.csv.bak and classifier.pkl.bak
        delete_backup_files()

    progress_label.config(text="Encoding images...")
    progress_bar.start()
    root.update()
    
    subprocess.run(['python', 'create_encodings.py'])
    
    progress_label.config(text="Training model...")
    root.update()
    
    subprocess.run(['python', 'train.py'])
    
    progress_bar.stop()
    messagebox.showinfo("Success", "Member added and model trained successfully!")
    add_member_frame.pack_forget()
    main_frame.pack()

# Setup main window
def maincall():
    global root, main_frame, add_member_frame, username_entry, progress_label, progress_bar
    root = tk.Tk()
    root.title("Face Recognition System")

    main_frame = tk.Frame(root)
    main_frame.pack()

    tk.Label(main_frame, text="Face Recognition System").pack(pady=20)

    tk.Button(main_frame, text="Add New Member", command=add_new_member).pack(pady=10)
    tk.Button(main_frame, text="Continue", command=continue_recognition).pack(pady=10)

    # Frame for adding new member
    add_member_frame = tk.Frame(root)

    tk.Label(add_member_frame, text="Add New Member").pack(pady=20)
    tk.Label(add_member_frame, text="Enter Username:").pack(pady=5)
    username_entry = tk.Entry(add_member_frame)
    username_entry.pack(pady=5)

    tk.Button(add_member_frame, text="Upload Images", command=upload_images).pack(pady=10)

    progress_label = tk.Label(add_member_frame, text="")
    progress_label.pack(pady=10)
    progress_bar = Progressbar(add_member_frame, orient=tk.HORIZONTAL, length=200, mode='indeterminate')
    progress_bar.pack(pady=10)

    root.mainloop()
