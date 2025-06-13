import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

in_file = 'corpus.txt'
out_file = 'clean_corp.txt'

with open(in_file, 'r', encoding='utf-8') as fin, open(out_file, 'w', encoding='utf-8') as fout:
    for line in fin:
        text = line.strip() 
        words = nltk.word_tokenize(text.lower())
        words_no_stop = [w for w in words if w not in stop_words]
        
        if len(words_no_stop) < 6:
            continue
        
        lemmas = [lemmatizer.lemmatize(w) for w in words_no_stop]

        fout.write(' '.join(lemmas) + '\n')
        

