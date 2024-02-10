import os
import shutil
import mimetypes
import tkinter as tk
from tkinter import filedialog

def organize_files(source_dir):
    try:
        for filename in os.listdir(source_dir):
            file_path = os.path.join(source_dir, filename)

            if os.path.isfile(file_path):
                file_type = get_file_type(file_path)
                dest_folder = os.path.join(source_dir, file_type)

                if not os.path.exists(dest_folder):
                    os.makedirs(dest_folder)

                shutil.move(file_path, os.path.join(dest_folder, filename))

        log_text.set("Files organized successfully.")
    except Exception as e:
        log_text.set(f"An error occurred: {str(e)}")

def get_file_type(file_path):
    mime_type, _ = mimetypes.guess_type(file_path)
    return mime_type.split('/')[0] if mime_type else "Other"

def select_directory():
    directory = filedialog.askdirectory()
    source_entry.delete(0, tk.END)
    source_entry.insert(0, directory)

# Create the main window
window = tk.Tk()
window.title("File Organizer")
window.geometry('500x400')

# Create and configure the widgets
source_label = tk.Label(window, text="Source Directory:")
source_entry = tk.Entry(window, width=40)
source_button = tk.Button(window, text="Browse", command=select_directory)
organize_button = tk.Button(window, text="Organize Files", command=lambda: organize_files(source_entry.get()))
log_label = tk.Label(window, text="Log:")
log_text = tk.StringVar()
log_entry = tk.Entry(window, textvariable=log_text, state='readonly', width=40)

# Place the widgets on the window
source_label.grid(row=0, column=0, padx=10, pady=10)
source_entry.grid(row=0, column=1, padx=10, pady=10)
source_button.grid(row=0, column=2, padx=10, pady=10)
organize_button.grid(row=1, column=0, columnspan=3, pady=10)
log_label.grid(row=2, column=0, padx=10, pady=10)
log_entry.grid(row=2, column=1, columnspan=2, padx=10, pady=10)

# Start the GUI event loop
window.mainloop()
