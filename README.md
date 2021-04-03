# sample_spam_classifier_appengine
I built a sample ham-or-spam classifier using a scikit-learn model deployed on Google App Engine. Data is obtained from [Kaggle](https://www.kaggle.com/uciml/sms-spam-collection-dataset)

## Breakdown Video
If you want to see a 30-second demo of the file run locally, feel free to click the image below.

[![Alt text](https://img.youtube.com/vi/3EUoh797zMs/0.jpg)](https://www.youtube.com/watch?v=3EUoh797zMs)

## Requirements
- A pickled vectorizer (I used TF-IDF, but you can use CountVectorizer if that suits you).
- A pickled model (I used Logistic Regression from scikit-learn with default parameters).
- **Note**: If you require further assistance, I've included a notebook folder which contains the notebook I used to pickle the text vectorizer and model I used in the breakdown video above. If you want to run the application locally through commandline or terminal, please comment lines 4 and lines 9 to 16.
