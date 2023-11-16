import tkinter as tk
from tkinter import filedialog

def select_input_folder():
    input_folder_path = filedialog.askdirectory()
    input_folder_entry.delete(0, tk.END)
    input_folder_entry.insert(0, input_folder_path)

def select_output_folder():
    output_folder_path = filedialog.askdirectory()
    output_folder_entry.delete(0, tk.END)
    output_folder_entry.insert(0, output_folder_path)

def strip_subfolders():
    input_path = input_folder_entry.get()
    output_format = output_format_entry.get()

    # Strip subfolders logic here
    log_output.insert(tk.END, f"Stripping subfolders from '{input_path}' to '{output_path}' ...\n")
    # Perform the action and update the log output
    # Example:
    # log_output.insert(tk.END, "Subfolders stripped successfully.\n")

def create_subfolders():
    input_path = input_folder_entry.get()
    output_format = output_format_entry.get()

    # Create subfolders logic here
    log_output.insert(tk.END, f"Creating subfolders from '{input_path}' to '{output_path}' with format '{output_format}'...\n")
    # Perform the action and update the log output
    # Example:
    # log_output.insert(tk.END, "Subfolders created successfully.\n")

# GUI creation
root = tk.Tk()
root.title("Folder Actions")

# Input folder
input_folder_label = tk.Label(root, text="Selected Folder:")
input_folder_label.pack()

input_folder_entry = tk.Entry(root, width=50)
input_folder_entry.pack()

input_folder_button = tk.Button(root, text="Select Folder", command=select_input_folder)
input_folder_button.pack()

# Output format
output_format_label = tk.Label(root, text="Output Format:")
output_format_label.pack()

output_format_entry = tk.Entry(root, width=50)
output_format_entry.insert(0, "./$artist$/$album$/$song$")
output_format_entry.pack()

# Strip Subfolders button
strip_subfolders_button = tk.Button(root, text="Strip Subfolders", command=strip_subfolders)
strip_subfolders_button.pack()

# Create Subfolders button
create_subfolders_button = tk.Button(root, text="Create Subfolders", command=create_subfolders)
create_subfolders_button.pack()

# Log output
log_output = tk.Text(root, height=10, width=70)
log_output.pack()

root.mainloop()
