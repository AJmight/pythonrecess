import os
import shutil
import time
from datetime import datetime, timedelta

# Configuration
source_dir = r'Documents'
destination_dir = r'Documents\Backup'
sync_interval_minutes = 3  # Check for changes every 3 minutes

def sync_recent_changes():
    # Create backup directory if needed
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
    
    # Calculate cutoff time (files modified in last 3 minutes)
    cutoff_time = datetime.now() - timedelta(minutes=sync_interval_minutes)
    
    # Track if we made any changes
    changes_made = False
    
    # Walk through all files in source directory
    for root, _, files in os.walk(source_dir):
        for file in files:
            source_path = os.path.join(root, file)
            
            # Get file modification time
            mod_time = datetime.fromtimestamp(os.path.getmtime(source_path))
            
            # If file was modified recently
            if mod_time > cutoff_time:
                # Create relative path for destination
                rel_path = os.path.relpath(source_path, source_dir)
                dest_path = os.path.join(destination_dir, rel_path)
                
                # Create subdirectories if needed
                os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                
                # Copy file (overwrites if exists)
                shutil.copy2(source_path, dest_path)
                print(f"Synced: {rel_path}")
                changes_made = True
    
    return changes_made

# Main loop
print(f"Starting backup monitor. Syncing changes every {sync_interval_minutes} minutes...")
while True:
    if sync_recent_changes():
        print(f"Sync completed at {datetime.now()}")
    else:
        print(f"No changes detected at {datetime.now()}")
    
    # Wait before checking again
    time.sleep(sync_interval_minutes * 60)