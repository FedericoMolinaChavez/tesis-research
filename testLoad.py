from stuff.preprocessingForRunning import bringDataFromArchive
from stuff.test import sequenceReaderDecoder
import tensorflow as tf
from keras.models import Sequential
from keras import optimizers
from keras.layers import Dense, Embedding, LSTM
import numpy as np 
import analisisResults
import keras
from keras.models import model_from_json
from keras.models import load_model
from automatic_model_loading import automatic_loading
changer = sequenceReaderDecoder('./stuff/ab079887.embl','./stuff/ab079887.SAMPLE')
changer.ReadBioSeqAndTransformToEvaluable(11)
testx =  bringDataFromArchive('./stuff/ab079887.SAMPLE')
# load json and create model

models = automatic_loading()

loaded_model = models[0] 


a  = loaded_model.predict(testx, verbose=1, batch_size=4)
a = np.argmax(a, axis=1)
print(a)
for i in a:
	if(i == 0):
		print(True)
b = models[1].predict(testx, verbose=1, batch_size=4)
b = np.argmax(b, axis=1)
print(b)
cont = 0
for i in b:
	if(i == 0):
		cont = cont+1
print(cont)
c = models[2].predict(testx, verbose=1, batch_size=4)
c = np.argmax(c,axis=1)
cont = 0
for i in c:
	if(i == 0):
		cont = cont+1
print(cont)
changer.ReadBioSeqAndTransformToEvaluable(9)
testx =  bringDataFromArchive('./stuff/ab079887.SAMPLE')
d = models[3].predict(testx,verbose=1, batch_size=4)
d = np.argmax(d, axis=1)
cont = 0
for i in d:
	if(i == 0):
		cont = cont+1
print(cont)
'''results = []
one = np.array([0,1])
zero = np.array([1,0])
for i in testy:
	#print(i)
	if(	np.array_equal(i,one)):
		results.append(1)
	if (np.array_equal(i,zero)):
		results.append(0)
print(len(results))
analisis = analisisResults.analisisResults(a,results)
print(analisis.testAccuracy())
print(analisis.testPresicion())
print(analisis.testSensitivity())
print(analisis.testSpecificity())
print(analisis.MattCorr())
print(2*((analisis.testPresicion()*analisis.testSensitivity())/(analisis.testSensitivity()+analisis.testPresicion())))
'''