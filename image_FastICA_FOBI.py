import utilities as utl
from FastICA import FastICA
from FOBI import FOBI
import numpy as np
np.random.seed(7)

eps = 0.00000001

# Read the images from ./images/mixed
names = ["unos", "dos", "tres"]
images = utl.listImages(names, "mixed")

# The images are mean centered
centImages = []
for image in images:
	rescaleImage = image
	centImage = rescaleImage - np.mean(rescaleImage)
	centImages.append(centImage)

# The images are whitened, the helper function is in utilities.py
whiteImages = utl.whitenMatrix(utl.list2matrix(centImages))

# Uncomment the lines below to plot the images after whitening
# utl.plotImages(utl.matrix2list(whiteImages), names, "../white_tranform", True, False)

# The images are now converted into time series data
# X is a 3*image_size matrix, with each row representing a image
X = whiteImages

# Find the individual components one by one
vectors = []
for i in range(0, len(images)):
	vector = FastICA(X, vectors, eps)
	# print vector
	vectors.append(vector)

# Stack the vectors to form the unmixing matrix
W = np.vstack(vectors)

# Get the original matrix
S = np.dot(W, whiteImages)

# Get the unmixed images
uimages = utl.matrix2list(S)

# Unmixing matrix through FOBI
fobiW = FOBI(X)

# Get the original matrix using fobiW
fobiS = np.dot(fobiW.T, whiteImages)

# Get the unmixed images through FOBI
fobi_uimages = utl.matrix2list(fobiS)

# Plot the unmixed images for FastICA and save them as well
utl.plotImages(uimages, names, "ica_g3", True, True)
utl.saveImages(uimages, names, "after/fastica")

# Plot the unmixed images for FOBI and save them as well
utl.plotImages(fobi_uimages, names, "fobi", True, True)
utl.saveImages(fobi_uimages, names, "after/fobi")
