import pandas as pd
import numpy as np
import os

path = "./CAT_Infrasound_Data/raw_raypaths_SPL"
for file_name in os.listdir(path):
    df = pd.read_csv(os.path.join(path, file_name), delimiter='\s+', header=None, names=['r [km]', 'z [km]', 'trans. coeff. [dB]', 'absorption [dB]', 'time [s]', 'SPL [dB]'])
    # Save the updated DataFrame back to the .dat file
    df.to_csv(os.path.join(path, file_name), sep='\t', index=False) 