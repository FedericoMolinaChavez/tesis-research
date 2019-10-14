from preprocessing import trueCreateFeatureVector
import tensorflow as tf
from keras.models import Sequential
from keras import optimizers
from keras.layers import Dense, Embedding, LSTM
import numpy as np 
import keras
from keras.models import model_from_json
from keras.models import load_model
import analisisResults

trainx,trainy,testx,testy,Valx,Valy =  trueCreateFeatureVector('./trainables/testPost9','./trainables/trestneg9')
config = tf.ConfigProto( device_count = {'GPU': 1} ) 
sess = tf.Session(config=config) 
keras.backend.set_session(sess)
class LSTMdef():
    def __init__(self, numLayers, numCells, drop, recurrDrop, recurrActivation, optim, loss, batch, learningRate, amsgrad):
        self.numLayers = numLayers
        self.numCells = numCells
        self.drop = drop
        self.recurrDrop = recurrDrop
        self.recurrActivation = recurrActivation
        self.optim = optim
        self.loss = loss
        self.batch = batch
        self.learningRate = learningRate
        self.amsgrad = amsgrad
        self.model = Sequential()
    def generate(self):
        print(trainx.shape[1])
        self.model.add(Embedding(20, 128, input_length = trainx.shape[1]))
        for i in range(0,self.numLayers-1):
            self.model.add(LSTM(self.numCells, dropout = self.drop, recurrent_dropout=self.recurrDrop, return_sequences = True, unroll = True,recurrent_activation=self.recurrActivation,bias_initializer='RandomNormal',implementation=1))
        self.model.add(LSTM(self.numCells, dropout = self.drop, recurrent_dropout=self.recurrDrop, unroll = True,recurrent_activation=self.recurrActivation,bias_initializer='RandomNormal',implementation=1))
        self.model.add(Dense(2,activation='softmax', bias_initializer='RandomNormal'))
        if(self.optim == 'adam'):
            optimizerx = optimizers.Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=None, decay=0.0, amsgrad=False)
            self.model.compile(loss = self.loss, optimizer = optimizerx,metrics=['accuracy'])
        if(self.optim == 'adam' and self.amsgrad == 'True'):
            optimizerx = optimizers.Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=None, decay=0.0, amsgrad=True)
            self.model.compile(loss = self.loss, optimizer = optimizerx,metrics=['accuracy'])
        if(self.optim == 'SGD'):
            optimizerx = optimizers.SGD(learning_rate=0.01, momentum=0.0, nesterov=False)
            self.model.compile(loss = self.loss, optimizer = optimizerx,metrics=['accuracy'])
        if(self.optim == 'adagrad'):
            optimizerx = optimizers.Adagrad(learning_rate=0.01)
            self.model.compile(loss = self.loss, optimizer = optimizerx,metrics=['accuracy'])
        if(self.optim == 'RMSprop'):
            optimizerx = optimizers.RMSprop(learning_rate=0.001, rho=0.9)
            self.model.compile(loss = self.loss, optimizer = optimizerx,metrics=['accuracy'])
        if(self.optim == 'Adamax'):
            optimizerx = optimizers.Adamax(learning_rate=0.002, beta_1=0.9, beta_2=0.999)
            self.model.compile(loss = self.loss, optimizer = optimizerx,metrics=['accuracy'])
        if(self.optim == 'Nadam'):
            optimizerx = optimizers.Nadam(learning_rate=0.002, beta_1=0.9, beta_2=0.999)
            self.model.compile(loss = self.loss, optimizer = optimizerx,metrics=['accuracy'])
    def test(self):
        print(self.model.summary())
        self.model.fit(trainx,trainy, batch_size=32, epochs=2, verbose=5)
        score,acc = self.model.evaluate(Valx,Valy,verbose=2,batch_size=4)
        print("Logloss score : %.2f" % (score))
        print("Validation set accuracy: %.2f" % (acc))
        a = self.model.predict_classes(testx, verbose=1, batch_size=4)
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
        return(analisis)
