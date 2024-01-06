import os
import pandas as pd
import numpy as np
import re
import glob
import json

dataset = []
labelset = []

startPath = "./CAT_Infrasound_Data/scraped_data"

input_path = "./CAT_Infrasound_Data/model_dataset1/input.json"
labels_path = "./CAT_Infrasound_Data/model_dataset1/labels.json"

for subdir in os.listdir(startPath):

    print(subdir)

    full_subdir_path = os.path.join(startPath, subdir)

    #Get altitude and distance (from microphone) of infrasound source
    micAlt = re.search(r'MicAlt_(\d+\.\d+)_', subdir)
    alt = micAlt.group(1)
    
    micDist = re.search(r'MicDistance_(\d+\.\d+)', subdir)
    dist = micDist.group(1)

    labelset.append([alt, dist])

    #Get the atmostats and fft files, convert their content to np arrays
    atmoFile = glob.glob(os.path.join(full_subdir_path, "AtmoStats*"))[0]
    dfAtmo = np.array(pd.read_csv(atmoFile))

    fftFile = glob.glob(os.path.join(full_subdir_path, "fft*"))[0]
    dfFFT = np.array(pd.read_csv(fftFile))

    dataset.append([dfAtmo, dfFFT])

#Save labelset and dataset as json files
with open(input_path, 'w') as f:
    json.dump(dataset, f)

with open(labels_path, 'w') as f:
    json.dump(labelset, f)