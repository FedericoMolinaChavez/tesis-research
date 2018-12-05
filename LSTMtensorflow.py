import tensorflow as tf
from tensorflow.contrib import rnn 
from preprocessing import createFeatureVector
import numpy as np
np.set_printoptions(threshold=np.inf)
import analisisResults

trainx,trainy,testx,testy =  createFeatureVector('./database/Train_Positive_Sample_S3_2_8_HMM.sample','./database/Train_Negative_Sample_S3_2_8_1_HMM.sample')


"""docstring for LSTM"""
input_size = len(trainx[0])
output_size = 1
time_steps = 5
learning_rate = 0.01
unit_size = 1
numLayers = 128
batchSize = 128
num_cells = 11
x =tf.placeholder('float', [None, input_size , unit_size])
y = tf.placeholder('float')
weights = {'out' : tf.Variable(tf.random_normal([num_cells, output_size]))}
biases = {'out' : tf.Variable(tf.random_normal([output_size], dtype=tf.float32))}

		
		

	
def lstm_cell_definition(num_cells):
	lstm_layer = rnn.LSTMCell(num_cells , forget_bias = 1, name='basic_lstm_cell')
	return lstm_layer
	
def lstm_network_definition(x):
	stacked_lstm = rnn.MultiRNNCell([lstm_cell_definition(num_cells) for _ in range(numLayers)])

	x = tf.transpose(x, [1,0,2])
	x = tf.reshape (x, [-1, input_size])
	x = tf.split(x, unit_size, 0)

	output, states = tf.nn.static_rnn(stacked_lstm, x, dtype=tf.float32)
	logits = tf.matmul(output[-1], weights['out']) + biases['out']
	return logits

def train(x):
	prediction = lstm_network_definition(x)
	cost = tf.reduce_logsumexp(tf.nn.sigmoid_cross_entropy_with_logits(logits=prediction, labels=y))
	optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)
	with tf.Session() as sess:
		sess.run(tf.global_variables_initializer())
		for epoch in range(time_steps):
			epoch_loss = 0
			i = 0
			for _ in range(int(len(trainx)/batchSize)):
				
				epoch_x, epoch_y = trainx[i : i + batchSize], trainy[i : i + batchSize]
				epoch_x = epoch_x.reshape((batchSize, input_size, 1))
				_, c = sess.run([optimizer, cost], feed_dict={x : epoch_x, y: epoch_y})
				epoch_loss += c
				i = i+batchSize
			print("loss "+ str(epoch_loss))
		correct = tf.equal(tf.argmax(prediction), tf.argmax(y))
		accuracy = tf.reduce_mean(tf.cast(correct, 'float'))
		print('Accuracy:',accuracy.eval({x:np.array(testx).reshape((-1,input_size,unit_size)), y:np.array(testy)}))
		results = []
		j = 0
		a = prediction.eval(feed_dict={x : np.array(testx).reshape(-1 , input_size, unit_size)})
		#print(a)
		#results = (sess.run(tf.argmax(prediction.eval(feed_dict={x : np.array(testx).reshape(-1 , input_size, unit_size)}),1)))
		'''arrEsper = []
		for i in range(len(testy)):
			arrEsper.append(testy[i])
		arrEsper = np.array(arrEsper)
		analisis = analisisResults.analisisResults(results,arrEsper)
		print(results)
		print(arrEsper)
		print(analisis.testAccuracy())
		print(analisis.testPresicion())
		print(analisis.testSensitivity())
		print(analisis.testSpecificity())
		#init = tf.global_variables_initializer()'''
		

		
train(x)
