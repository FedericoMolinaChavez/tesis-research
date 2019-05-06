import numpy as np
import matplotlib.pyplot as plt

acc = [95.74074074]
prec = [95.92105263]
recall = [88.88888889]
spec = [99.16666667]
MCC = [83.58305674]
F1 = [92.26967089]

																											
									
fig, ax = plt.subplots()

g = [acc,prec,recall,spec,MCC,F1]
y = ["acc","prec","recall","spec","MCC","F1"]
first = ax.scatter(y,g, label='LSTM')

					

									
																										
acc = [93.75]
prec = [94.17101081]
recall = [91.42857143]
spec = [95]
MCC = [86.84848967]
F1 = [92.77952983]

g = [acc,prec,recall,spec,MCC,F1]
y = ["acc","prec","recall","spec","MCC","F1"]
first = ax.scatter(y,g, label='CNN')

ax.set_ylabel('Resultados en porcentaje')
ax.set_title('Sitio de clivaje 1')

ax.legend()

plt.show()