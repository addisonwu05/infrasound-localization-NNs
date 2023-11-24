#this code is intended to convert the A_Atmo (atmospheric attenuation) [dB] column to a series of relative SPL measurements wrt time
#will then hopefully be used to make a FFT vector

import os
import pandas as pd
import math

startPath = "./CAT_Infrasound_Data/raw_raypaths"
endPath = ".CAT_Infrasound_Data/raw_raypaths_SPL"

for filename in os.listdir(startPath):
    #Read datafile and ensure it is float file
    df = pd.read_table(os.path.join(startPath, filename), dtype=float)
    df = df.astype(float)

    #Add appropriate columns
    newColumnName = "Sound Pressure Amplitude"
    df = df.assign(newColumnName = 0)
    
    #Use formula 2 in ISO-9613-1-1933 to convert to sound pressure values
    for line in df.iterrows():
        initialSPA = 1
        df['Sound Pressure Amplitude (Pa)'][line] = initialSPA/(10**(math.abs(df['absorption [dB]'][line])/20))
    output_file_path = os.path.join(endPath, filename)
    df.to_csv(output_file_path, sep='\t', index=False, header=False)