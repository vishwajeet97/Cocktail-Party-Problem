import utilities as utl
import numpy as np
np.random.seed(7)

eps = 0.00000001

def g1(u):
	return np.tanh(u)

def g1_dash(u):
	d = g1(u)
	return 1 - d*d

def g2(u):
	return u*np.exp(-(u*u)/2)

def g2_dash(u):
	return (1 - u*u)*np.exp(-(u*u)/2)

def g3(u):
	return 1/(1 + np.exp(-u))

def g3_dash(u):
	d = g3(u)
	return d*(1 - d)

def g4(u):
	return u*u*u

def g4_dash(u):
	return 3*u*u

def FastICA(X, vectors):
	# The size of w1 is determined by the number of images
	size = X.shape[0]
	n = X.shape[1]
	# Initial weight vector
	w1 = np.random.rand(size)
	w2 = np.random.rand(size)
	# Making the vector of unit norm
	w1 = w1/np.linalg.norm(w1)
	w2 = w2/np.linalg.norm(w2)

	while( np.abs(np.dot(w1.T,w2)) < (1 - eps)):
		w1 = w2
		first = np.dot(X, g4(np.dot(w2.T, X)))/n
		second = np.mean(g4_dash(np.dot(w2.T, X)))*w2
		w2 = first - second
		w3 = w2
		# Decorelate the vectors using Gram-Schmidt deflation with already computed components
		for vector in vectors:
			w3 = w3 - np.dot(w2.T, vector)*vector
		w2 = w3
		w2 = w2/np.linalg.norm(w2)

	return w1

# Read the images from ./images/mixed
names = ["unos", "dos", "tres"]
images = utl.listImages(names, "mixed")

# The images are 8 bit gray scaled images i.e. their value lie between 0 and 255
# The values of pixel are rescaled to [0, 1]
# The images are also mean centered
centImages = []
for image in images:
	rescaleImage = image
	centImage = rescaleImage - np.mean(rescaleImage)
	centImages.append(centImage)

# for row in centImages[0]:
# 	print row

# The images are whitened, the helper function is in utilities.py
whiteImages = utl.whitenImages(centImages)
# utl.plotImages(whiteImages, names, "../white_tranform", True, False)
# utl.showHistogram(whiteImages, names, "../white_transform_histogram", False)

# The images are now converted into time series data
# X is a 3*image_size matrix, with each row representing a image
X = utl.list2matrix(whiteImages)

# Find the individual components one by one
vectors = []
for i in range(0, len(images)):
	vector = FastICA(X, vectors)
	# print vector
	vectors.append(vector)

# Stack the vectors to form the unmixing matrix
W = np.vstack(vectors)

# Get the original matrix
S = np.dot(W, utl.list2matrix(whiteImages))

# Get the unmixed images
uimages = utl.matrix2list(S)

# Plot the unmixed images
utl.plotImages(uimages, names, "../ica_g4", True, False)

# Plot the histogram of unmixed images
utl.showHistogram(uimages, names, "../ica_histogram_g4", False)