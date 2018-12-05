import matplotlib.pyplot as plt
import numpy as np

nameOfArchive = "accuracy.v"
file = open(nameOfArchive,'r')

contentInArchive = file.readlines()
y = []
for i in contentInArchive:
	i.replace('\r','')
	i.replace('\n','')
	print(i)
	y.append(float(i))
file2 = open("test.v",'r')
a = file2.readlines()

file3 = open("real.v",'r')
l = file3.readlines()
x = []
for i in l :
	x.append(float(i))
plt.plot(a,y,x)
plt.ylabel('porcentaje')
plt.xlabel('numero de prueba')
plt.title('MCC')
plt.show()