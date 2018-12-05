from preprocessing import createFeatureVector
import tensorflow as tf
from keras.models import Sequential
from keras import optimizers
from keras.layers import Dense, Embedding, LSTM
import numpy as np 
import analisisResults
import keras

config = tf.ConfigProto( device_count = {'GPU': 1} ) 
sess = tf.Session(config=config) 
keras.backend.set_session(sess)


trainx,trainy,testx,testy,Valx,Valy =  createFeatureVector('./database/Train_Positive_Sample_S1_3_8_HMM.sample','./database/Train_Negative_Sample_S1_3_8_1_HMM.sample')

print(trainx.shape)
model = Sequential()
model.add(Embedding(30, 128, input_length = trainx.shape[1]))
model.add(LSTM(200, dropout = 0.2, recurrent_dropout=0.3, return_sequences = True, unroll = True,recurrent_activation='hard_sigmoid',bias_initializer='RandomNormal',implementation=1))
model.add(LSTM(200, dropout = 0.2, recurrent_dropout=0.3, unroll = True,recurrent_activation='hard_sigmoid',bias_initializer='RandomNormal',implementation=1))
model.add(Dense(2,activation='softmax', bias_initializer='RandomNormal'))
optimizerx = optimizers.Adagrad(lr=0.01, epsilon=None, decay=0.0)
model.compile(loss = 'categorical_crossentropy', optimizer = optimizerx,metrics=['accuracy'])
print(model.summary())
model.fit(trainx,trainy, batch_size=16, epochs=10,verbose=5)

score,acc = model.evaluate(Valx,Valy,verbose=2,batch_size=4)
print("Logloss score : %.2f" % (score))
print("Validation set accuracy: %.2f" % (acc))

a = model.predict_classes(testx, verbose=1, batch_size=4)
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
analisis = analisisResults.analisisResults(a,results)
print(analisis.testAccuracy())
print(analisis.testPresicion())
print(analisis.testSensitivity())
print(analisis.testSpecificity())
print(analisis.MattCorr())
print(2*((analisis.testPresicion()*analisis.testSensitivity())/(analisis.testSensitivity()+analisis.testPresicion())))
