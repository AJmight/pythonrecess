# automate backup script locally within 3mins of modification
import os
import shutil
import datetime

# Set the source and destination directories
source_dir = r'Documents'
destination_dir = r'Documents\Backup'
# Create the destination directory if it doesn't exist
if not os.path.exists(destination_dir):
    os.makedirs(destination_dir)

# Get the current date and time
now = datetime.datetime.now()

# Create a timestamped backup directory
backup_dir = os.path.join(destination_dir, now.strftime('%Y-%m-%d_%H-%M-%S'))
os.makedirs(backup_dir)

# Copy the files from the source directory to the backup directory
for filename in os.listdir(source_dir):
    source_file = os.path.join(source_dir, filename)
    if os.path.isfile(source_file):
        shutil.copy2(source_file, backup_dir)
        print(f'Copied {filename} to {backup_dir}')

print('Backup completed successfully.')