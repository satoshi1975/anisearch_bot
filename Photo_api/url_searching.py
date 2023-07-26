import requests
import urllib.parse

URL = "https://api.trace.moe/search?url={}"


def url_request(photo_url):
    list_id = []
    response = requests.get(URL.format(
        urllib.parse.quote_plus(photo_url))).json()
    [list_id.append(i['anilist']) for i in response['result']]
    return list_id
