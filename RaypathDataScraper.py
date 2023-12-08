import os
import re
import numpy as np
import pandas as pd

startPath = "./CAT_Infrasound_Data/raw_raypaths_SPL"
endPath = "./CAT_Infrasound_Data/scraped_raypaths"

for filename in os.listdir(startPath):
    #Set the altitude of the microphone
    microphone_alt = np.around(np.random.uniform(3, 20), decimals=2)
    microphone_r = np.around(np.random.uniform(10, 900), decimals=2)

    #Read datafile and ensure it is float file
    df = pd.read_table(os.path.join(startPath, filename), dtype=float)
    df = df.astype(float)

    #parse for relevant data, r and z must be within the microphone's pickup range
    #Spherical distribution? Pythagorean inequality
    drop_row_list = []
    for i in range(0, len(df)):
        if (microphone_r - float(df["# r [km]"][i]))**2 + (microphone_alt - float(df["z [km]"][i]))**2 > 2.5**2:  #microphone with capture radius of 2.5 km
            drop_row_list.append(i) # data is out of range of microphone discard it
    df = df.drop(labels = drop_row_list, axis = 0) #discard said rows

    #the times are set relative to when the microphone registers, not how long it takes after emitted from source
    df["time [s]"] = df["time [s]"] - min(df["time [s]"])
    #drop irrelevant columns
    df = df.drop(columns=["# r [km]", "z [km]", "trans. coeff. [dB]"])

    #get the source altitude (raw dataset)
    match = re.search(r'Alt(\d+\.\d+)', filename)
    altitude = match.group(1)
        
    #new file name
    newfile = f"MicAlt_{microphone_alt}_MicDistance_{microphone_r}_SrcAlt_{altitude}_{filename}"

    #save to the scraped folder as a TSV (tab CSV)
    output_file_path = os.path.join(endPath, newfile)
    df.to_csv(output_file_path, sep='\t', index=False, header=False)
    break
