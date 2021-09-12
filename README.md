# Custom-NER_Spacyv3.1
This project demonstrates how to build a Custom NER Model in Space 3.1

Space v3.1 does not support or needs to be modified many things developed for Spacy v2.
 
Overview 
(Refer model/Train.py and model/Test.py)
	Initially, the both the train and test datas are cleaned.

	The data requires to be converted into the NER format.

	However, the converted data is in the old format and Space v3.1 no longer accepts the data in this NER format. This has to be converted to their .spacy format by 		converting these first in doc and then a docbin.

	FYI- model/Train.Spacy and model/Test.Spacy is provided.

(Refer: model/base_config.cfg and model/config.cfg)
	The custom training in Space v3. requires base_config.cfg and config.cfg. I created these files and provide a relevant data (train and test) and pipeline required for this 	project. We can play around many things before we train the model. 

	I developed config.cfg which is required in the Spacev3. while training the model. Command prompt or Terminal can be used
	
	        #python -m spacy init fill-config base_config.cfg config.cfg

Once, all the requirements are meet, I trained the custom model. (Sample screenshot is attached under the name: Training model(NER) Spacy v3

(Refer: model/output)
 Once the model is fully trained, it can be saved. 

(Refer: Final_test.py)
Finally, I made a prediction with my final model. Sample Screenshot is attached.
