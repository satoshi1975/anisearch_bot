"""запрос к API по персонажу"""

import requests
from filters import templates

URL = 'https://graphql.anilist.co'

QUERY = """query($search:String,$page:Int,$id:Int)
{
  Page(page:$page,perPage:1){
    characters(search:$search,id:$id){
        id
      name {
        full
      }
      age
      image {
        large
      }
      siteUrl
      description
      media(sort:FAVOURITES,perPage:4) {
        nodes{
          id
          title{
            english
            romaji
            native
          }
        }
      }
    }
    
    
  }
}
"""


#функция запроса к API
def char_request(dic):

    response = requests.post(URL,
                             timeout=5,
                             json={
                                 "query": QUERY,
                                 "variables": dic
                             }).json()

    return templates.templates_char_by_name(
        response['data']['Page']['characters'][0])
