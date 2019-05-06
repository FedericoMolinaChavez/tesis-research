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
		labels.append([int(i[: 1]),0])
		featureStep = []
		c = i[1 :]
		d = c.split(' ');
		for j in d:
			if(j != '' and j != '\n'):
				featureStep.append(int(j))
		if(len(featureStep) == 12):
			features.append(featureStep[2:])
		elif(len(featureStep) == 11):
			features.append(featureStep[1:])
		else:
			features.append(featureStep)
		featureStep = []
	res = []	
	for i in range(0,len(labels)):
		res.append([labels[i],features[i]])
	return res

def createFeatureVector (positive, negative, size=0.2):
	dataToProcess = []


	dataToProcess += bringDataFromArchive("./database/Train_Positive_Sample_S1_3_8_HMM.sample")
	dataToProcess += bringDataFromArchive("./database/Train_Negative_Sample_S1_3_8_1_HMM.sample")

	dataToProcess += bringDataFromArchive(negative)
	dataToProcess += bringDataFromArchive(positive)

	dataToProcess += bringDataFromArchive("./database/Train_Positive_Sample_S3_2_8_HMM.sample")
	dataToProcess += bringDataFromArchive("./database/Train_Negative_Sample_S3_2_8_1_HMM.sample")
	
	dataToProcess += bringDataFromArchive("./database/Train_Positive_Sample_S4_7_2_HMM.sample")
	dataToProcess += bringDataFromArchive("./database/Train_Negative_Sample_S4_7_2_1_HMM.sample")

	dataToProcess += bringDataFromArchive("./database/Train_Positive_Sample_S5_5_5_HMM.sample")
	dataToProcess += bringDataFromArchive("./database/Train_Negative_Sample_S5_5_5_1_HMM.sample")

	dataToProcess += bringDataFromArchive("./database/Train_Positive_Sample_S6_9_0_HMM.sample")
	dataToProcess += bringDataFromArchive("./database/Train_Negative_Sample_S6_9_0_1_HMM.sample")

	dataToProcess += bringDataFromArchive("./database/Train_Positive_Sample_S7_3_7_HMM.sample")
	dataToProcess += bringDataFromArchive("./database/Train_Negative_Sample_S7_3_7_1_HMM.sample")

	dataToProcess += bringDataFromArchive("./database/Train_Positive_Sample_S8_1_10_HMM.sample")
	dataToProcess += bringDataFromArchive("./database/Train_Negative_Sample_S8_1_10_1_HMM.sample")

	dataToProcess += bringDataFromArchive("./database/Train_Positive_Sample_S9_2_9_HMM.sample")
	dataToProcess += bringDataFromArchive("./database/Train_Negative_Sample_S9_2_9_1_HMM.sample")



	
	dataToProcess += bringDataFromArchive("./database/Test_Positive_Sample_S1_3_8_HMM.sample")
	dataToProcess += bringDataFromArchive("./database/Test_Negative_Sample_S1_3_8_1_HMM.sample")

	dataToProcess += bringDataFromArchive("./database/Test_Positive_Sample_S2_6_5_HMM.sample")
	dataToProcess += bringDataFromArchive("./database/Test_Negative_Sample_S2_6_5_1_HMM.sample")

	dataToProcess += bringDataFromArchive("./database/Test_Positive_Sample_S3_2_8_HMM.sample")
	dataToProcess += bringDataFromArchive("./database/Test_Negative_Sample_S3_2_8_1_HMM.sample")

	dataToProcess += bringDataFromArchive("./database/Test_Positive_Sample_S4_7_2_HMM.sample")
	dataToProcess += bringDataFromArchive("./database/Test_Negative_Sample_S4_7_2_1_HMM.sample")

	dataToProcess += bringDataFromArchive("./database/Test_Positive_Sample_S5_5_5_HMM.sample")
	dataToProcess += bringDataFromArchive("./database/Test_Negative_Sample_S5_5_5_1_HMM.sample")

	dataToProcess += bringDataFromArchive("./database/Test_Positive_Sample_S6_9_0_HMM.sample")
	dataToProcess += bringDataFromArchive("./database/Test_Negative_Sample_S6_9_0_1_HMM.sample")

	dataToProcess += bringDataFromArchive("./database/Test_Positive_Sample_S7_3_7_HMM.sample")
	dataToProcess += bringDataFromArchive("./database/Test_Negative_Sample_S7_3_7_1_HMM.sample")

	dataToProcess += bringDataFromArchive("./database/Test_Positive_Sample_S8_1_10_HMM.sample")
	dataToProcess += bringDataFromArchive("./database/Test_Negative_Sample_S8_1_10_1_HMM.sample")

	dataToProcess += bringDataFromArchive("./database/Test_Positive_Sample_S9_2_9_HMM.sample")
	dataToProcess += bringDataFromArchive("./database/Test_Negative_Sample_S9_2_9_1_HMM.sample")



	
	#print (dataToProcess)
	#random.shuffle(dataToProcess)
	features = np.array(dataToProcess)
	#print(len(features))
	train = features[ int(len(features)*size) :]
	trainX = []
	trainY = []
	testX = []
	testY = []
	#print(len(train))
	for i in train :
		trainY.append(i[0])
		trainX.append(i[1])

	test = features [: int(len(features)*size)]
	#print(len(test))
	for i in test :
		testY.append(i[0])
		testX.append(i[1])
	
	#print(trainX)
	#print(testY)
	return trainX,trainY,testX,testY


trainx,trainy,testx,testy = createFeatureVector('./database/Train_Positive_Sample_S2_6_5_HMM.sample','./database/Train_Negative_Sample_S2_6_5_1_HMM.sample')

#with open('aut_seq_pickle.pickle','wb') as f:
	#pickle.dump([trainx,trainy,testx,testy],f)