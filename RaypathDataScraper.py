import os
import re
import numpy as np
import pandas as pd

startPath = "./CAT_Infrasound_Data/raw_raypaths_SPL"
atmoPath = "./CAT_Infrasound_Data/atmo_files"
endPath = "./CAT_Infrasound_Data/scraped_data"

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
        if (microphone_r - float(df['# r [km]'][i]))**2 + (microphone_alt - float(df['z [km]'][i]))**2 > 2.5**2:  #microphone with capture radius of 2.5 km
            drop_row_list.append(i) # data is out of range of microphone discard it
    df = df.drop(labels = drop_row_list, axis = 0) #discard said rows
    if len(df) == 0:
        continue
    #the times are set relative to when the microphone registers, not how long it takes after emitted from source
    df['time [s]'] = df['time [s]'] - min(df['time [s]'])
    #drop irrelevant columns
    df = df.drop(columns=['# r [km]', 'z [km]', 'trans. coeff. [dB]', 'absorption [dB]'])
        
    #new file name for raypathData
    newfileRaypath = f"{filename}_MicAlt_{microphone_alt}_MicDistance_{microphone_r}"

    #get the corresponding atmospheric file number
    atmo = re.search(r'Atmo(\d{1,2})_', filename)
    atmoNumber = atmo.group(1)
    print(atmoNumber)

    #read the atmospheric file
    dfAtmo = pd.read_table(os.path.join(atmoPath, "example" + atmoNumber + ".met"), sep='\s+', comment='#', header = None)
    dfAtmo = dfAtmo.astype(float)
    print(dfAtmo[0][0])

    #parse for the atmospheric measurements that are within range of microphone
    atmo_drop_row_list = []
    for i in range(0, len(dfAtmo)):
        if (abs(microphone_alt - dfAtmo[0][i]) > 2.5):
            atmo_drop_row_list.append(i)
    dfAtmo = dfAtmo.drop(labels = atmo_drop_row_list, axis = 0)
    dfAtmo.drop(dfAtmo.columns[0], axis=1, inplace=True)
    if len(dfAtmo) == 0:
        continue

    #new file name for scraped atmo data
    newfileAtmo = f"Atmo_{atmoNumber}_MicAlt_{microphone_alt}_MicDistance_{microphone_r}"

    #get the source altitude (raw dataset)
    match = re.search(r'Alt(\d+\.\d+)', filename)
    altitude = match.group(1)

    #create subdirectory for these two files
    directoryName = f"Atmo_{atmoNumber}_SrcAlt_{altitude}_MicAlt_{microphone_alt}_MicDistance_{microphone_r}"
    os.makedirs(directoryName)

    df.to_csv(os.path.join(directoryName, newfileRaypath), index=False)
    dfAtmo.to_csv(os.path.join(directoryName, newfileAtmo), index=False)

    break




    