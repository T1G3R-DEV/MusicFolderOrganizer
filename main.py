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

def run_process():
    input_path = input_folder_entry.get()
    output_path = output_folder_entry.get()
    # Füge hier den Code hinzu, um die gewünschte Aktion mit den ausgewählten Pfaden auszuführen
    print(f"Aktion wird mit Eingabepfad '{input_path}' und Ausgabepfad '{output_path}' ausgeführt")

# GUI erstellen
root = tk.Tk()
root.title("Music Folder Orgernizer v0.0.1")

# Eingabeordner
input_folder_label = tk.Label(root, text="Eingabeordner:")
input_folder_label.pack()

input_folder_entry = tk.Entry(root, width=50)
input_folder_entry.pack()

input_folder_button = tk.Button(root, text="Ordner wählen", command=select_input_folder)
input_folder_button.pack()

# Ausgabeordner
output_folder_label = tk.Label(root, text="Ausgabeordner:")
output_folder_label.pack()

output_folder_entry = tk.Entry(root, width=50)
output_folder_entry.pack()

output_folder_button = tk.Button(root, text="Ordner wählen", command=select_output_folder)
output_folder_button.pack()

# Run Button
run_button = tk.Button(root, text="Run", command=run_process)
run_button.pack()

root.mainloop()
