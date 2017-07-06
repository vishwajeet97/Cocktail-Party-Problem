import skimage
import numpy as np
from skimage import io
from skimage.transform import resize
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def mixSounds(sound_list, weights):
	""" Return a sound array mixed in proportion with the ratios given by weights"""
	mixSound = np.zeros(len(sound_list[0]))
	i = 0
	for sound in sound_list:
		mixSound += sound*weights[i]
		i += 1

	return mixSound 

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
		plt.savefig(path + ".jpg", bbox_inches='tight')
	plt.show()