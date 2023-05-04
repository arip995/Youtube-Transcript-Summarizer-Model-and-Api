from flask import Flask, request
from flask_cors import CORS, cross_origin
from transcript_api import APIv1
from youtube_transcript_api import TranscriptsDisabled as err
from segmenter import split_sentences
from extractive_summariser import text_summarizer
from typing import Dict, Any

app = Flask(__name__)
CORS(app)


@app.route("/extractive", methods=['POST'])
@cross_origin()
def extractive_summary():
    try:
        res: Dict[Any] = request.get_json()
        plain_text = APIv1(youtube_link=res.get('link')).get_video_id().get_transcript()    # noqa: E501
        return {'summary': text_summarizer(text=split_sentences(plain_text), percentage=res.get('percentage'))}, 200    # OK
    
    except (IndexError, ValueError, TypeError, ):
        return {'message': 'Invalid Parameters'}, 400   # bad request
    
    except err:
        return {'message': 'No transcripts available for this video'}, 500  # Internal server error


@app.route("/abstractive", methods=['POST'])
@cross_origin()
def abstractive_summary():
    return {'message': 'Not Implemented'}


if __name__ == '__main__':
    app.run(debug=True,)
