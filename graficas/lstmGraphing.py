import numpy as np
import matplotlib.pyplot as plt



          
                       
                                              
                                               

acc = (90.625,96.78571429)
prec = (91.42857143,96.89363563)
recall = (96.15384615,95.38461538)
spec = (66.66666667,97.4137931)
MCC = (76.15384615,93.31724869)
F1 = (93.73169303,96.38852583 )

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
ax.set_title('Sitio de clivaje 9')
ax.set_xticks(ind)
ax.set_xticklabels(('80/20','70/30'))
ax.legend()


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