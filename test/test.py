
#importing score function
from score import *


#importing model
lr_model_path = "/Users/Soham/Documents/CMI-SEM-4/AML/src/models/lr_model.sav"
lr_model = pkl.load(open(lr_model_path, "rb"))

# Defining input values to test the score function on
obvious_ham = "I am good"
obvious_spam = "click on this link"
threshold = 0.5


# Defining Unit Tests

# Smoke Test: Function returns values without crashing
def test_smoke(text=obvious_ham, model=lr_model, threshold=threshold) -> None:
    label, prop = score(text, model, threshold)
    assert label != None, "Prediction is non boolean"
    assert prop != None, "Propensity is not float"