from preprocessing import trueCreateFeatureVector
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras import optimizers
from tensorflow.keras.layers import Dense, Embedding, LSTM
import numpy as np 
from tensorflow.keras.models import model_from_json
from tensorflow.keras.models import load_model
import analisisResults
from tensorflow.keras import backend
trainx,trainy,testx,testy,Valx,Valy =  trueCreateFeatureVector('./trainables/testPost1','./trainables/trestneg1')
config = tf.ConfigProto( device_count = {'GPU': 1} ) 
sess = tf.Session(config=config) 
backend.set_session(sess)
class LSTMdef():
    def __init__(self, numLayers, numCells, drop, recurrDrop, recurrActivation, optim, loss, batch, learningRate, amsgrad,epochs):
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
        self.epochs = epochs
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
            optimizerx = optimizers.SGD(lr=0.01, momentum=0.0, nesterov=False)
            self.model.compile(loss = self.loss, optimizer = optimizerx,metrics=['accuracy'])
        if(self.optim == 'adagrad'):
            optimizerx = optimizers.Adagrad(lr=0.01)
            self.model.compile(loss = self.loss, optimizer = optimizerx,metrics=['accuracy'])
        if(self.optim == 'RMSprop'):
            optimizerx = optimizers.RMSprop(lr=0.001, rho=0.9)
            self.model.compile(loss = self.loss, optimizer = optimizerx,metrics=['accuracy'])
        if(self.optim == 'Adamax'):
            optimizerx = optimizers.Adamax(lr=0.002, beta_1=0.9, beta_2=0.999)
            self.model.compile(loss = self.loss, optimizer = optimizerx,metrics=['accuracy'])
        if(self.optim == 'Nadam'):
            optimizerx = optimizers.Nadam(lr=0.002, beta_1=0.9, beta_2=0.999)
            self.model.compile(loss = self.loss, optimizer = optimizerx,metrics=['accuracy'])
    def test(self):
        print(self.model.summary())
        #print(trainx.shape[1])
        self.model.fit(trainx,trainy, batch_size=32, epochs=self.epochs, verbose=5)
        score,acc = self.model.evaluate(Valx,Valy,verbose=2,batch_size=4)
        #print("Logloss score : %.2f" % (score))
        #print("Validation set accuracy: %.2f" % (acc))
        a = self.model.predict_classes(testx, verbose=1, batch_size=4)
        #print(a)
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
        #print(analisis.testAccuracy())
        #print(analisis.testPresicion())
        #print(analisis.testSensitivity())
        #print(analisis.testSpecificity())
        #print(analisis.MattCorr())
        #print(2*((analisis.testPresicion()*analisis.testSensitivity())/(analisis.testSensitivity()+analisis.testPresicion())))
        return(analisis)
