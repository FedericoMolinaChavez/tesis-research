from keras.layers.convolutional import Conv1D
from keras.layers import MaxPooling1D
from keras.layers import Dense, Embedding, MaxPool1D, Flatten
import numpy as np 
import analisisResults
from preprocessing import createFeatureVector
from keras.models import Model
from keras.layers import Input
from keras.optimizers import SGD
import keras
from keras.utils import np_utils

trainx,trainy,testx,testy,Valx,Valy =  createFeatureVector('./database/Train_Positive_Sample_S1_3_8_HMM.sample','./database/Train_Negative_Sample_S1_3_8_1_HMM.sample',"./database/Test_Negative_Sample_S1_3_8_1_HMM.sample","./database/Test_Positive_Sample_S1_3_8_HMM.sample")
#print(trainx.shape[0])
a = Input(shape = (trainx.shape[1],))
print(a)
input_c = Embedding(30, 128, input_length = trainx.shape[1])(a)
#a = Input(shape = (trainx.shape[0],trainx.shape[1],3))

tower_1 = Conv1D(64, 1, padding='same', activation='relu')(input_c)
tower_1 = Conv1D(64, 3, padding='same', activation='relu')(tower_1)

tower_2 = Conv1D(64, 1, padding='same', activation='relu')(input_c)
tower_2 = Conv1D(64, 5, padding='same', activation='relu')(tower_2)

tower_3 = MaxPool1D(pool_size=3, strides=1, padding='same')(input_c)
tower_3 = Conv1D(64, 1, padding='same', activation='relu')(tower_3)

output = keras.layers.concatenate([tower_1, tower_2, tower_3], axis = -1)
output = Flatten()(output)
out    = Dense(2, activation='sigmoid')(output)

model = Model(inputs = a, outputs = out)

model.compile(loss = 'categorical_crossentropy', optimizer='adam',metrics=['accuracy'])
print(model.summary())
model.fit(trainx,trainy, batch_size=32, epochs=10,verbose=5)
model_json = model.to_json()
with open("models/model1.json","w") as json_file:
	json_file.write(model_json)
model.save_weights("models/model1.h5")
score,acc = model.evaluate(Valx,Valy,verbose=2,batch_size=4)
print("Logloss score : %.2f" % (score))
print("Validation set accuracy: %.2f" % (acc))

r  = model.predict(Valx, verbose=1, batch_size=4)
r = np.argmax(r, axis=1)
print(r)
results = []
one = np.array([0,1])
zero = np.array([1,0])
for i in Valy:
	#print(i)
	if(	np.array_equal(i,one)):
		results.append(1)
	if (np.array_equal(i,zero)):
		results.append(0)

analisis = analisisResults.analisisResults(r,results)
print(analisis.testAccuracy())
print(analisis.testPresicion())
print(analisis.testSensitivity())
print(analisis.testSpecificity())
print(analisis.MattCorr())
print(2*((analisis.testPresicion()*analisis.testSensitivity())/(analisis.testSensitivity()+analisis.testPresicion())))