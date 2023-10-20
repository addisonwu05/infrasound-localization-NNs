#this code is intended to convert the A_Atmo (atmospheric attenuation) [dB] column to a series of relative SPL measurements wrt time
#will then hopefully be used to make a FFT vector

import os
import numpy as np
import pandas as pd
import math

startPath = "./CAT_Infrasound_Data/raw_raypaths"
endPath = ".CAT_Infrasound_Data/raw_raypaths_SPL"

for filename in os.listdir(startPath):
    #Read datafile and ensure it is float file
    df = pd.read_table(os.path.join(startPath, filename), dtype=float, skip_blank_lines=False)
    df = df.astype(float)
    df['Propagation Distance (km)'] = df.Series([], dtype='float')
    
    #Add measurements for cumulative propgation distance for each ray
    #see "s" in ISO document 1993-1
    cumulativePropagationDistance = 0
    for line in df.iterrows():
        if line == 0:
            df.loc[line, 'Propgation Distance (km)'] = 0    
        if df.isnull().loc[line]:
            cumulativePropagationDistance = 0
            continue
        if df.isnull().loc[line - 1]:
            df.loc[line, 'Propgation Distance (km)'] = cumulativePropagationDistance
            continue
        else:
            cumulativePropagationDistance =+ math.sqrt((df['# r [km]'][line] - df['# r [km]'][line-1])**2
                                                       + (df['z [km]'][line] - df['z [km]'][line-1])**2)
        df.loc[line, 'Propgation Distance (km)'] = cumulativePropagationDistance
        break #remove when sure code works

    #Now deal with converting attenuation to SPL using formula in ISO 1993-1

    