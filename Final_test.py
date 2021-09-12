#!/usr/bin/env python
# coding: utf-8

# # Due to the time constrain, I have done a informal test. This model can be improvised.

# In[1]:


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


# #('By analysing tumour from patients with sporadic cell prolymphocytic leukaemia a rare clonal malignancy with similarities to a mature cell leukaemia seen in we demonstrate a high frequency of mutations in',
#  {'entities': [(0, 1, 'O'),
#    (3, 11, 'O'),
#    (13, 18, 'B'),
#    (20, 23, 'O'),
#    (25, 32, 'O'),
#    (34, 37, 'O'),
#    (39, 46, 'B'),
#    (48, 51, 'I'),
#    (53, 66, 'I'),
#    (68, 76, 'I'),
#    (78, 78, 'O'),
#    (80, 83, 'O'),
#    (85, 90, 'B'),
#    (92, 101, 'I'),
#    (103, 106, 'O'),
#    (108, 119, 'O'),
#    (121, 122, 'O'),
#    (124, 124, 'O'),
#    (126, 131, 'B'),
#    (133, 136, 'I'),
#    (138, 146, 'I'),
#    (148, 151, 'O'),
#    (153, 154, 'O'),
#    (156, 157, 'O'),
#    (159, 169, 'O'),
#    (171, 171, 'O'),
#    (173, 176, 'O'),
#    (178, 186, 'O'),
#    (188, 189, 'O'),
#    (191, 199, 'O'),
#    (201, 202, 'O')]})

# In[55]:


nlp = spacy.load(R"/Users/dinesh/Documents/Data Science/oscer_project_test/data/NERModel1/output/model-best") #load the best model


# In[56]:


doc = nlp('By analysing tumour from patients with sporadic cell prolymphocytic leukaemia a rare clonal malignancy with similarities to a mature cell leukaemia seen in we demonstrate a high frequency of mutations in')


# In[57]:


[(ent.text, ent.label_) for ent in doc.ents]


# #('Sporadic prostate carcinoma is the most common male cancer in the Western world yet many of the major genetic events involved in the progression of this often fatal cancer remain to be elucidated',
#  {'entities': [(0, 7, 'B'),
#    (9, 16, 'I'),
#    (18, 26, 'I'),
#    (28, 29, 'O'),
#    (31, 33, 'O'),
#    (35, 38, 'O'),
#    (40, 45, 'O'),
#    (47, 50, 'B'),
#    (52, 57, 'I'),
#    (59, 60, 'O'),
#    (62, 64, 'O'),
#    (66, 72, 'O'),
#    (74, 78, 'O'),
#    (80, 82, 'O'),
#    (84, 87, 'O'),
#    (89, 90, 'O'),
#    (92, 94, 'O'),
#    (96, 100, 'O'),
#    (102, 108, 'O'),
#    (110, 115, 'O'),
#    (117, 124, 'O'),
#    (126, 127, 'O'),
#    (129, 131, 'O'),
#    (133, 143, 'O'),
#    (145, 146, 'O'),
#    (148, 151, 'O'),
#    (153, 157, 'O'),
#    (159, 163, 'O'),
#    (165, 170, 'B'),
#    (172, 177, 'O'),
#    (179, 180, 'O'),
#    (182, 183, 'O'),
#    (185, 194, 'O')]})

# In[68]:


doc = nlp('Sporadic prostate carcinoma is the most common male cancer in the Western world yet many of the major genetic events involved in the progression of this often fatal cancer remain to be elucidated')
[(ent.text, ent.label_) for ent in doc.ents]


# In[69]:


doc = nlp('cancer')
[(ent.text, ent.label_) for ent in doc.ents]

