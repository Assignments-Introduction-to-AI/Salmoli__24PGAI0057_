import nltk
nltk.download('punkt')
nltk.download('wordnet')
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import re

class Bayes_Classifier:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(ngram_range=(1, 2), stop_words='english')
        self.clf = MultinomialNB(alpha=0.01)
        self.ps = PorterStemmer()
        self.wnl = WordNetLemmatizer()

    def preprocess_text(self, text):
        # Lower casing
        text = text.lower()
        
        # Remove punctuation
        text = re.sub(r'[^\w\s]', '', text)
        
        # Tokenize and stem/lemmatize text
        tokens = word_tokenize(text)
        stemmed_tokens = [self.ps.stem(token) for token in tokens]
        lemmatized_tokens = [self.wnl.lemmatize(token) for token in stemmed_tokens]
        
        # Return preprocessed text as a string
        return ' '.join(lemmatized_tokens)

    def train(self, lines):
        texts = []
        labels = []
        for line in lines:
            stars, _, text = line.split('|')
            preprocessed_text = self.preprocess_text(text)
            texts.append(preprocessed_text)
            labels.append(stars)
        X = self.vectorizer.fit_transform(texts)
        self.clf.fit(X, labels)

    def classify(self, lines):
        texts = []
        for line in lines:
            _, _, text = line.split('|')
            preprocessed_text = self.preprocess_text(text)
            texts.append(preprocessed_text)
        X = self.vectorizer.transform(texts)
        return self.clf.predict(X).tolist()