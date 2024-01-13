import os
import random
import shutil

# Path to the folder where subfolders will be deleted
folder_path = "./CAT_Infrasound_Data/scraped_data"  # Replace with your folder path

# Number of subfolders to delete
number_of_subfolders_to_delete = 30000

# List all subfolders in the directory
subfolders = [os.path.join(folder_path, folder) for folder in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, folder))]

# Randomly select subfolders to delete
subfolders_to_delete = random.sample(subfolders, min(number_of_subfolders_to_delete, len(subfolders)))

# Delete the selected subfolders
for subfolder in subfolders_to_delete:
    shutil.rmtree(subfolder)

print(f"Deleted {len(subfolders_to_delete)} subfolders.")