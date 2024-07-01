# infrasound-localization-NNs
Infrasound propagation simulation data and machine learning code used for infrasonic source localization in refractive settings

infraGA raytracing tool: https://github.com/LANL-Seismoacoustics/infraGA

Run the files in the following order (make sure to change directories as appropriate):

1. RaypathDataGenerator.py
2. AttenutationtoRelativeAmplitude.py
3. RaypathDataScraper.py
4. AtmoStats.py or FFT.py (one after the other)
5. DataOrganize.py

in which afterwards, you can feed the data into the model of whose weights will be released soon (or in the meantime, train it in models.ipynb as attached)
