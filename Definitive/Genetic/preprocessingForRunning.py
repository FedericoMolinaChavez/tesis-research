import numpy as np 
import pickle as pk 


def bringDataFromArchive(path):
    f = open(path, 'r')
    contentInArchive = f.readlines()
   # print(contentInArchive)
    test = []
    for i in contentInArchive:
        aux = i [ : len(i) - 2]
        ans1 = aux.split(' ')
        a2 = [int(i) for i in ans1]
        #print(a2)
        test.append(a2)
    test = np.array(test)
    return(test)    
#bringDataFromArchive('ab079887.SAMPLE')