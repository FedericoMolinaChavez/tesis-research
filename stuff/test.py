from Bio import SeqIO
import numpy as np
import os 

#print("something")

class sequenceReaderDecoder():
    def __init__(self, filePath, fileDestiny):
        self.filePath = filePath
        self.fileDestiny = fileDestiny
        self.aminoacids = {"G" : 0 ,"P" : 1,"A" : 2,"V" : 3,"L" : 4,"I" : 5,"M" : 6,"C" : 7,"F" : 8,"Y" : 9,"W" : 10,"H" : 11,"K" : 12,"R" : 13,"Q" : 14,"N" : 15,"E" : 16,"D" : 17,"S" : 18,"T" : 19}
    def setFilePath(self, filepath):
        self.filePath = filepath
    def setFileDestiny(self, filepath):
        self.filePath = filepath
    def ReadBioSeqAndTransformToTrainable(self, windowSize):
        record = SeqIO.read(self.filePath, "embl")
        print(dir(record))
        #print(record.features)
        cleavageloc = []
        for i in range(2,len(record.features)):
            #print (i.qualifiers)
            a = record.features[i].location.start
            print(a)
            cleavageloc.append(a)
            ##print(i.location.extract(record.seq))
        a = np.array(record.seq)
        a2 = [self.aminoacids[i] for i in a]
        #print(a2)
        startPosition = 0
        endPosition = windowSize
        endArray = []
        for i in range(0,len(a2)-(windowSize)):
            if(i-(windowSize//2) in cleavageloc):
                #print(True)
                subArray = [1, a2[startPosition:endPosition]]
                startPosition = startPosition+1
                endPosition = endPosition+1
                endArray.append(subArray)
            else:    
                subArray = [0,a2[startPosition:endPosition]]
                startPosition = startPosition+1
                endPosition = endPosition+1
                endArray.append(subArray)
        #print(endArray)
        ansStr= ''
        f = open(self.fileDestiny, 'w+')
        for i in endArray:
            ansStr = str(i[0])+' '
            for j in i[1]:
                ansStr += str(j)+' '
            ansStr += '\n'
            f.write(ansStr)
        f.close()
    def InverseTransform(self, filePath, windowSize):
        self.aminoacids = { 0 : "G" , 1 : "P", 2 : "A",  3 : "V",  4 : "L", 5 : "I" ,6 : "M",7 : "C",8 : "F",9 : "Y",10 : "W",11 : "H",12 : "K",13 : "R",14 : "Q",15 : "N",16 : "E",17 : "D",18 : "S",19 : "T"}
        f = open(filePath)
        test = []
        contentInArchive = f.readlines()
        for i in contentInArchive:
           aux = i [ : len(i) - 2]
           ans1 = aux.split(' ')
           a2 = [int(i) for i in ans1]
           a2 = a2[1 :]
           #print(a2)
           test.append(a2)
        fullArray = []
        for i in test[0]:
            fullArray.append(i)
        for i in range(1, len(test)):
            a = test[i][8]
            fullArray.append(a)
        a2 = [self.aminoacids[i] for i in fullArray]
        record = SeqIO.read(self.filePath, "embl")
        aOriginal = np.array(record.seq)
        #print(len(a2))
        #print(len(aOriginal))
        #print(aOriginal)
        for i in range(0, len(a2)):
            if(a2[i] != aOriginal[i]):
               print(a2[i])
               print(' ')
               print(aOriginal[i])
        print('es igual')

       
    def ReadBioSeqAndTransformToTrainableWithoutSaving(self, windowSize):
        record = SeqIO.read(self.filePath, "embl")
        #print(dir(record))
        #print(record.features)
        cleavageloc = []
        for i in range(2,len(record.features)):
            #print (i.qualifiers)
            a = record.features[i].location.start
            #print(a)
            cleavageloc.append(a)
            ##print(i.location.extract(record.seq))
        if(len(cleavageloc) > 9):
            cleavageloc = cleavageloc[ :9]
        a = np.array(record.seq)
        a2 = [self.aminoacids[i] for i in a]
        startPosition = 0
        endPosition = windowSize
        endArray = []
        cont = 1
        for i in range(0,len(a2)-windowSize):
            if(i-5 in cleavageloc):
                #print(True)
                subArray = [cont, a2[startPosition:endPosition]]
                startPosition = startPosition+1
                endPosition = endPosition+1
                endArray.append(subArray)
                cont = cont + 1
            else:    
                subArray = [0,a2[startPosition:endPosition]]
                startPosition = startPosition+1
                endPosition = endPosition+1
                endArray.append(subArray)
        #print(endArray)
        ansArray = []
        ansStr= ''
        for i in endArray:
            ansStr = str(i[0])+' '
            for j in i[1]:
                ansStr += str(j)+' '
            ansStr += '\n'
            ansArray.append(ansStr)
        return ansArray    
    def ReadBioSeqAndTransformToEvaluable(self, windowsSize):
        record = SeqIO.read(self.filePath, "embl")
        a = np.array(record.seq)
        a2 = [self.aminoacids[i] for i in a]
        startPosition = 0
        endPosition = windowsSize
        endArray = []
        for i in range(0,len(a2)-windowsSize): 
            subArray = a2[startPosition:endPosition]
            startPosition = startPosition+1
            endPosition = endPosition+1
            endArray.append(subArray)
        print(len(endArray))
        f = open(self.fileDestiny, 'w+')
        for i in endArray:
            #print(i)
            ansStr = ''
            for j in range(0,len(i)):
               ansStr += str(i[j])+' '
            ansStr += '\n'
            #print(ansStr)
            f.write(ansStr)
        f.close()
class TestTrainSetter():
    def __init__(self, directoryEMBLfiles, directoryTestTrain):
        self.directoryEMBLfiles = directoryEMBLfiles
        self.directoryTestTrain = directoryTestTrain
    def readFilesAndTransformLocally(self):
        reader = sequenceReaderDecoder('','')
        allFiles = []
        for filename in os.listdir(self.directoryEMBLfiles):
            if filename.endswith(".embl"):
                reader.setFilePath(self.directoryEMBLfiles +'/'+ filename)
                allFiles.append(reader.ReadBioSeqAndTransformToTrainableWithoutSaving(11))
        return allFiles
    def convertToUsable(self):
        fullArray = self.readFilesAndTransformLocally()
        test = []
        for j in fullArray:
            for i in j:
                aux = i [ : len(i) - 2]
                ans1 = aux.split(' ')
                a2 = [int(i) for i in ans1]
                #print(a2)
                test.append(a2)
        return test
    def splitPositiveFromNegative(self):
        complete = self.convertToUsable()
        pos = []
        neg = []
        for i in complete :
            if (i[0] == 0):
                neg.append(i)
            else:
                pos.append(i)
        return(pos,neg)
    def splitAndSafe(self):
        pos,neg = self.splitPositiveFromNegative()
        one = []
        two = []
        three = []
        four = []
        five = []
        six = []
        seven = []
        eight = []
        nine = []
        for i in pos :
            if (i[0] == 1):
                one.append(i)
            if (i[0] == 2):
                two.append(i)
            if (i[0] == 3):
                three.append(i)
            if (i[0] == 4):
                four.append(i)
            if (i[0] == 5):
                five.append(i)
            if (i[0] == 6):
                six.append(i)
            if (i[0] == 7):
                seven.append(i)
            if (i[0] == 8):
                eight.append(i)
            if (i[0] == 9):
                nine.append(i)
        f1 = open(self.directoryTestTrain+'/testPost1', 'w+')
        for i in one:
            ansStr = ''
            for j in i :
                ansStr += str(j) + ' '
            ansStr += '\n'
            f1.write(ansStr)  
        f1.close()
        f2 = open(self.directoryTestTrain+'/testPost2', 'w+')
        for i in two:
            ansStr = str(1) + ' '
            for j in range(1,len(i)) :
                ansStr += str(i[j]) + ' '
            ansStr += '\n'
            f2.write(ansStr)
        f2.close()
        
        f3 = open(self.directoryTestTrain+'/testPost3', 'w+')
        for i in three:
            ansStr = str(1) + ' '
            for j in range(1,len(i)) :
                ansStr += str(i[j]) + ' '
            ansStr += '\n'
            f3.write(ansStr)
        f3.close()

        f4 = open(self.directoryTestTrain+'/testPost4', 'w+')
        for i in four:
            ansStr = str(1) + ' '
            for j in range(1,len(i)) :
                ansStr += str(i[j]) + ' '
            ansStr += '\n'
            f4.write(ansStr)
        f4.close()

        f5 = open(self.directoryTestTrain+'/testPost5', 'w+')
        for i in five:
            ansStr = str(1) + ' '
            for j in range(1,len(i)) :
                ansStr += str(i[j]) + ' '
            ansStr += '\n'
            f5.write(ansStr)
        f5.close()    

        f6 = open(self.directoryTestTrain+'/testPost6', 'w+')
        for i in six:
            ansStr = str(1) + ' '
            for j in range(1,len(i)) :
                ansStr += str(i[j]) + ' '
            ansStr += '\n'
            f6.write(ansStr)
        f6.close()

        f7 = open(self.directoryTestTrain+'/testPost7', 'w+')
        for i in seven:
            ansStr = str(1) + ' '
            for j in range(1,len(i)) :
                ansStr += str(i[j]) + ' '
            ansStr += '\n'
            f7.write(ansStr)
        f7.close()

        f8 = open(self.directoryTestTrain+'/testPost8', 'w+')
        for i in eight:
            ansStr = str(1) + ' '
            for j in range(1,len(i)) :
                ansStr += str(i[j]) + ' '
            ansStr += '\n'
            f8.write(ansStr)
        f8.close()

        f9 = open(self.directoryTestTrain+'/testPost9', 'w+')
        for i in nine:
            ansStr = str(1) + ' '
            for j in range(1,len(i)) :
                ansStr += str(i[j]) + ' '
            ansStr += '\n'
            f9.write(ansStr)
        f9.close()   

        ninth = len(neg)//9
        for i in range(0,9):
            f = open(self.directoryTestTrain + '/trestneg'+str(i+1), 'w+')
            partition = neg [i*ninth : (i*ninth)+ninth]
            for i in partition:
                ansStr = ''
                for j in i :
                    ansStr += str(j) + ' '
                ansStr += '\n'
                f.write(ansStr)  
            f.close()

        #ReadBioSeqAndTransformToTrainableWithoutSaving
#newobj = sequenceReaderDecoder('ab079887.embl','ab079887.SAMPLE')
#newobj.ReadBioSeqAndTransformToTrainable(9)
#newobj.ReadBioSeqAndTransformToEvaluable(11)
#newobj = TestTrainSetter('./embl', './trainables')
#newobj.splitAndSafe()
#newobj.InverseTransform('ab079887.SAMPLE', 9)