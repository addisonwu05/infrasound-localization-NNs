# For each scraped raypath datafile, obtain the corresponding atmospheric readings (in-range)

import os
import re
import numpy as np
import pandas as pd

startPath = "./CAT_Infrasound_Data/scraped_raypaths"
middlePath = "./CAT_Infrasound_Data/atmo_files"
endPath = "./CAT_Infrasound_Data/scraped_atmo_files"

for filename in sorted(os.listdir(startPath), key=numericalSort):
    print(filename)

    