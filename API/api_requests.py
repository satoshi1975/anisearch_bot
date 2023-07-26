"""запрос к API по медиа"""
import requests

URL = 'https://graphql.anilist.co'

QUERY = """query($id_media:Int,$name_title:String,$type:MediaType,$page_media:Int=1,
$page_char:Int,$genres:[String],$rank:Int,$tags:[String],
$sort:[MediaSort])
{
  Page(page:$page_media,perPage:1){
    media(id:$id_media,type:$type,genre_in:$genres,averageScore_lesser:$rank,search:$name_title,
      sort:$sort,tag_in:$tags){
      id
      type
      siteUrl
      title{
        english
        romaji
        native
      }
      coverImage{
        large
      }
      startDate {
        year
        month
        day
      }
      endDate {
        year
        month
        day
      }
      format
      description
      studios(sort:FAVOURITES_DESC){
        nodes{
          id
          name
        }
      }
      characters(page:$page_char,perPage:1,sort:ROLE) {
        nodes{
          id
          description
          name {
            full
            native
          }
          image {
            large
          }
          age
          description
          siteUrl
          
        }
      }
      episodes

    }
    
  }
}


"""


#функция запроса к API по медиа
def show_media(dic, page):
    dic['page_media'] = page
    response = requests.post(URL,
                             timeout=5,
                             json={
                                 "query": QUERY,
                                 'variables': dic
                             }).json()

    view = response['data']['Page']['media'][0]

    result = {}
    result['id'] = view['id']
    result['url'] = view['siteUrl']
    result['img'] = view['coverImage']['large']
    result['start'] = view['startDate']
    result['end'] = view['endDate']
    result['format'] = view['format']
    result['description'] = view['description']
    if view['type'] == 'ANIME':
        result['studios'] = view['studios']['nodes'][0]['name']
    else:
        result['studios'] = 'None'
    result['episodes'] = view['episodes']
    result['type'] = view['type']
    if view['title']['english'] is not None:
        result['title'] = view['title']['english']
    elif view['title']['romaji'] is not None:
        result['title'] = view['title']['romaji']
    else:
        result['title'] = view['title']['native']
    # print(result)
    return result


def show_char(id_media, page):
    """функция запроса к API по персонажу"""
    search_dict = {'id_media': id_media, 'page_char': page}
    response = requests.post(URL,
                             timeout=5,
                             json={
                                 "query": QUERY,
                                 'variables': search_dict
                             }).json()
    view = response['data']['Page']['media'][0]['characters']['nodes'][0]
    return view
