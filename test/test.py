
#importing score function
from score import *


#importing model
lr_model_path = "/Users/Soham/Documents/CMI-SEM-4/AML/src/models/lr_model.sav"
lr_model = pkl.load(open(lr_model_path, "rb"))

# Defining input values to test the score function on
obvious_ham = "I am good"
obvious_spam = "click on this link to go to heaven"
threshold = 0.5


# Defining Unit Tests

# Smoke Test: Function returns values without crashing
def test_smoke(text=obvious_ham, model=lr_model, threshold=threshold) -> None:
    label, prop = score(text, model, threshold)
    assert label != None, "Prediction is non boolean"
    assert prop != None, "Propensity is not float"
    
# Format Test: Check function input/output types 
def test_input_formats(text=obvious_ham, threshold=threshold, model=lr_model) -> None:
    label, prop = score(text, model, threshold)

    assert type(text) == str
    assert type(threshold) == float 
    assert type(label) == bool
    assert type(prop) == np.float64 
    
# Prediction Value Test
def test_pred_value(text=obvious_ham, threshold=threshold, model=lr_model) -> None:
    label, prop = score(text, model, threshold)

    assert label == False or label == True
    
# Propensity Value Test
def test_prop_value(text=obvious_ham, threshold=threshold, model=lr_model) -> None:
    label, prop = score(text, model, threshold)

    assert prop >= 0 and prop <= 1
    
# Check Prediction Value for Threshold = 0 Test
def test_pred_thres_zero(text=obvious_ham, threshold=threshold, model=lr_model) -> None:
    label, prop = score(text, model, threshold=0)

    assert label == True
    
# Check Prediction Value for Threshold = 1 Test
def test_pred_thres_one(text=obvious_ham, threshold=threshold, model=lr_model) -> None:
    label, prop = score(text, model, threshold=1)

    assert label == False

# Check Prediction Value for Threshold = 1 Test
def test_obvious_spam(text=obvious_spam, threshold=threshold, model=lr_model) -> None:
    label, prop = score(text, model, threshold)

    assert label == True, "Prob: {}".format(prop)

# Check Prediction Value for Threshold = 1 Test
def test_obvious_spam(text=obvious_spam, threshold=threshold, model=lr_model) -> None:
    label, prop = score(text, model, threshold)

    assert label == True, "Prob: {}".format(prop)