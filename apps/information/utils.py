# API client library
import googleapiclient.discovery
import googleapiclient.errors

from urllib.parse import urlparse, parse_qs

from config.config import DEVELOPER_KEY

# API information
api_service_name = "youtube"
api_version = "v3"

# API client
youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey=DEVELOPER_KEY)


class Util:
    @staticmethod
    def get_yt_video_id(url):
        if url.startswith(('youtu', 'www')):
            url = 'http://' + url

        query = urlparse(url)

        if 'youtube' in query.hostname:
            if query.path == '/watch':
                return parse_qs(query.query)['v'][0]
            elif query.path.startswith(('/embed/', '/v/')):
                return query.path.split('/')[2]
        elif 'youtu.be' in query.hostname:
            return query.path[1:]
        else:
            raise ValueError

    @staticmethod
    def get_description(url):
        video_id = Util.get_yt_video_id(url)

        request = youtube.videos().list(
            part="snippet",
            id=video_id,
            fields="items(snippet(description))"
        )

        data = request.execute()
        return data['items'][0]['snippet']['description']
