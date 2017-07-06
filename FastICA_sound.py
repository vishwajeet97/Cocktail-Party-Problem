from scipy.io import wavfile
from FastICA_image import FastICA
import utilities as utl
import numpy as np

# Specify the name
name = ["X", "Y"]

# Read the mixed signals
rate1, data1 = wavfile.read('./sounds/mixed' + name[0] + '.wav')
rate2, data2 = wavfile.read('./sounds/mixed' + name[1] + '.wav')

# Centering the mixed signals and scaling the values as well
data1 = data1 - np.mean(data1)
data1 = data1/32768
data2 = data2 - np.mean(data2)
data2 = data2/32768

# Creating a matrix out of the signals
signals = [data1, data2]
matrix = np.vstack(signals)

# Whitening the matrix as a pre-processing step
whiteMatrix = utl.whitenMatrix(matrix)

X = whiteMatrix

# Find the individual components one by one
vectors = []
for i in range(0, X.shape[0]):
	# The FastICA function is used as is from FastICA_image.py, and the it works out of the box
	vector = FastICA(X, vectors)
	vectors.append(vector)

# Stack the vectors to form the unmixing matrix
W = np.vstack(vectors)

# Get the original matrix
S = np.dot(W, whiteMatrix)

# Plot the separated sound signals
utl.plotSounds([S[0], S[1]], ["1", "2"], rate1, "Ring_StarWars_separated")

# Write the separated sound signals, 5000 is multiplied so that signal is audible
wavfile.write("./sounds/separate" + name[0] + ".wav", rate1, 5000*S[0].astype(np.int16))
wavfile.write("./sounds/separate" + name[1] + ".wav", rate1, 5000*S[1].astype(np.int16))