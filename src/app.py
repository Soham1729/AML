import os,sys,json

sys.path.append('/Users/Soham/Documents/CMI-SEM-4/AML/test')

from score import *
from helpers import *

from flask import Flask, request, render_template

app = Flask(__name__, template_folder = '/Users/Soham/Documents/CMI-SEM-4/AML/test/template')

#importing model
lr_model_path = "/Users/Soham/Documents/CMI-SEM-4/AML/src/models/lr_model.sav"
lr_model = pkl.load(open(lr_model_path, "rb"))

# Setting threshold value
threshold=0.5

@app.route('/') 
def home():
    return render_template('post.html')

@app.route('/score', methods=['POST'])
def spam():
    sent = request.form['sent']
    label, prop = score(sent, lr_model, threshold)
    prop = round(prop, 3)
    lbl = "Spam" if label == 1 else "Not Spam"

    dict1 = {"Sentence": sent, "Prediction": lbl, "Propensity": prop}
    json_object = json.dumps(dict1, indent = 4) 

    return json_object
