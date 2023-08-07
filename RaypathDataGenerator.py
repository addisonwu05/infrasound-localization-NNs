import pyautogui
import time
import numpy as np

#Get the cursor at the right place
time.sleep(10)
print(pyautogui.position())

#First, select the atmospheric profile
for i in range(0, 17):
    atmo = "example" + str(i) + ".met"
    #Then, set an initial source altitude
    for j in np.arange(0, 20, 0.05):
        #ROUND J TO 2 DECIMAL PLACES SO I DON'T GET BAD LONG FLOATING POINT ARITHMETIC
        j = np.round(j, decimals=2)
        #Then, run the command
        pyautogui.typewrite("./infraGA/bin/infraga-2d -prop ./infraGA/training_data/profs/" + atmo + " src_alt=" + str(j) + "incl_min=-89" + " incl_max=89")
        pyautogui.press("enter")
        #Rename and move the file
        newFileName = "Atmo" + str(i) + "_Alt" + str(j) + ".raypaths.dat"
        pyautogui.typewrite("mv ./infraGA/training_data/profs/example" + str(i) + ".raypaths.dat" + " ./raw_raypaths/" + newFileName)
        pyautogui.press("enter")