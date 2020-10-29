import pickle
from google.cloud import storage
from flask import Flask, render_template, request
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer

# accessing bucket where model and vectorizer are stored
client = storage.Client()
bucket = client.get_bucket('week_7_demo')
blob1 = bucket.blob('model.pickle')
blob2 = bucket.blob('tfidf_vect.pickle')
blob1.download_to_filename('model_local')
blob2.download_to_filename('tfidf_vect')

# loading in pickled model and vectorizer
tfidf_vect = pickle.load(open('tfidf_vect', "rb"))
model = pickle.load(open('model_local', "rb"))

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/prediction', methods = ['POST', 'GET'])
def prediction():
    if request.method == 'POST':
        predictions = request.form
        for key, item in predictions.items():
            # extract string message
            sms = item
        # vectorize input text
        sms_transformed = tfidf_vect.transform([sms])

        # return prediction on vectorized text
        return model.predict(sms_transformed)[0]

if __name__ == '__main__':
    app.run(host = "127.0.0.1", port = 8080, debug = True)