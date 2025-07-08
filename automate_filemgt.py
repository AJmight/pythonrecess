# This script automates the organization of files in the Downloads folder
# It sorts files into folders based on their extensions
# Import necessary libraries


import os
import shutil

# Get the current working directory
download_dir = r'C:\Users\user\OneDrive\Desktop\Bunjako beach final'
# Define the destination directory
destination_dir = r'C:\Users\user\OneDrive\Desktop\Bunjako beach final\organized_files'
# Create the destination directory if it doesn't exist
if not os.path.exists(destination_dir):
    os.makedirs(destination_dir)
# List all folders in the download directory
folders={
    'music': ['.mp3', '.wav', '.flac'],
    'web': ['.html', '.css', '.js'],
    'images': ['.jpg', '.jpeg', '.png', '.gif'],
    'videos': ['.mp4', '.avi', '.mov', '.mkv'],
    'documents': ['.pdf', '.docx', '.txt', '.xlsx'],
    'audio': ['.mp3', '.wav', '.flac'],
}
# create target folders if dont exist
for folder in folders:
    folder_path = os.path.join(destination_dir, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        
# loop through all files in the download directory
for filename in os.listdir(download_dir):
    file_path = os.path.join(download_dir, filename)
    # Check if it is a directory
    if os.path.isdir(file_path): 
        continue
    # Check the file extension and move it to the corresponding folder
    for folder, extensions in folders.items():
        if any(filename.lower().endswith(ext) for ext in extensions):
            target_folder = os.path.join(destination_dir, folder)
            shutil.move(file_path, target_folder)
            print(f'Moved {filename} to {target_folder}')
            break