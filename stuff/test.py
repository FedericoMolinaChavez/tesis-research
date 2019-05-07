from Bio import SeqIO
import numpy as np


#print("something")

class sequenceReaderDecoder():
    def __init__(self, filePath, fileDestiny):
        self.filePath = filePath
        self.fileDestiny = fileDestiny
        self.aminoacids = {"G" : 0 ,"P" : 1,"A" : 2,"V" : 3,"L" : 4,"I" : 5,"M" : 6,"C" : 7,"F" : 8,"Y" : 9,"W" : 10,"H" : 11,"K" : 12,"R" : 13,"Q" : 14,"N" : 15,"E" : 16,"D" : 17,"S" : 18,"T" : 19}
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
        startPosition = 0
        endPosition = windowSize
        endArray = []
        for i in range(0,len(a2)-windowSize):
            if(i-5 in cleavageloc):
                print(True)
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

#newobj = sequenceReaderDecoder('ab079887.embl','ab079887.SAMPLE')
#newobj.ReadBioSeqAndTransformToTrainable(11)
#newobj.ReadBioSeqAndTransformToEvaluable(11)