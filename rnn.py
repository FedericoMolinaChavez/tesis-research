import tensorflow as tf
from tensorflow.python.ops import rnn, rnn_cell
import numpy as np
from preprocessing import createFeatureVector
import analisisResults
trainx,trainy,testx,testy =  createFeatureVector('./database/Train_Positive_Sample_S3_2_8_HMM.sample','./database/Train_Negative_Sample_S3_2_8_1_HMM.sample')

hm_epochs = 2
n_classes = 1
batch_size = 128

chunk_size = len(trainx[0])
n_chunks = 1
rnn_size = 11

x = tf.placeholder('float', [None, chunk_size,n_chunks])
y = tf.placeholder('float')

def recurrent_neural_network(x):
    layer = {'weights':tf.Variable(tf.random_normal([rnn_size, n_classes])),
                      'biases':tf.Variable(tf.random_normal([n_classes]))}
    x = tf.transpose(x, [1,0,2])
    x = tf.reshape (x, [-1, chunk_size])
    x = tf.split(x, n_chunks, 0)

    lstm_cell = rnn_cell.BasicLSTMCell(rnn_size,state_is_tuple=True)
    outputs, states = rnn.static_rnn(lstm_cell, x, dtype=tf.float32)
    output = tf.matmul(outputs[-1],layer['weights']) + layer['biases']

    return output

def train_neural_network(x):
    prediction = recurrent_neural_network(x)
    cost = tf.reduce_mean( tf.nn.softmax_cross_entropy_with_logits(logits=prediction,labels=y) )

    #optimizer = tf.train.GradientDescentOptimizer(0.1).minimize(cost)
    optimizer = tf.train.RMSPropOptimizer(0.1).minimize(cost)
    
   
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())

        for epoch in range(hm_epochs):
            epoch_loss = 0
            i = 0
            for _ in range(int(len(trainx)/batch_size)):
                epoch_x, epoch_y = np.array(trainx[i : i + batch_size]), np.array(trainy[i : i + batch_size])
                epoch_x = epoch_x.reshape((batch_size,chunk_size,1))
                _, c = sess.run([optimizer, cost], feed_dict={x: epoch_x, y: epoch_y})
                epoch_loss += c
                i = i+batch_size

            print('Epoch', epoch, 'completed out of',hm_epochs,'loss:',epoch_loss)

        correct = tf.equal(tf.argmax(prediction, 1), tf.argmax(y, 1))

        accuracy = tf.reduce_mean(tf.cast(correct, 'float'))        

        print('Accuracy:',accuracy.eval({x:np.array(testx).reshape((-1,chunk_size,1)), y:np.array(testy)}))
        results = []
        j = 0
        results = (sess.run(tf.argmax(prediction.eval(feed_dict={x : np.array(testx).reshape(-1 , chunk_size, n_chunks)}),1)))
        arrEsper = []            
        #print(testy)
        for i in range(len(testy)) :
            arrEsper.append(testy[i][0])
        
            
        analisis = analisisResults.analisisResults(results,arrEsper)
        print(results)
        #print(arrEsper)
        print(analisis.testAccuracy())
        print(analisis.testPresicion())
        print(analisis.testSensitivity())
        print(analisis.testSpecificity())
        

train_neural_network(x)