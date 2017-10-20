import skimage
import numpy as np
from skimage import io
from skimage.transform import resize
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def listImages(name_list, path, as_grey=True):
	"""Gives a list of 200*200 Gray-Scale images whose names are specified by name_list"""
	image_list = []

	for name in name_list:
		image = io.imread("./images/" + path + "/" + name + ".jpg", as_grey=as_grey)
		if as_grey is True:
			image = resize(image, (200, 200))
		image_list.append(image)

	return image_list

def saveImages(image_list, name_list, path):
	"""Saves the list of images in the folder specified by path"""
	i = 0
	for image in image_list:
		name = name_list[i]
		io.imsave("./images/" + path + "/" + name + ".jpg", image)
		i += 1 

def list2matrix(image_list):
	"""Converts the image into a vector and 
	stacks the vectors to form a matirx of size (no of images)*(width*height)"""
	flatten_list = []
	for image in image_list:
		flatten_list.append(image.ravel())

	matrix = np.vstack(flatten_list)

	return matrix

def matrix2list(matrix):
	"""Converts the matrix into a list of images.
	Considering each row of the matrix to be a image"""
	image_list = []
	for row in matrix:
		image = np.reshape(row, (200, 200))
		image_list.append(image)

	return image_list

def whitenMatrix(matrix):
	"""Whitening tranformation is applied to the images given as a matrix"""
	"""The transformation for the matrix X is given by E*D^(-1/2)*transpose(E)*X"""
	"""Where D is a diagonal matrix containing eigen values of covariance matrix of X"""
	"""E is the matrix containing eigen vectors of covariance matrix of X"""
	# Covariance matrix is approximated by this
	covMatrix = np.dot(matrix, matrix.T)/matrix.shape[1]

	# Doing the eigen decomposition of cavariance matrix of X 
	eigenValue, eigenVector = np.linalg.eigh(covMatrix)
	# Making a diagonal matrix out of the array eigenValue
	diagMatrix = np.diag(eigenValue)
	# Computing D^(-1/2)
	invSqrRoot = np.sqrt(np.linalg.pinv(diagMatrix))
	# Final matrix which is used for transformation
	whitenTrans = np.dot(eigenVector,np.dot(invSqrRoot, eigenVector.T))
	# whiteMatrix is the matrix we want after all the required transformation
	# To verify, compute the covvariance matrix, it will be approximately identity
	whiteMatrix = np.dot(whitenTrans, matrix)

	# print np.dot(whiteMatrix, whiteMatrix.T)/matrix.shape[1]

	return whiteMatrix


def showHistogram(image_list, name_list, path, toSave=False, hist_range=(0.0, 1.0)):
	"""Shows the histogram of images specified by image_list 
	and sets the range of hist() using hist_range"""
	fig = plt.figure()
	fig.subplots_adjust(hspace=.5)
	image_coordinate = 321
	i = 0
	for image in image_list:
		fig.add_subplot(image_coordinate)
		plt.title(name_list[i])
		plt.set_cmap('gray')
		plt.axis('off')
		plt.imshow(image)

		image_coordinate += 1

		fig.add_subplot(image_coordinate)
		plt.title('histogram')
		plt.hist(image.ravel(), bins=256, range=hist_range)

		image_coordinate += 1	
		i += 1

	if toSave:
		plt.savefig("./plots/images/" + path + ".jpg")
	plt.show()

def plotImages(image_list, name_list, path, as_grey, toSave=False):
	"""Plots the images given in image_list side by side."""

	fig = plt.figure()
	imageCoordinate = 100 + 10*len(image_list) + 1
	i = 0

	for image in image_list:
		fig.add_subplot(imageCoordinate)
		plt.title(name_list[i])
		plt.axis('off')
		plt.imshow(image)
		if as_grey:
			plt.set_cmap('gray')

		imageCoordinate += 1
		i += 1

	if toSave:
		plt.savefig("./plots/images/" + path + ".png",bbox_inches='tight')
	plt.show()

def plotSounds(sound_list, name_list, samplerate, path, toSave=False):
	"""Plots the sounds as a time series data"""

	times = np.arange(len(sound_list[0]))/float(samplerate)

	fig = plt.figure(figsize=(15,4))
	imageCoordinate = 100 + 10*len(sound_list) + 1
	i = 0

	for sound in sound_list:
		fig.add_subplot(imageCoordinate)
		plt.fill_between(times, sound, color='k')
		plt.xlim(times[0], times[-1])
		plt.title(name_list[i])
		plt.xlabel('time (s)')
		plt.ylabel('amplitude')
		# plt.axis("off")
		plt.plot(sound)

		imageCoordinate += 1
		i += 1

	if toSave:
		plt.savefig("./plots/sounds/" + path + ".png", bbox_inches='tight')
	plt.show()