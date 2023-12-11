import os
import pandas as pd

#Delete scraped raypath files that are too small 
path = "./CAT_Infrasound_Data/scraped_raypaths"
minLength = 10
for filename in os.listdir(path):
    df = pd.read_csv(os.path.join(path, filename))
    print(len(df))
    if len(df) < minLength: #change at discretion
        os.remove(os.path.join(os.path.join(path, filename)))
        print("deleted")