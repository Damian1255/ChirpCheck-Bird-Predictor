from flask import Flask, render_template, redirect, url_for, session, request, jsonify
import prediction

predictor = prediction.Predictor()

# Initialize Flask app
app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def predict():
    text = request.form['text']
    processed_text = text.lower()   
    prediction = predictor.predict(processed_text)

    return render_template('index.html', text=prediction)

if __name__ == '__main__':
    app.run(debug=True)

