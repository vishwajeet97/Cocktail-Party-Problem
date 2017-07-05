import scipy.io.wavfile as io
import matplotlib.pyplot as plt
import numpy as np

rate, data = io.read('./sounds/mixed1.wav')

# print rate
plt.figure(1)
plt.title('Signal Wave...')
plt.plot(data)
plt.show()
# print type(data)