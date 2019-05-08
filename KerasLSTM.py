from preprocessing import trueCreateFeatureVector
import tensorflow as tf
from keras.models import Sequential
from keras import optimizers
from keras.layers import Dense, Embedding, LSTM
import numpy as np 
import analisisResults
import keras
from keras.models import model_from_json
from keras.models import load_model

config = tf.ConfigProto( device_count = {'GPU': 1} ) 
sess = tf.Session(config=config) 
keras.backend.set_session(sess)


trainx,trainy,testx,testy,Valx,Valy =  trueCreateFeatureVector('./stuff/trainables/testPost1','./stuff/trainables/trestneg1')

print(trainx.shape)
model = Sequential()
model.add(Embedding(30, 128, input_length = trainx.shape[1]))
model.add(LSTM(500, dropout = 0.2, recurrent_dropout=0.3, return_sequences = True, unroll = True,recurrent_activation='hard_sigmoid',bias_initializer='RandomNormal',implementation=1))
model.add(LSTM(500, dropout = 0.2, recurrent_dropout=0.3, return_sequences = True, unroll = True,recurrent_activation='hard_sigmoid',bias_initializer='RandomNormal',implementation=1))
model.add(LSTM(500, dropout = 0.2, recurrent_dropout=0.3, return_sequences = True, unroll = True,recurrent_activation='hard_sigmoid',bias_initializer='RandomNormal',implementation=1))
model.add(LSTM(500, dropout = 0.2, recurrent_dropout=0.3, unroll = True,recurrent_activation='hard_sigmoid',bias_initializer='RandomNormal',implementation=1))
model.add(Dense(2,activation='softmax', bias_initializer='RandomNormal'))
optimizerx = optimizers.Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=None, decay=0.0, amsgrad=False)
model.compile(loss = 'poisson', optimizer = optimizerx,metrics=['accuracy'])
print(model.summary())
model.fit(trainx,trainy, batch_size=32, epochs=15,verbose=5)

model_json = model.to_json()
with open("models/model2.json","w") as json_file:
	json_file.write(model_json)
model.save_weights("models/model2.h5")

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
