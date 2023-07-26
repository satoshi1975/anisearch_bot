import requests
# import bot
URl = "https://api.trace.moe/search"


def get_file_name(name):
    list_id = []
    response = requests.post(URl,
                             data=open(f'{name}', "rb"),
                             headers={
                                 "Content-Type": "image/jpeg"
                             }).json()
    [list_id.append(i['anilist']) for i in response['result']]
    return list_id
