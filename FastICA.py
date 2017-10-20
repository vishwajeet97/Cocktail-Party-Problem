import numpy as np
np.random.seed(7)

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

def FastICA(X, vectors, eps):
	"""FastICA technique is used.
	The function returns one independent component.
	X is assumed to be centered and whitened.
	The paper by A. Hyvarinen and E. Oja is in itself the best resource out there for it.
	Independent Component Analysis:Algorithms and Applications - A. Hyvarinen and E. Oja
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