import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import contractions
import string

import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')

class Processing:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()
        self.punctuation = string.punctuation
        self.contractions = contractions

    def preprocess_text(self, text):
        # Lowercase the text
        text = text.lower()
        # Expand contractions
        text = ' '.join([self.contractions.fix(word) for word in text.split()])
        # replace the text with 'specie' if the text contains the species name
        species = ['Javan Myna', 'Black-naped Oriole', 'Little Egret', 'Collared Kingfisher']
        for specie in species:
            text = text.replace(specie.lower(), 'specie')
        # Remove punctuation
        text = ''.join([char for char in text if char not in self.punctuation])
        # Tokenize the text
        tokens = word_tokenize(text)
        # Remove stop words
        tokens = [word for word in tokens if word not in self.stop_words]
        # remove token that is 2 characters or less
        tokens = [word for word in tokens if len(word) > 2]
        # POS tagging
        pos_tags = nltk.pos_tag(tokens)
        # Lemmatize the text using the POS tags
        text = ' '.join([self.lemmatizer.lemmatize(word, self.get_wordnet_pos(pos_tag)) for word, pos_tag in pos_tags])
        
        return text
    
    def get_wordnet_pos(self, tag):
        if tag.startswith('J'):
            return nltk.corpus.wordnet.ADJ
        elif tag.startswith('V'):
            return nltk.corpus.wordnet.VERB
        elif tag.startswith('N'):
            return nltk.corpus.wordnet.NOUN
        elif tag.startswith('R'):
            return nltk.corpus.wordnet.ADV
        else:
            return nltk.corpus.wordnet.NOUN