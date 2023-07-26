"""шаблоны для структуризации результатов запросов к API"""


def templates_media(res):
    """Шаблоны для описания медиа"""
    if res['start']['day'] is None:
        start_date = ''
        end_date = ''
    elif res['start']['day'] is not None and res['end']['day'] is not None:
        start_date = f'{res["start"]["day"]}.{res["start"]["month"]}.{res["start"]["year"]} - '
        end_date = f'{res["end"]["day"]}.{res["end"]["month"]}.{res["end"]["year"]}'
    else:
        start_date = f'{res["start"]["day"]}.{res["start"]["month"]}.{res["start"]["year"]} - '
        end_date = 'present time'


    caption= f'Title: {res["title"]}\n\n{start_date}{end_date}\n' \
             f'format: {res["format"]}\n' \
             f'episodes: {res["episodes"]}\n' \
             f'studios: {res["studios"]}'
    return caption


def templates_char_by_name(dic):
    """шаблоны для информации о персонаже по медиа"""
    res_dict = {}
    res_dict['img'] = dic['image']['large']
    media_list = []
    for i in dic['media']['nodes']:
        if i['title']['english'] is not None:
            media_list.append(i['title']['english'])
        elif i['title']['romaji'] is not None:
            media_list.append(i['title']['romaji'])
        else:
            media_list.append(i['title']['native'])
    media_list = '\n'.join(media_list)
    res_dict['media_list'] = ', '.join(media_list)
    res_dict['url'] = dic['siteUrl']
    res_dict['id'] = dic['id']
    res_dict['caption']=f"Name:{dic['name']['full']}\n" \
                        f"Age:{dic['age']}\n" \
                        f"Media:\n{media_list}"
    return res_dict
