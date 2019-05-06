from preprocessing import createFeatureVector
import tensorflow.contrib.learn as skflow
import numpy as np
trainx,trainy,testx,testy =  createFeatureVector('./database/Train_Positive_Sample_S3_2_8_HMM.sample','./database/Train_Negative_Sample_S3_2_8_1_HMM.sample')
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(trainx)

trainx = scaler.transform(trainx)
testx = scaler.transform(testx)


#def my_model(X, y):
#    """This is DNN with 10, 20, 10 hidden layers, and dropout of 0.5 probability."""
#    layers = skflow.ops.dnn(X, [10, 20, 10], keep_prob=0.5)
#    return skflow.models.logistic_regression(layers, y)

#clf = skflow.TensorFlowEstimator(model_fn=my_model, n_classes=1)
clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(10,10,20,10,2), random_state=1)

'''clf = skflow.DynamicRnnEstimator(ProblemType.CLASSIFICATION,
    prediction_type,
    sequence_feature_columns,
    context_feature_columns=None,
    num_classes=1,
    num_units=10,
    cell_type='basic_rnn',
    optimizer='SGD',
    learning_rate=0.1,
    predict_probabilities=False,
    momentum=None,
    gradient_clipping_norm=5.0,
    dropout_keep_probabilities=None,
    model_dir=None,
    feature_engineering_fn=None,
    config=None
)'''

clf.fit(trainx,trainy)
prediction = clf.predict(testx)
print(prediction)
print(testy)
for i in range(len(testy)):
	if (prediction[i]==1):
		if(testy[i]==1):
			print(1)
#[4, 9, 9, 0, 6, 9, 3, 1, 6, 8]
from sklearn.metrics import classification_report,confusion_matrix
print(confusion_matrix(prediction,testy))
print(classification_report(prediction,testy))