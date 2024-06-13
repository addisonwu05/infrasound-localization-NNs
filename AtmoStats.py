import os
import glob
import re
import numpy as np
import pandas as pd

startPath = "./Infrasound_Data/scraped_data"

for subdir in os.listdir(startPath):

    if subdir == ".DS_Store":
        continue

    full_subdir_path = os.path.join(startPath, subdir)
    print(full_subdir_path)
    #Find the file containing in-range atmospheric data
    file_path = glob.glob(os.path.join(full_subdir_path, "ScrapedAtmo*"))[0]
    print(file_path)

    #Read in said file in csv format
    df = pd.read_csv(file_path)

    #list for stats
    atmoStats = []

    #Get stats in each column (mean, min, max, stdev)
    for i in range(0, df.shape[1]):
        
        mean = np.mean(df.iloc[:, i])
        atmoStats.append(mean)
        
        stdev = np.std(df.iloc[:, i])
        atmoStats.append(stdev)
        
        min = np.min(df.iloc[:, i])
        atmoStats.append(min) 
        
        max = np.max(df.iloc[:, i])
        atmoStats.append(max)

        y_data = df.iloc[:, i]
        x_data = np.arange(0, len(y_data) * 0.1, 0.1)  # Generate x-domain

        # Fit a polynomial of order 5
        poly_coefficients = np.polyfit(x_data, y_data, 5)
        
        atmoStats.extend(poly_coefficients)

    atmo = re.search(r'Atmo_(\d{1,2})_', file_path)
    atmoNumber = atmo.group(1)

    micAlt = re.search(r'MicAlt_(\d+\.\d+)_', file_path)
    alt = micAlt.group(1)

    atmoStats.append(alt)

    fileName = f"AtmoStats_Atmo_{atmoNumber}_MicAlt_{alt}"

    # Convert atmoStats to DataFrame
    stats_df = pd.DataFrame([atmoStats])

    # Save DataFrame as CSV in the current subdir
    save_path = os.path.join(full_subdir_path, fileName)
    stats_df.to_csv(save_path, index=False, header=False)