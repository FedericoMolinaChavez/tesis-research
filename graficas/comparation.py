import numpy as np
import matplotlib.pyplot as plt
					
acc = [93.75]
prec = [94.11764706]
recall = [92.30769231]
spec = [100]
MCC = [67.30769231]
F1 = [93.2038835]

																											
									
fig, ax = plt.subplots()

g = [acc,prec,recall,spec,MCC,F1]
y = ["acc","prec","recall","spec","MCC","F1"]
first = ax.scatter(y,g, label='LSTM')

					

												
																										
acc = [97.61904762]
prec = [97.6744186]
recall = [100]
spec = [96.55172414]
MCC = [100]
F1 = [	98.82352941	]

g = [acc,prec,recall,spec,MCC,F1]
y = ["acc","prec","recall","spec","MCC","F1"]
first = ax.scatter(y,g, label='CNN')

ax.set_ylabel('Resultados en porcentaje')
ax.set_title('Sitio de clivaje 6')

ax.legend()

plt.show()