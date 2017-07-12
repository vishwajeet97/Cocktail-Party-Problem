import numpy as np

def FOBI(X):
	"""Fourth Order Blind Identification technique is used.
	The function returns the unmixing matrix.
	X is assumed to be centered and whitened.
	The paper by J. Cardaso is in itself the best resource out there for it.
	SOURCE SEPARATION USING HIGHER ORDER MOMENTS - Jean-Francois Cardoso"""	

	rows = X.shape[0]
	n = X.shape[1]
	# Initializing the weighted covariance matrix which will hold the fourth order information
	weightedCovMatrix = np.zeros([rows, rows]) 

	# Approximating the expectation by diving with the number of data points
	for signal in X.T:
		norm = np.linalg.norm(signal)
		weightedCovMatrix += norm*norm*np.outer(signal, signal)

	weightedCovMatrix /= n

	# Doing the eigen value decomposition
	eigValue, eigVector = np.linalg.eigh(weightedCovMatrix)

	# print eigVector
	return eigVector
