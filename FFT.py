#fft of pressure data

import os
import glob
import numpy as np
from scipy.interpolate import interp1d
import pandas as pd

startPath = "./CAT_Infrasound_Data/scraped_data"
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
   
#Interpolate, zero-pad, FFT
for subdir in os.listdir(startPath):
    
    if subdir == ".DS_Store":
        continue

    print(subdir)
    full_subdir_path = os.path.join(startPath, subdir)

    #Find the file containing in-range sound pressure data
    file_path = glob.glob(os.path.join(full_subdir_path, "ScrapedRaypath*"))[0] 

    #Read in said file in csv format
    df = pd.read_csv(file_path)
    df = df.sort_values(by=df.columns[0])  #sort by time order
    
    #Linearly interpolate and perform zero-padding to get maximum length for consistency
    time = np.array(df.iloc[:, 0])
    pressure = np.array(df.iloc[:, 1])
    
    numPoints = 2 ** 14 #Must be power of 2 (pref even)
    
    f = interp1d(time, pressure, kind='linear', bounds_error=False, fill_value=(pressure[0], 0)) #Zero pads after the last entry
    time_uniform = np.linspace(0, maxTime, num=numPoints)
    pressure_uniform = f(time_uniform)

    #Get FFT and then calculate its magnitude
    fft_result = np.abs(np.fft.fft(pressure_uniform))

    fft_df = pd.DataFrame({'Magnitude': fft_result})

    filename = f"fft_{subdir}"

    fft_df.to_csv(os.path.join(full_subdir_path, filename), index=False)