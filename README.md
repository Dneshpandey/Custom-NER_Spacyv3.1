# Custom-NER_Spacyv3.1
This project demonstrates how to build a Custom NER Model in Spacy v3.1
		
	Python 3.8.8 and Spacy v3.1

There are several changes between Spacy v3.1 and Spacy v2.
 
Overview of the model

Initially, the train and test datas are cleaned.
The data requires to be converted into the NER format. However, the converted data is in the old format and Spacy v3.1 no longer accepts  data in this format. This has to be converted to ".spacy" format by converting  first in doc and then a docbin.
(Refer model/Train.py and model/Test.py)
(FYI- model/Train.Spacy and model/Test.Spacy is provided.)


The custom training in Space v3. requires base_config.cfg and config.cfg. I created these files and provide a relevant data (train and test) and pipeline required for this project. We can play around many things before we train the model. 
(Refer: model/base_config.cfg and model/config.cfg)


I have developed a config.cfg that is required in Spacev3. Trainning process is carried out in Terminal.
	
	python -m spacy init fill-config base_config.cfg config.cfg

Once, all the requirements are met, I trained the custom model. (Sample screenshot is attached under the name: Training model(NER) Spacy v3
		
	python -m spacy train config.cfg --output ./output --paths.train ./train.spacy --paths.dev ./dev.spacy

(Refer: model/output)
 Once the model is fully trained, it can be saved. 

(Refer: Final_test.py)
Finally, I made a prediction with my final model. Sample Screenshot is attached.

Additional Info:
The pipelines are a great and easy way to use models for inference. The Hugging Face transformers package is an immensely popular Python library providing pretrained models that are extraordinarily useful for a variety of natural language processing (NLP) tasks.
