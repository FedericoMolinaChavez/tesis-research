import numpy as np
import matplotlib.pyplot as plt

									
																																					
																																											
																																																							
acc = (95 ,  93.75, 90	)
prec = (95.25707491,  94.17101081, 90.90909091)
recall = (87.77777778,  91.42857143, 83.33333333)
spec = (98.0952381,  95, 92.85714286)
MCC = (82.71314474,  86.84848967, 76.19047619)
F1 = (91.35432526		,  92.77952983	, 86.95652174		)

ind = np.arange(len(acc))  # the x locations for the groups
width = 0.3  # the width of the bars

fig, ax = plt.subplots()

rects1 = ax.bar(ind - width/6, acc, width,
                color='Navy', label='Cert')
rects2 = ax.bar(ind , prec, width,
                color='orange', label='prec')
rects3 = ax.bar(ind + width/6, recall, width,
                color='darkviolet', label='Recall')
rects4 = ax.bar(ind + 2*width/6, spec, width,
                color='red', label='Esp')
rects5 = ax.bar(ind + 3*width/6, MCC, width,
                color='forestgreen', label='MCC')
rects6 = ax.bar(ind + 4*width/6, F1, width,
                color='yellow', label='F1')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Resultados en porcentaje')
ax.set_title('Sitio de clivaje 1')
ax.set_xticks(ind)
ax.set_xticklabels(('Vainilla', 'Google-i', 'VGG-i'))
ax.legend()
ax.axis([None, None, 75, 102])



def autolabel(rects, xpos='center'):
    """
    Attach a text label above each bar in *rects*, displaying its height.

    *xpos* indicates which side to place the text w.r.t. the center of
    the bar. It can be one of the following {'center', 'right', 'left'}.
    """

    xpos = xpos.lower()  # normalize the case of the parameter
    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0.5, 'right': 0.57, 'left': 0.43}  # x_txt = x + w*off

    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()*offset[xpos], 1.01*height,
                '{}'.format(height), ha=ha[xpos], va='bottom')


#autolabel(rects1, "left")
#autolabel(rects2, "right")

plt.show()