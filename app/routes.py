from flask import Blueprint, render_template, request, jsonify
from textblob import TextBlob

bp = Blueprint('routes', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/sentiment_analysis', methods=['POST'])
def sentimenti_analysis():
    request_body = request.json
    if 'text' not in request_body:
        return jsonify({'error': 'No text was passed'}), 400
    return analyze_sentiment(request_body['text']), 200
    

def analyze_sentiment(text):
    textBlob_res = TextBlob(text)
    return {
        'text': text,
        'polarity': textBlob_res.sentiment.polarity,
        'subjectivity': textBlob_res.sentiment.subjectivity
    }