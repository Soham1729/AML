from helpers import *

bow_path = "/Users/Soham/Documents/CMI-SEM-4/AML/src/models/bow.sav"
tfidf_path = "/Users/Soham/Documents/CMI-SEM-4/AML/src/models/tfidf.sav"
bow = pkl.load(open(os.path.join(bow_path), "rb"))
tfidf = pkl.load(open(os.path.join(tfidf_path), "rb"))

def score(text: str, model, threshold: float):
    
    bow_text = bow.transform([preprocess_text(text)])
    tfidf_text = tfidf.transform(bow_text)[0]
    
    propensity = model.predict_proba(tfidf_text)[0][1]
    
    if propensity >= threshold:
        prediction = bool(1)
    else:
        prediction = bool(0)

    return prediction, propensity
