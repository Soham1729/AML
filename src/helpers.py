# This contains all the helper functions used in the project implementation
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pickle as pkl
from collections import Counter
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer
from sklearn.metrics import accuracy_score,confusion_matrix,precision_score,recall_score, f1_score, classification_report, precision_recall_curve, auc
import nltk
from nltk.corpus import stopwords
import string
import mlflow
import mlflow.sklearn
import urlparse



def preprocess_text(text):   # import raw txt data 
    text = text.lower()
    words = nltk.word_tokenize(text)
    
    meaningful_instances = []
    
    for i in words:
        if i.isalnum() and i not in stopwords.words('english') and i not in string.punctuation:
            meaningful_instances.append(i)
            
    final_text = []
    
    for i in meaningful_instances:
        final_text.append(i)
        
    return " ".join(final_text)    

def preprocess_data(data):   #import pandas dataframe to the function
    
    data = data.drop_duplicates(keep = 'first')
    data.loc[:, 'num_char'] = data['Message'].apply(len)
    data.loc[:, 'num_word'] = data['Message'].apply(lambda x: len(nltk.word_tokenize(x)))
    data.loc[:, 'num_sentence'] = data['Message'].apply(lambda x: len(nltk.sent_tokenize(x)))
    
    return data

