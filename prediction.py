import pickle

# Load the model
model = pickle.load(open('LR_model.pkl','rb'))

# Load the vectorizer
vectorizer = pickle.load(open('vectorizer.pkl','rb'))

class Predictor:
    def predict(self, text):
        # Vectorize the text
        text_vectorized = vectorizer.transform([text])

        # Make a prediction
        prediction = model.predict(text_vectorized)

        return prediction[0]
