from flask import Flask, render_template, redirect, url_for, session, request, jsonify
import src.predictor as predictor
import src.processing as processing

predictor = predictor.Predictor()
processor = processing.Processing()

# Initialize Flask app
app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def predict():
    if request.method == 'POST':
        text = request.json['description']
        processed_text = processor.preprocess_text(text)
        result = predictor.predict(processed_text)

        return jsonify({'success': True, 'result': result})
    else:
        return render_template('index.html')
    

if __name__ == '__main__':
    app.run(debug=True)

