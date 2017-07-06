import utilities as utl
from scipy.io import wavfile
import numpy as np

# Read the files as numpy array
rate1, data1 = wavfile.read("sourceX.wav")
rate2, data2 = wavfile.read("sourceY.wav")

# Using the mixSounds helper function from utilities.py
mixedX = utl.mixSounds([data1, data2], [0.3, 0.7]).astype(np.int16)
mixedY = utl.mixSounds([data1, data2], [0.6, 0.4]).astype(np.int16)

# Plot the mixed sound sources
utl.plotSounds([mixedX, mixedY], ["mixedX","mixedY"], rate1, "../plots/sounds/Ring_StarWars_mixed", False)

# Save the mixed sources as wav files
wavfile.write("mixedX.wav", rate1, mixedX)
wavfile.write("mixedY.wav", rate1, mixedY)