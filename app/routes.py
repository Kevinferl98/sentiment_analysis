from flask import Blueprint, render_template, request, jsonify
from textblob import TextBlob
from .mongo import MongoDB

bp = Blueprint('routes', __name__)
mongo = MongoDB('mongodb://localhost:27017', 'sentimentDB', 'sentiment_analysis')

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/sentiment_analysis', methods=['POST'])
def sentiment_analysis():
    request_body = request.json
    if 'text' not in request_body:
        return jsonify({'error': 'No text was passed'}), 400
    try:
        response = analyze_sentiment(request_body['text'])
        mongo.collection.insert_one(response.copy())
        return response, 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

def analyze_sentiment(text):
    textBlob_res = TextBlob(text)
    return {
        'text': text,
        'polarity': textBlob_res.sentiment.polarity,
        'subjectivity': textBlob_res.sentiment.subjectivity
    }