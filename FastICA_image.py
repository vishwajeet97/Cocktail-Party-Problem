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
	"""The following algorithm is used to compute the independent componenets
	1. Initialize a random vector
	2. Make it of unit norm
	3. Repeat until convergence
	   W = E{xg(W.T*x)} - E{g_dash(W.T*x)}*W 
	   W = W/norm(W)
	"""
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
		# first is E{xg(W.T*x)} term
		first = np.dot(X, g3(np.dot(w2.T, X)))/n
		# second is E{g_dash(W.T*x)}*W term
		second = np.mean(g3_dash(np.dot(w2.T, X)))*w2
		# Update step
		w2 = first - second
		# Using Gram-Schmidt deflation to decorelate the vectors
		w3 = w2
		for vector in vectors:
			w3 = w3 - np.dot(w2.T, vector)*vector
		w2 = w3
		w2 = w2/np.linalg.norm(w2)

	return w1

if __name__ == "__main__":
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
	# utl.showHistogram(utl.matrix2list(whiteImages), names, "../white_transform_histogram", False)

	# The images are now converted into time series data
	# X is a 3*image_size matrix, with each row representing a image
	X = whiteImages

	# Find the individual components one by one
	vectors = []
	for i in range(0, len(images)):
		vector = FastICA(X, vectors)
		# print vector
		vectors.append(vector)

	# Stack the vectors to form the unmixing matrix
	W = np.vstack(vectors)

	# Get the original matrix
	S = np.dot(W, whiteImages)

	# Get the unmixed images
	uimages = utl.matrix2list(S)

	# Plot the unmixed images
	utl.plotImages(uimages, names, "../ica_g4", True, False)

	# Plot the histogram of unmixed images
	utl.showHistogram(uimages, names, "../ica_histogram_g4", False)