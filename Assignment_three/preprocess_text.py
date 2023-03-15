from nltk.corpus import stopwords
import string
from nltk.stem.porter import PorterStemmer
ps= PorterStemmer()

def preprocess_text(text):
    text = text.lower()
    words = nltk.word_tokenize(text)
    
    meaningful_instances = []
    
    for i in words:
        if i.isalnum() and i not in stopwords.words('english') and i not in string.punctuation:
            meaningful_instances.append(i)
            
    final_text = []
    
    for i in meaningful_instances:
        final_text.append(ps.stem(i))
        
    return " ".join(final_text)   