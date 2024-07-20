#fft of pressure data

import os
import glob
import numpy as np
from scipy.interpolate import interp1d
import pandas as pd

startPath = "./Infrasound_Data/scraped_data"
maxTime = 0

#Get longest time duration of any file
for subdir in os.listdir(startPath):

    if subdir == ".DS_Store":
        continue

    full_subdir_path = os.path.join(startPath, subdir)

    #Find the file containing in-range sound pressure data
    file_path = glob.glob(os.path.join(full_subdir_path, "ScrapedRaypath*"))[0]

    #Read in said file in csv format
    df = pd.read_csv(file_path)
    
    #Get duration of the file
    duration = df.iloc[:, 0].max()
    if duration > maxTime:
        maxTime = duration

print(maxTime)