import os
import random

# Path to the folder where files will be deleted
folder_path = "./CAT_Infrasound_Data/scraped_data"  # Replace with your folder path

# Number of files to delete
number_of_files_to_delete = 30000

# List all files in the directory
files = [file for file in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, file))]

# Randomly select files to delete
files_to_delete = random.sample(files, min(number_of_files_to_delete, len(files)))

# Delete the selected files
for file in files_to_delete:
    os.remove(os.path.join(folder_path, file))

print(f"Deleted {len(files_to_delete)} files.")