#!/usr/bin/env python
# coding: utf-8

# # This file demonstrates the preparation of "train.spacy" for trainning the model

# In[ ]:


import nltk
import pandas as pd
import re
import string
import numpy as np
from spacy.tokens import DocBin
import spacy
import json
from tqdm import tqdm
import random


# In[ ]:


colnames=['Words', 'Label'] 
data1 = pd.read_csv('/Users/dinesh/Documents/Data Science/oscer_project_test/data/NERModel1/train.tsv',names=colnames, header=None, sep='\t')


# In[ ]:


data1.head()


# In[ ]:


#Convert to string
data1['Words'] = data1['Words'].astype(str)
data1['Label'] = data1['Label'].astype(str)


# In[ ]:


#Remove all the unwanted characters from the dataset. Data Cleaning
data1['Words'] = data1['Words'].str.replace('[^a-zA-Z0-9\.]', '')
data1['Words'] = data1['Words'].str.replace('\d+', '')
data1['Words'] = data1['Words'].map(lambda x: x.rstrip(' ' + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' + ' ' ))


# In[ ]:


#...Handle NAN...


# In[ ]:


data1['Words'].replace('', np.nan, inplace=True)


# In[ ]:


data1['Words'].isnull().sum()


# In[ ]:


data1[ data1['Words'] != 'nan']


# In[ ]:


#Drop all the null rows and reset the index
data1.dropna(subset=['Words'], inplace=True)
data1.reset_index(drop=True, inplace=True)


# In[ ]:


data1.head(30)


# In[ ]:


len(data1['Words'])


# In[ ]:


#Preparing dataset in spacy entities format
Train_data = []
temp_sent = ""
temp_ent = []
start_idx = 0
end_index = 0
for i in range(0,len(data1['Words'])):
    if data1['Words'][i] == '.':
        temp_sent = temp_sent.strip()
        Train_data.append((temp_sent,{"entities": temp_ent}))
        temp_sent = ""
        temp_ent = []
        start_idx = 0
        end_index = 0
        
    else:
        word_length = len(data1['Words'][i])
        #start_idx = 0
        end_index = start_idx + word_length-1
        temp_ent.append((start_idx, end_index, data1['Label'][i]))
        temp_sent = temp_sent + ' ' + (data1['Words'][i])
        start_idx = end_index + 2
Train_data


# In[ ]:


import spacy
from spacy.tokens import DocBin

nlp = spacy.blank("en")
def create_tranning(TRAIN_DATA):
    db = DocBin()
    for text, annot in tqdm(TRAIN_DATA):
        doc = nlp.make_doc(text)
        #doc = dframcy.nlp(text)
        ents = []
        for start,end, label in annot["entities"]:
            span = doc.char_span(start,end,label = label,alignment_mode = "expand")
            if span is None:
                print("Skipping entity")
            else:
                ents.append(span)
        doc.ents = ents
        db.add(doc)
    return(db)

#db.to_disk("/Users/dinesh/Documents/Data Science/oscer_project_test/data/NERModel1/test.spacy") #save the docbin object


# In[ ]:


Train_Data = create_tranning(Train_data)
Train_Data.to_disk("/Users/dinesh/Documents/Data Science/oscer_project_test/data/NERModel1/train.spacy") #save the docbin object

