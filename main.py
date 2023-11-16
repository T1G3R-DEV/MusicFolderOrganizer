import tkinter as tk
from tkinter import filedialog
import os
import re

import shutil
from mutagen.easyid3 import EasyID3
from mutagen.flac import FLAC
from mutagen.wavpack import WavPack

def get_music_tags(file_path):
    tags = {}
    try:
        if file_path.lower().endswith('.mp3'):
            audio = EasyID3(file_path)
            tags['artist'] = audio['artist'][0] if 'artist' in audio else 'Unknown Artist'
            tags['album'] = audio['album'][0] if 'album' in audio else 'Unknown Album'
            tags['title'] = audio['title'][0] if 'title' in audio else os.path.basename(file_path)
        elif file_path.lower().endswith('.flac'):
            audio = FLAC(file_path)
            tags['artist'] = audio['artist'][0] if 'artist' in audio else 'Unknown Artist'
            tags['album'] = audio['album'][0] if 'album' in audio else 'Unknown Album'
            tags['title'] = audio['title'][0] if 'title' in audio else os.path.basename(file_path)
        elif file_path.lower().endswith('.wav'):
            audio = WavPack(file_path)
            tags['artist'] = audio['artist'][0] if 'artist' in audio else 'Unknown Artist'
            tags['album'] = audio['album'][0] if 'album' in audio else 'Unknown Album'
            tags['title'] = audio['title'][0] if 'title' in audio else os.path.basename(file_path)
        else:
            print(f"Unsupported format for file: {file_path}")
            return None
    except Exception as e:
        print(f"Error reading tags for {file_path}: {e}")
        return None
    
    

    return tags

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
    #output_format = output_format_entry.get()

    # Strip subfolders logic here
    log_output.insert(tk.END, f"Stripping subfolders from '{input_path}' ...\n")
    # Perform the action and update the log output
    # Example:
    # log_output.insert(tk.END, "Subfolders stripped successfully.\n")
    for root, dirs, files in os.walk(input_path):
        for file in files:
            file_path = os.path.join(root, file)
            # Move files to the most outer folder
            new_path = os.path.join(input_path, file)
            # Rename .jpg files if they already exist
            count = 1
            while os.path.exists(new_path):
                file_name, file_ext = os.path.splitext(file)
                new_path = os.path.join(input_path, f"{file_name}_{count}{file_ext}")
                count += 1
            try:
                os.rename(file_path, new_path)
                #log_output.insert(tk.END,f"Moved")
            except Exception as e:
                log_output.insert(tk.END,f"Error moving {file}: {e}")
            #log_output.insert(tk.END, f"Moving File '{file_path}' to '{new_path}' ...\n")

    # Delete empty subfolders
    for root, dirs, files in os.walk(input_path, topdown=False):
        for folder in dirs:
            folder_path = os.path.join(root, folder)
            if not os.listdir(folder_path):
                try:
                    os.rmdir(folder_path)
                    #log_output.insert(tk.END, f"Deleting Folder '{folder_path}' ...\n")
                except OSError as e:
                    log_output.insert(tk.END, f"ERROR: '{e}' ...\n")
            else: 
                log_output.insert(tk.END, f"ERROR: Folder not empty, try deleting it manually ...\n")
    log_output.insert(tk.END, f"Finished Moving files ...\n")
                


def create_subfolders():
    input_path = input_folder_entry.get()
    output_format = output_format_entry.get()

    # Create subfolders logic here
    log_output.insert(tk.END, f"Creating subfolders from '{input_path}' with format '{output_format}'...\n")
    # Perform the action and update the log output
    # Example:
    for root, dirs, files in os.walk(input_path):
        for file in files:
            file_path = os.path.join(root, file)
            tags = get_music_tags(file_path)
            if tags:
                tag_title = tags['title'].replace(' ', '_')
                tag_title = re.sub(r'[^\w.-]', '-', tag_title)

                tag_album = tags['album'].replace(' ', '_')
                tag_album = re.sub(r'[^\w.-]', '-', tag_album)

                tag_artist = tags['artist'].replace(' ', '_')
                tag_artist = re.sub(r'[^\w.-]', '-', tag_artist)

                artist_folder = os.path.join(input_path, tag_artist)
                album_folder = os.path.join(artist_folder, tag_album)

                # Create folders if they don't exist
                os.makedirs(album_folder, exist_ok=True)

                # Move the file
                new_file_path = os.path.join(album_folder, f"{tag_title}{os.path.splitext(file)[1]}")
                try:
                    os.rename(file_path, new_file_path)
                    #log_output.insert(tk.END,f"Moved {file} to {album_folder}")
                except Exception as e:
                    log_output.insert(tk.END,f"Error moving {file}: {e}")
            else: 
                log_output.insert(tk.END,f"Error moving {file_path}: Tags not found")
    log_output.insert(tk.END, "\nSubfolders created successfully.\n")


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
log_output = tk.Text(root, height=20, width=100)
log_output.pack()

root.mainloop()
