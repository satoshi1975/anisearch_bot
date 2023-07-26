from typing import Optional

from aiogram.utils.keyboard import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardBuilder, InlineKeyboardButton
from filters.handler_filters import GenreCallbackData,RankCallbackData,TagCallbackData,MediaCallbackData,\
    CharByMediaCallbackData,CharByNameCallbackData,IterSearchByPhotoResult,MediaCollection,CharCollection,\
    ListOfCollections,IterObjectsInCol
from keyboards.lists import media_genre, tag_list


def make_row_keyboard(items: list[str]) -> ReplyKeyboardMarkup:

    row = [KeyboardButton(text=item) for item in items]
    return ReplyKeyboardMarkup(keyboard=[row], resize_keyboard=True)


def make_inline_keyboard(items: list[str], pref, size):
    row = [
        InlineKeyboardButton(text=item, callback_data=f'{pref}' + f'{item}')
        for item in items
    ]
    builder = InlineKeyboardBuilder()

    for i in row:
        builder.add(i)
    print(builder.as_markup())
    return builder.adjust(size).as_markup()


def make_genre_keyboard(del_g: list[str]):

    builder = InlineKeyboardBuilder()
    for i in media_genre:
        if i in del_g:
            builder.button(text=i + '\U00002714',
                           callback_data=GenreCallbackData(opt='rem', val=i))
        else:
            builder.button(text=i,
                           callback_data=GenreCallbackData(opt='add', val=i))

    builder.button(text='save choice',
                   callback_data=GenreCallbackData(opt='save'))

    return builder.adjust(2).as_markup()


def make_rank_keyboard(items: list[int], choose: Optional[bool]):
    builder = InlineKeyboardBuilder()
    if choose == 'search?':
        builder.button(text='searching', callback_data='searching')

    elif choose is not None:
        builder.button(text='by min',
                       callback_data=RankCallbackData(sort='SCORE'))
        builder.button(text='by max',
                       callback_data=RankCallbackData(sort='SCORE_DESC'))
    elif choose is None:
        for i in items:
            builder.button(text=f'{i}', callback_data=RankCallbackData(val=i))

    return builder.adjust(2).as_markup()


def make_tags_keyboard(page_f, page_l, choice, tags_list):
    # print(tags_list)
    iter_list = tag_list[page_f:page_l]
    builder = InlineKeyboardBuilder()
    for i in iter_list:
        if i in tags_list:
            builder.button(text=f'\U00002714{i}',
                           callback_data=TagCallbackData(val=i,
                                                         page_f=page_f,
                                                         page_l=page_l))

        else:
            builder.button(text=i,
                           callback_data=TagCallbackData(val=i,
                                                         page_f=page_f,
                                                         page_l=page_l))
    # if status==None:
    #     builder.button(text='<--',callback_data=TagCallbackData(page_f=page_f-8,page_l=page_l-8))
    #     builder.button(text='-->',callback_data=TagCallbackData(page_f=page_f+8,page_l=page_l+8))
    # else:
    builder.button(text='<--',
                   callback_data=TagCallbackData(page_f=page_f - 8,
                                                 page_l=page_l - 8))
    builder.button(text='-->',
                   callback_data=TagCallbackData(page_f=page_f + 8,
                                                 page_l=page_l + 8))
    builder.button(text='save', callback_data=TagCallbackData(save=True))
    return builder.adjust(2).as_markup()


def make_media_keyboard(page, url, id, user_id, media_type, col):
    page = int(page)
    list_of_collections = {
        "favorite": f"\U00002B50",
        "planned": f"I'll see",
        "in_process": f"in the process",
        "finished": f"Viewed"
    }
    if col is not None: list_of_collections[f'{col}'] += f'\U00002714'

    builder = InlineKeyboardBuilder()
    builder.button(text='site', url=url)
    builder.button(text='characters',
                   callback_data=CharByMediaCallbackData(page_char=1,
                                                         id_media=id))
    print(type(page))
    if page != 0:
        builder.button(text='<--',
                       callback_data=MediaCallbackData(page=page - 1))
    builder.button(text='-->', callback_data=MediaCallbackData(page=page + 1))
    builder.button(text=list_of_collections['favorite'],
                   callback_data=MediaCollection(id=id,
                                                 id_user=user_id,
                                                 col_type='favorite',
                                                 type=media_type,
                                                 page=page))
    builder.button(text=list_of_collections['planned'],
                   callback_data=MediaCollection(id=id,
                                                 id_user=user_id,
                                                 col_type='planned',
                                                 type=media_type,
                                                 page=page))
    builder.button(text=list_of_collections['in_process'],
                   callback_data=MediaCollection(id=id,
                                                 id_user=user_id,
                                                 col_type='in_process',
                                                 type=media_type,
                                                 page=page))
    builder.button(text=list_of_collections['finished'],
                   callback_data=MediaCollection(id=id,
                                                 id_user=user_id,
                                                 col_type='finished',
                                                 type=media_type,
                                                 page=page))
    # builder.button(text=f"\U00002B50", callback_data=MediaCollection(id=id,id_user=user_id,col_type='favorite',type=media_type,
    #                                                                 page=page))
    # builder.button(text=f"I'll see", callback_data=MediaCollection(id=id,id_user=user_id,col_type='planned',type=media_type,
    #                                                               page=page))
    # builder.button(text=f"in the process", callback_data=MediaCollection(id=id,id_user=user_id,col_type='in_process',type=media_type,
    #                                                                     page=page))
    # builder.button(text=f"Viewed", callback_data=MediaCollection(id=id,id_user=user_id,col_type='finished',type=media_type,
    #                                                             page=page))

    return builder.adjust(2).as_markup()


def make_char_by_media_keyboard(page, url, id_media, user_id, char_id):
    builder = InlineKeyboardBuilder()
    builder.button(text="site", url=url)
    builder.button(text='description', callback_data='af')
    if page != 0:
        builder.button(text='<--',
                       callback_data=CharByMediaCallbackData(
                           page_char=page - 1, id_media=id_media))
    builder.button(text='-->',
                   callback_data=CharByMediaCallbackData(page_char=page + 1,
                                                         id_media=id_media))
    builder.button(text="\U00002B50",
                   callback_data=MediaCollection(id=char_id,
                                                 id_user=user_id,
                                                 col_type='favorite',
                                                 type='char_type',
                                                 page=page))

    return builder.adjust(2).as_markup()


def make_search_char_keyboard(name, page, link):
    builder = InlineKeyboardBuilder()
    builder.button(text='link', url=link)
    builder.button(text='description', callback_data='search')
    if page != 0:
        builder.button(text='<--',
                       callback_data=CharByNameCallbackData(name=name,
                                                            page=page - 1))
    builder.button(text='-->',
                   callback_data=CharByNameCallbackData(name=name,
                                                        page=page + 1))
    return builder.adjust(2).as_markup()


def make_photo_search_keyboard():
    markup_list = [
        KeyboardButton(text='by url'),
        KeyboardButton(text='upload photo')
    ]
    return ReplyKeyboardMarkup(keyboard=[markup_list], resize_keyboard=True)


def make_iter_search_by_photo(page, url, col, user_id, media_id):
    list_of_collections = {
        "favorite": f"\U00002B50",
        "planned": f"I'll see",
        "in_process": f"in the process",
        "finished": f"Viewed"
    }
    if col is not None: list_of_collections[f'{col}'] += f'\U00002714'
    builder = InlineKeyboardBuilder()
    builder.button(text="link", url=url)
    builder.button(text="description", url=url)
    if page != 0:
        builder.button(text="<--",
                       callback_data=IterSearchByPhotoResult(page=page - 1,
                                                             id_media=media_id,
                                                             type_coll=None,
                                                             user_id=user_id))
    builder.button(text="-->",
                   callback_data=IterSearchByPhotoResult(page=page + 1,
                                                         id_media=media_id,
                                                         type_coll=None,
                                                         user_id=user_id))
    builder.button(text=list_of_collections['favorite'],
                   callback_data=IterSearchByPhotoResult(page=page,
                                                         id_media=media_id,
                                                         type_coll='favorite',
                                                         user_id=user_id))
    builder.button(text=list_of_collections['planned'],
                   callback_data=IterSearchByPhotoResult(page=page,
                                                         id_media=media_id,
                                                         type_coll='planned',
                                                         user_id=user_id))
    builder.button(text=list_of_collections['in_process'],
                   callback_data=IterSearchByPhotoResult(
                       page=page,
                       id_media=media_id,
                       type_coll='in_process',
                       user_id=user_id))
    builder.button(text=list_of_collections['finished'],
                   callback_data=IterSearchByPhotoResult(page=page,
                                                         id_media=media_id,
                                                         type_coll='finished',
                                                         user_id=user_id))
    # builder.button(text=list_of_collections['favorite'],
    #                callback_data=MediaCollection(id=id, id_user=user_id, col_type='favorite', type="anime_type",
    #                                              page=page))
    # builder.button(text=list_of_collections['planned'],
    #                callback_data=MediaCollection(id=id, id_user=user_id, col_type='planned', type="anime_type",
    #                                              page=page))
    # builder.button(text=list_of_collections['in_process'],
    #                callback_data=MediaCollection(id=id, id_user=user_id, col_type='in_process', type='anime_type',
    #                                              page=page))
    # builder.button(text=list_of_collections['finished'],
    #                callback_data=MediaCollection(id=id, id_user=user_id, col_type='finished', type='media_type',
    #                                              page=page))
    return builder.adjust(2).as_markup()


def make_list_of_collections(id_user, type):
    builder = InlineKeyboardBuilder()
    builder.button(text='favorite',
                   callback_data=ListOfCollections(id_user=id_user,
                                                   type_coll='favorite',
                                                   type_media=type))

    builder.button(text='in planned',
                   callback_data=ListOfCollections(id_user=id_user,
                                                   type_coll='planned',
                                                   type_media=type))

    builder.button(text='in process',
                   callback_data=ListOfCollections(id_user=id_user,
                                                   type_coll='in_process',
                                                   type_media=type))

    builder.button(text='finished',
                   callback_data=ListOfCollections(id_user=id_user,
                                                   type_coll='finished',
                                                   type_media=type))
    return builder.adjust(2).as_markup()


def iter_objects_in_col(page, id_media, url, id_user, type_coll, type_media,
                        id_obj):
    builder = InlineKeyboardBuilder()

    builder.button(text='site', url=url)
    builder.button(text='characters',
                   callback_data=CharByMediaCallbackData(page_char=0,
                                                         id_media=id_media))
    if page != 0:
        builder.button(text='<--',
                       callback_data=IterObjectsInCol(count=page - 1,
                                                      id_user=id_user,
                                                      is_drop=False,
                                                      type_coll=type_coll,
                                                      type_media=type_media,
                                                      id_obj=id_obj))
    builder.button(text='-->',
                   callback_data=IterObjectsInCol(count=page + 1,
                                                  id_user=id_user,
                                                  is_drop=False,
                                                  type_coll=type_coll,
                                                  type_media=type_media,
                                                  id_obj=id_obj))
    builder.button(text='drop',
                   callback_data=IterObjectsInCol(count=page + 1,
                                                  id_user=id_user,
                                                  type_coll=type_coll,
                                                  type_media=type_media,
                                                  is_drop=True,
                                                  id_obj=id_obj))
    # builder.button(text="drop from collection")
    return builder.adjust(2).as_markup()


# def make_list_of_collections_manga(id_user):
#     builder = InlineKeyboardBuilder()
#     builder.button(text='favorite', callback_data=ListOfCollections(id_user=id_user, type_call='favorite',
#                                                                     type_media="manga_type"))
#
#     builder.button(text='in planned', callback_data=ListOfCollections(id_user=id_user, type_call='planned'))
#
#     builder.button(text='in process',callback_data=ListOfCollections(id_user=id_user, type_call='in_process'))
#
#     builder.button(text='finished', callback_data=ListOfCollections(id_user=id_user, type_call='finished'))
#     return builder.adjust(2).as_markup()
