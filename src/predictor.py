import pickle

# Load the model
model = pickle.load(open('src/models/NB_model.pkl','rb'))

# Load the vectorizer
vectorizer = pickle.load(open('src/models/NB_vectorizer.pkl','rb'))

class Predictor:
    def predict(self, text):
        # Vectorize the text
        text_vectorized = vectorizer.transform([text])

        # Make a prediction
        prediction = model.predict(text_vectorized)

        # get confidence
        confidence = model.predict_proba(text_vectorized)
        confidence = max(confidence[0])

        # Return the prediction and confidence
        return (prediction[0], confidence)
