from keras.models import model_from_json
from keras.models import load_model

model_names = {'clivage_1_json' : 'models/model1.json',
			   'clivage_1' : 'models/model1.h5',
			   'clivage_2_json' : 'models/model2.json',
			   'clivage_2' : 'models/model2.h5',
			   'clivage_3_json' : 'models/model3.json',
			   'clivage_3' : 'models/model3.h5',
			   'clivage_4_json' : 'models/model4.json',
			   'clivage_4' : 'models/model4.h5',
			   'clivage_5_json' : 'models/model5.json',
			   'clivage_5' : 'models/model5.h5',
			   'clivage_6_json' : 'models/model6.json',
			   'clivage_6' : 'models/model6.h5',
			   'clivage_7_json' : 'models/model7.json',
			   'clivage_7' : 'models/model7.h5',
			   'clivage_8_json' : 'models/model8.json',
			   'clivage_8' : 'models/model8.h5',
			   'clivage_9_json' : 'models/model9.json',
			   'clivage_9' : 'models/model9.h5'}

def automatic_loading () :
	keys = list(model_names.keys())
	#print(keys)
	models = []
	j = 0
	for i in range(0,int(len(keys)/2)):
		try:
			i = i*2
			json_file = open(model_names.get(keys[i]), 'r')
			loaded_model_json = json_file.read()
			json_file.close()
			loaded_model = model_from_json(loaded_model_json)
			loaded_model.load_weights(model_names.get(keys[i+1]))
			print("Loaded model from disk")
			models.append(loaded_model)
		except Exception as e:
			raise
		else:
			pass
		finally:
			pass
		
	return models

#print(automatic_loading())