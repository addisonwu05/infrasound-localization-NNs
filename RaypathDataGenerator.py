import os
import numpy as np

#First, select the atmospheric profile
for i in range(0, 17):
    atmo = "example" + str(i) + ".met"
    #Then, set an initial source altitude
    for j in np.arange(2, 20, 0.05):
        #Round to 2 decimal places, avoid floating point arithmetic chaos
        j = np.round(j, decimals=2)
        #Then, run the command
        os.system("./infraGA/bin/infraga-2d -prop ./infraGA/examples/profs/" + atmo + " src_alt=" + str(j) + " incl_min=-89 " + " incl_max=89")
        #Rename and move the file
        newFileName = "Atmo" + str(i) + "_Alt" + str(j) + ".raypaths.dat"
        os.system("mv ./infraGA/examples/profs/example" + str(i) + ".raypaths.dat" + " ./raw_raypaths/" + newFileName)
