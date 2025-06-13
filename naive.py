from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import joblib

file = 'clean_corp.txt'

texts = []
labels = []

with open(file, encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        tag, text = line[:7], line[7:].strip()
        if tag == '< 01 > ':
            labels.append(1)
        elif tag == '< 02 > ':
            labels.append(2)
  
        texts.append(text)

print(labels)

model = make_pipeline(TfidfVectorizer(), MultinomialNB())

model.fit(texts, labels)

joblib.dump(model, 'text_classifier.pkl')
