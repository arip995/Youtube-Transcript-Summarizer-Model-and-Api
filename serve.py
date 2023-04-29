from flask import Flask, request
from transcript_api import APIv1
from segmenter import split_sentences
from extractive_summariser import text_summarizer
from typing import Dict

app = Flask(__name__)


@app.route("/")
@app.route("/extractive", methods=['POST'])
def extractive_summary():
    try:
        gay: Dict[str | float] = request.get_json()

        plain_text = APIv1(youtube_link=gay.get('link')).get_video_id().get_transcript()
        return {'summary': text_summarizer(text=split_sentences(plain_text), percentage=gay.get('percentage'))}, 200
    
    except (IndexError, ValueError, TypeError):
        return {'message': 'Invalid Parameters'}, 400


@app.route("/abstractive", methods=['POST'])
def abstractive_summary():
    return {'message': 'Not Implemented'}


if __name__ == '__main__':
    app.run(debug=True)
