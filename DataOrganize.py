import os
import pandas as pd
import re
import glob
import json

dataset = []
labelset = []

startPath = "./CAT_Infrasound_Data/scraped_data"

input_path = "./CAT_Infrasound_Data/model_dataset5/input.json"
labels_path = "./CAT_Infrasound_Data/model_dataset5/labels.json"

for subdir in os.listdir(startPath):

    if subdir == ".DS_Store":
        continue

    print(subdir)

    full_subdir_path = os.path.join(startPath, subdir)

    #Get altitude and distance (from microphone) of infrasound source
    srcAlt = re.search(r'SrcAlt_(\d+\.\d+)_', subdir)
    alt = srcAlt.group(1)
    
    micDist = re.search(r'MicDistance_(\d+\.\d+)', subdir)
    dist = micDist.group(1)

    labelset.append([alt, dist])

    #Get the atmostats and fft files
    atmoFile = glob.glob(os.path.join(full_subdir_path, "AtmoStats*"))[0]
    dfAtmo = (pd.read_csv(atmoFile, header = None)).values.tolist()[0]
    
    fftFile = glob.glob(os.path.join(full_subdir_path, "fft*"))[0]
    dfFFT = (pd.read_csv(fftFile)).values.tolist()
    dfFFT = [item for sublist in dfFFT for item in sublist]

    dataset.append([dfAtmo, dfFFT])

#Save labelset and dataset as json files
with open(input_path, 'w') as f:
    json.dump(dataset, f)

with open(labels_path, 'w') as f:
    json.dump(labelset, f)