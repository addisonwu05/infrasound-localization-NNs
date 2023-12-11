import os
import pandas as pd

#Delete scraped raypath files that are too small 
path = "./CAT_Infrasound_Data/scraped_raypaths"
count = 0
for filename in os.listdir(path):
    count = count + 1
    df = pd.read_csv(os.path.join(path, filename))
    print(len(df))
    if len(df) < 10: #change at discretion
        os.remove(os.path.join(os.path.join(path, filename)))
        print("deleted")
print(count)