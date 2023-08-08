import os
import pandas as pd

#Delete scraped raypath files that are too small 
for filename in os.listdir("./scraped_raypaths"):
    df = pd.read_csv(os.path.join("./scraped_raypaths", filename))
    if len(df) < 10: #change at discretion
        os.remove(os.path.join(os.path.join("./scraped_raypaths", filename)))
