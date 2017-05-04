import numpy
import keras
#from keras.models import Sequential
#from keras.layers import Dense
#from keras.layers import Dropout
#from keras.layers import LSTM
#from keras.callbacks import ModelCheckpoint
#from keras.utils import np_utils

filename = "file.txt"
raw_text = open(filename).read()
raw_text = raw_text.lower()

chars = sorted(list(set(raw_text)))

n_chars = len(raw_text)
n_vocab = len(chars)

seq_length = 100
dataX = []
dataY = []
for i in range(0, n_chars - seq_length, 1):
	seq_in = raw_text[i: i+seq_length]
	seq_out = raw_text[i+seq_length]
	dataX.append([ord(char) for char in seq_in])
	dataY.append(ord(seq_out))

n_patterns = len(dataX)
print("total number of patterns: ", n_patterns)