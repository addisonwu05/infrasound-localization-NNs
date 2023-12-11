import os
import pandas as pd

#Delete scraped raypath files that are too small 
path = "./CAT_Infrasound_Data/scraped_raypaths"
for filename in os.listdir(path):
    df = pd.read_csv(os.path.join(path, filename))
    if len(df) < 10: #change at discretion
        os.remove(os.path.join(os.path.join(path, filename)))
        print("deleted")
