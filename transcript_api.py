from youtube_transcript_api import YouTubeTranscriptApi as yt, TranscriptsDisabled as err
import re
from typing import Tuple, Any


class APIv1:
    
    def __init__(self, youtube_link: str) -> None:
        self.link: str = youtube_link
        self.vid: str = ""
        self.vid_id: str = ""
    
    def get_video_id(self) -> Any:
        self.vid_id = re.findall('v=[a-zA-Z0-9-_]*', self.link)[0][2:]
        self.vid = yt.get_transcript(self.vid_id, languages=['en-US', 'en-GB','en-IN', 'en'])
        return self
    
    @staticmethod
    def _clean_data(data: str) -> str:
        param = re.compile(r'([[0-9A-Za-z,. ]*])|([-@#$%^&*?+_:;]*)|([\n])')
        return param.sub(repl="", string=data, count=len(data))
    
    def get_transcript(self) -> str:
        transcript = " ".join(map(lambda obj: APIv1._clean_data(obj['text']), self.vid))
        return transcript
    
    def get_duration(self) -> int:
        dur: int = sum(map(lambda obj: obj['duration'], self.vid))
        return int(dur)