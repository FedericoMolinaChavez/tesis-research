from preprocessing import createFeatureVector
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

trainx,trainy,testx,testy,Valx,Valy =  createFeatureVector('./database/Train_Positive_Sample_S1_3_8_HMM.sample','./database/Train_Negative_Sample_S1_3_8_1_HMM.sample',"./database/Test_Negative_Sample_S1_3_8_1_HMM.sample","./database/Test_Positive_Sample_S1_3_8_HMM.sample")
# load json and create model

models = automatic_loading()

loaded_model = models[0] 


a  = loaded_model.predict(testx, verbose=1, batch_size=4)
a = np.argmax(a, axis=1)
print(a)
results = []
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


trainx,trainy,testx,testy,Valx,Valy =  createFeatureVector('./database/Train_Positive_Sample_S2_6_5_HMM.sample','./database/Train_Negative_Sample_S2_6_5_1_HMM.sample',"./database/Test_Negative_Sample_S2_6_5_1_HMM.sample","./database/Test_Positive_Sample_S2_6_5_HMM.sample")
# load json and create model

#models = automatic_loading()

loaded_model = models[2] 


a  = loaded_model.predict(testx, verbose=1, batch_size=4)
a = np.argmax(a, axis=1)
print(a)
results = []
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