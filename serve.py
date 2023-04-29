from flask import Flask, request
from transcript_api import APIv1
from segmenter import split_sentences
from extractive_summariser import text_summarizer

app = Flask(__name__)


@app.route("/")
@app.route("/extractive", methods=['GET'])
def extractive_summary():
    try:
        link: str = request.args.get('link')
        try:
            summ = APIv1(youtube_link=link).get_video_id().get_transcript()
            return {'summary': summ}, 200
        except IndexError:
            return {'message': 'Invalid Youtube Link'}, 500
    except RuntimeError:
        return {'message': 'Invalid Named Parameters'}, 500


if __name__ == '__main__':
    app.run(debug=True)
