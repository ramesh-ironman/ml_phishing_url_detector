from flask import Flask, request, render_template
import joblib
import pandas as pd
from extractor import extract_features

app = Flask(__name__)
model = joblib.load('phish_model.pkl')

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        url = request.form['url']
        feats = extract_features(url)
        pred = model.predict(feats)[0]
        return render_template('result.html', safe=pred==-1, url=url)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
