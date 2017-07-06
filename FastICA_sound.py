from scipy.io import wavfile
import matplotlib.pyplot as plt
from FastICA_image import FastICA
import utilities as utl
import numpy as np

# Read the mixed signals
rate1, data1 = wavfile.read('./sounds/mixedX.wav')
rate2, data2 = wavfile.read('./sounds/mixedY.wav')

# Centering the mixed signals
data1 = data1 - np.mean(data1)
data2 = data2 - np.mean(data2)

signals = [data1, data2]
matrix = np.vstack(signals)

whiteMatrix = utl.whitenMatrix(matrix)

X = whiteMatrix

# Find the individual components one by one
vectors = []
for i in range(0, X.shape[0]):
	vector = FastICA(X, vectors)
	# print vector
	vectors.append(vector)

# Stack the vectors to form the unmixing matrix
W = np.vstack(vectors)

# Get the original matrix
S = np.dot(W, whiteMatrix)

# utl.plotSounds([S[0], S[1]], ["1", "2"], rate1, "aas")

wavfile.write("./sounds/separateX.wav", rate1, 1000*S[0].astype(np.int16))
wavfile.write("./sounds/separateY.wav", rate1, 1000*S[1].astype(np.int16))