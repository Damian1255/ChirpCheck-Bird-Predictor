import pickle
import json

class Predictor:
    def __init__(self):
        # Load the model and vectorizer
        self.model = pickle.load(open('src/models/model.pkl','rb'))
        self.vectorizer = pickle.load(open('src/models/vectorizer.pkl','rb'))

        # Load the bird information
        with open('static/bird_info.json') as f:
            self.bird_info = json.load(f)
    
    def predict(self, text):
        # Vectorize the text
        text_vectorized = self.vectorizer.transform([text])

        # Make a prediction & get confidence score
        prediction = self.model.predict(text_vectorized)
        confidence = self.model.predict_proba(text_vectorized)

        # retrieve the bird information
        bird = self.bird_info[str(prediction[0])]
        bird['confidence'] = round(max(confidence[0]) * 100, 2)

        # Return the information
        return bird
