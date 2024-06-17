import os
import pandas as pd
import re
import glob
import json
import random

train_dataset = []
train_labelset = []

val_dataset = []
val_labelset = []

startPath = "./Infrasound_Data/scraped_data"

numFiles = len(os.listdir(startPath))

train_input_path = "./Infrasound_Data/model_dataset9/train_input.json"
train_labels_path = "./Infrasound_Data/model_dataset9/train_labels.json"

val_input_path = "./Infrasound_Data/model_dataset9/val_input.json"
val_labels_path = "./Infrasound_Data/model_dataset9/val_labels.json"

atmo_labels = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
random.seed(47)
random.shuffle(atmo_labels)
train_atmo_labels, val_atmo_labels = atmo_labels[:14], atmo_labels[14:]

counter = 1

for subdir in os.listdir(startPath):

    if subdir == ".DS_Store":
        continue

    print(subdir)
    print("File ", counter, " of ", numFiles )
    counter = counter + 1

    full_subdir_path = os.path.join(startPath, subdir)

    #Get altitude and distance (from microphone) of infrasound source
    srcAlt = re.search(r'SrcAlt_(\d+\.\d+)_', subdir)
    alt = srcAlt.group(1)
    
    micDist = re.search(r'MicDistance_(\d+\.\d+)', subdir)
    dist = micDist.group(1)

    #Get the atmostats and fft files
    atmoFile = glob.glob(os.path.join(full_subdir_path, "AtmoStats*"))[0]
    dfAtmo = (pd.read_csv(atmoFile, header = None)).values.tolist()[0]
    
    fftFile = glob.glob(os.path.join(full_subdir_path, "fft*"))[0]
    dfFFT = (pd.read_csv(fftFile)).values.tolist()
    dfFFT = [item for sublist in dfFFT for item in sublist]

    #Inspect atmo file label
    atmoLabel = re.search(r'Atmo_(\d+)_SrcAlt', subdir).group(1)

    if int(atmoLabel) in train_atmo_labels:
        train_labelset.append([alt, dist])
        train_dataset.append([dfAtmo, dfFFT])

    else:
        val_labelset.append([alt, dist])
        val_dataset.append([dfAtmo, dfFFT])

#Shuffle the datasets
combined_train = list(zip(train_dataset, train_labelset))
random.shuffle(combined_train)
train_dataset[:], train_labelset[:] = zip(*combined_train)

combined_val = list(zip(val_dataset, val_labelset))
random.shuffle(combined_val)
val_dataset[:], val_labelset[:] = zip(*combined_val)

#Save datasets and labelsets as json files
with open(train_input_path, 'w') as f:
    json.dump(train_dataset, f)

with open(train_labels_path, 'w') as f:
    json.dump(train_labelset, f)

with open(val_input_path, 'w') as f:
    json.dump(val_dataset, f)

with open(val_labels_path, 'w') as f:
    json.dump(val_labelset, f)
