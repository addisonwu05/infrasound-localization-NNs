import os
import numpy as np

#First, select the atmospheric profile
for i in range(6, 11):
    atmo = "example" + str(i) + ".met"
    #Then, set an initial source altitude
    for j in np.arange(2, 20, 0.05):
        #ROUND J TO 2 DECIMAL PLACES SO I DON'T GET BAD LONG FLOATING POINT ARITHMETIC
        j = np.round(j, decimals=2)
        #Then, run the command
        os.system("./infraGA/bin/infraga-2d -prop ./infraGA/examples/profs/" + atmo + " src_alt=" + str(j) + " incl_min=-89 " + " incl_max=89")
        #Rename and move the file
        newFileName = "Atmo" + str(i) + "_Alt" + str(j) + ".raypaths.dat"
        os.system("mv ./infraGA/examples/profs/example" + str(i) + ".raypaths.dat" + " ./raw_raypaths/" + newFileName)