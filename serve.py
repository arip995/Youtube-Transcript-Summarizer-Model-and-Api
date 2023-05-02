from flask import Flask, request
from flask_cors import CORS, cross_origin
from transcript_api import APIv1
from youtube_transcript_api import TranscriptsDisabled as err
from segmenter import split_sentences
from extractive_summariser import text_summarizer
from typing import Dict, Any

app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route("/extractive", methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
def extractive_summary():
    try:
        gay: Dict[Any] = request.get_json()
        plain_text = APIv1(youtube_link=gay.get('link')).get_video_id().get_transcript()    # noqa: E501
        return {'summary': text_summarizer(text=split_sentences(plain_text), percentage=gay.get('percentage'))}, 200    # noqa: E501
    
    except (IndexError, ValueError, TypeError, ):
        return {'message': 'Invalid Parameters'}, 400
    
    except err:
        return {'message': 'No transcripts available for this video'}, 500


@app.route("/abstractive", methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
def abstractive_summary():
    return {'message': 'Not Implemented'}


if __name__ == '__main__':
    app.run(debug=True,)
