"""Searches script file name, check and change permissions"""
import os
import sys
import stat

def update_file_permissions(filename):
    # Walk through the directory to find the file
    for root, dirs, files in os.walk("."): # Changed to current dir for safety
        if filename in files:
            path = os.path.join(root, filename)
            
            # Check for Write permission
            if not os.access(path, os.W_OK):
                print(f"No write permission for {path}")
                return

            # Add Execute permission for User and Group
            current_mode = os.stat(path).st_mode
            os.chmod(path, current_mode | stat.S_IXUSR | stat.S_IXGRP)
            print(f"Execute permissions restored for: {path}")
            return
    print("File not found.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        update_file_permissions(sys.argv[1])
