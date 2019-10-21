# Este codigo se encarga de leer todo el archivo de datos de testeo y entreno, luego se formatean

import numpy as np
import random
import pickle


def bringDataFromArchive(nameOfArchive):
	file = open(nameOfArchive,'r')
	contentInArchive = file.readlines()
	labels = []
	features = []
	contentInArchive = contentInArchive [1 :]
	for i in contentInArchive:
		if (int(i[: 1]) == 1):
			labels.append([1,0])
		else:
			labels.append([0,1])
		featureStep = []
		d = i.split(' ')
		d = d [2 :]
		for j in d:
			if(j != '' and j != '\n'):
				featureStep.append(int(j)+1)
		features.append(featureStep)
		featureStep = []
	res = []	
	for i in range(0,len(labels)):
		res.append([labels[i],features[i]])
	return res

def trueCreateFeatureVector(positive, negative):
	dataToTrain = []
	dataToTest = []
	auxP = bringDataFromArchive(positive)
	f = bringDataFromArchive(negative)
	f = f[int(len(f)*0.99) : ]
	postrain = auxP[int(len(auxP)  * 0.2) :]
	negtrain = f[int(len(f) * 0.2) :]
	dataToTrain += postrain
	dataToTrain += negtrain
	
	postest = auxP[ : int(len(auxP)  * 0.2)] 
	negtest = f[ : int(len(f) * 0.2) ]
	dataToTest += postest
	dataToTest += negtest


	trainX = []
	trainY = []
	testX = []
	testY = []
	ValX = []
	ValY = []

	train = dataToTrain[int(len(dataToTrain)*0.2) :]
	val = dataToTrain[ : int(len(dataToTrain)*0.2)]

	for i in train :
		c = i[0]
		d = i[1]
		#d = d.reshape(len(i[1]),1)
		trainY.append(c)
		trainX.append(d)
	for i in val :
		c = i[0]
		d = i[1]
		#d = d.reshape(len(i[1]),1)
		ValY.append(c)
		ValX.append(d)
	test = dataToTest
	random.shuffle(test)
	for i in test :
		c = i[0]
		d = i[1]
		#d = d.reshape(len(i[1]),1)
		testY.append(c)
		testX.append(d)
	#print(trainY)
	trainY = np.array(trainY)
	trainX = np.array(trainX)
	testX = np.array(testX)
	testY = np.array(testY)
	ValX = np.array(ValX)
	ValY = np.array(ValY)

	return trainX,trainY,testX,testY,ValX,ValY


def createFeatureVector (positive, negative,negt,post, size=0.2):
	dataToProcess = []
	dataToTest = []
	auxP = bringDataFromArchive(positive)
	f = bringDataFromArchive(negative)
	
	f = f[int(len(f)*0.999) : ]

	total1 = len(auxP)+len(f)
	print(len(auxP)/total1)
	
	
	
	dataToTest += bringDataFromArchive(negt)
	dataToTest = dataToTest[int(len(dataToTest)*0.999) : ]
	c = bringDataFromArchive(post)

	total = len(c)+len(dataToTest)
	print(len(c)/total)

	dataToTest += bringDataFromArchive(post)
	

	
	train = auxP[int(len(auxP)*0.2) : ]
	train += f[int(len(f)*0.2) :]
	val = auxP[ : int(len(auxP)*0.2)]
	val += f[ : int(len(f)*0.2)]
	#print(val)
	random.shuffle(train)
	random.shuffle(val)
	
	trainX = []
	trainY = []
	testX = []
	testY = []
	ValX = []
	ValY = []
	
	for i in train :
		c = i[0]
		d = i[1]
		#d = d.reshape(len(i[1]),1)
		trainY.append(c)
		trainX.append(d)
	for i in val :
		c = i[0]
		d = i[1]
		#d = d.reshape(len(i[1]),1)
		ValY.append(c)
		ValX.append(d)
	test = dataToTest
	random.shuffle(test)
	for i in test :
		c = i[0]
		d = i[1]
		#d = d.reshape(len(i[1]),1)
		testY.append(c)
		testX.append(d)
	trainY = np.array(trainY)
	trainX = np.array(trainX)
	testX = np.array(testX)
	testY = np.array(testY)
	ValX = np.array(ValX)
	ValY = np.array(ValY)

	return trainX,trainY,testX,testY,ValX,ValY


#trainx,trainy,testx,testy,Valx,Valy =  createFeatureVector('./database/Train_Positive_Sample_S9_2_9_HMM.sample','./database/Train_Negative_Sample_S9_2_9_1_HMM.sample')
#print(trainy)
#print(testy)
#with open('aut_seq_pickle.pickle','wb') as f:
#	pickle.dump([trainx,trainy,testx,testy],f)