import math
import re

class Bayes_Classifier:
    def __init__(self):
        self.classes = []
        self.class_counts = {}
        self.feature_counts = {}
        self.vocabulary = set()

    def preprocess_text(self, text):
        # Remove non-alphabetic characters and convert to lowercase
        text = re.sub(r'[^a-zA-Z]', ' ', text).lower()
        # Tokenize the text
        words = re.findall(r'\b\w+\b', text)
        # Remove stop words
        stop_words = set(['the', 'a', 'an', 'is', 'are', 'to', 'in', 'for', 'of'])
        words = [word for word in words if word not in stop_words]

        return words

    def train(self, lines):
        for line in lines:
            label, _, text = line.split('|')
            words = self.preprocess_text(text)
            if label not in self.classes:
                self.classes.append(label)
                self.class_counts[label] = 0
                self.feature_counts[label] = {}
            self.class_counts[label] += 1
            for word in words:
                self.vocabulary.add(word)
                if word not in self.feature_counts[label]:
                    self.feature_counts[label][word] = 0
                self.feature_counts[label][word] += 1

    def classify(self, lines):
        predictions = []
        for line in lines:
            _, _, text = line.split('|')
            words = self.preprocess_text(text)
            max_prob = float('-inf')
            max_class = None
            for c in self.classes:
                prob_c = math.log(self.class_counts[c]) - math.log(sum(self.class_counts.values()))
                prob_x_c = 0
                for word in words:
                    count_wc = self.feature_counts[c].get(word, 0) + 1
                    count_c = sum(self.feature_counts[c].values()) + len(self.vocabulary)
                    prob_wc = math.log(count_wc) - math.log(count_c)
                    prob_x_c += prob_wc
                prob_c_x = prob_c + prob_x_c
                if prob_c_x > max_prob:
                    max_prob = prob_c_x
                    max_class = c
            predictions.append(max_class)
        return predictions
