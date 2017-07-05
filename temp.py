import numpy as np

a = np.array([[0.23, 0.14, 0.35], [0.32, 0.05, 0.17], [0.07, 0.31, 0.25]])
b = np.linalg.inv(a)
print b

# def g1(u):
# 	return np.tanh(u)

# def g2(u):
# 	return u*np.exp(-(u*u)/2)

# def g1_dash(u):
# 	d = g1(u)
# 	return 1 - d*d

# def g2_dash(u):
# 	return (1 - u*u)*np.exp(-(u*u)/2)

# w = np.array([.2, .4, .1])

# x = np.array([[1,2,3,4,5], [7,3,8,4,3], [9,5,2,5,7]])
# # print np.dot(x.T, w)
# s = g1_dash(np.dot(w.T, x))
# print s
# print np.mean(s)
# # first = np.dot(x, g1(np.dot(w.T, x)))/n