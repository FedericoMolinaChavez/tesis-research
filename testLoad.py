from stuff.preprocessingForRunning import bringDataFromArchive
from stuff.test import sequenceReaderDecoder
import tensorflow as tf
from keras.models import Sequential
from keras import optimizers
from keras.layers import Dense, Embedding, LSTM
import numpy as np 
import analisisResults
import keras
import sys
from keras.models import model_from_json
from keras.models import load_model
from automatic_model_loading import automatic_loading
import random
def testLoad(fileorig, otherfile):
	changer = sequenceReaderDecoder('./stuff/ab079887.embl','./stuff/ab079887.SAMPLE')
	changer.ReadBioSeqAndTransformToEvaluable(10)
	testx =  bringDataFromArchive('./stuff/ab079887.SAMPLE')
	testx = testx[1:]
	# load json and create model

	models = automatic_loading()	

	loaded_model = models[0] 
	c1 = []
	c2 = []
	c3 = []
	c4 = []
	c5 = []
	c6 = []
	c7 = []
	c8 = []
	c9 = []

	a  = loaded_model.predict(testx, verbose=1, batch_size=4)
	a = np.argmax(a, axis=1)

	for i in range(0, len(a)):
		if(a[i] == 0):
			c1.append(i)
	random.shuffle(a)
	b = models[1].predict(testx, verbose=1, batch_size=4)
	b = np.argmax(b, axis=1)

	cont = 0
	for i in range(0, len(b)):
		if(b[i] == 0):
			c2.append(i)


	c = models[2].predict(testx, verbose=1, batch_size=4)
	c = np.argmax(c,axis=1)
	cont = 0
	for i in range(0, len(c)):
		if(c[i] == 0):
			c3.append(i)


	d = models[3].predict(testx,verbose=1, batch_size=4)
	d = np.argmax(d, axis=1)
	cont = 0
	for i in range(0, len(d)):
		if(d[i] == 0):
			c4.append(i)


	d = models[4].predict(testx,verbose=1, batch_size=4)
	d = np.argmax(d, axis=1)
	cont = 0
	for i in range(0, len(d)):
		if(d[i] == 0):
			c5.append(i)


	d = models[5].predict(testx,verbose=1, batch_size=4)
	d = np.argmax(d, axis=1)
	cont = 0
	for i in range(0, len(d)):
		if(d[i] == 0):
			c6.append(i)


	d = models[6].predict(testx,verbose=1, batch_size=4)
	d = np.argmax(d, axis=1)
	cont = 0
	for i in range(0, len(d)):
		if(d[i] == 0):
			c7.append(i)


	d = models[7].predict(testx,verbose=1, batch_size=4)
	d = np.argmax(d, axis=1)
	cont = 0
	for i in range(0, len(d)):
		if(d[i] == 0):
			c8.append(i)


	d = models[8].predict(testx,verbose=1, batch_size=4)
	d = np.argmax(d, axis=1)
	cont = 0
	for i in range(0, len(d)):
		if(d[i] == 0):
			c9.append(i)
	random.shuffle(c1)
	random.shuffle(c2)
	random.shuffle(c3)
	random.shuffle(c4)
	random.shuffle(c5)
	random.shuffle(c6)
	random.shuffle(c7)
	random.shuffle(c8)
	random.shuffle(c9)
	if ( len(c1) > 6):
		c1 = c1[ : 6]
	if ( len(c2) > 6):
		c2 = c2[ : 6]
	if ( len(c3) > 6):
		c3 = c3[ : 6]
	if ( len(c4) > 6):
		c4 = c4[ : 6]
	if ( len(c5) > 6):
		c5 = c5[ : 6]
	if ( len(c6) > 6):
		c6 = c6[ : 6]
	if ( len(c7) > 6):
		c7 = c7[ : 6]
	if ( len(c8) > 6):
		c8 = c8[ : 6]
	if ( len(c9) > 6):
		c9 = c9[ : 6]
	return(c1, c2, c3, c4, c5, c6, c7, c8, c9)

