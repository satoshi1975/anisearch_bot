"""модуль с классами коллбеков"""
from typing import Optional
from aiogram.filters.callback_data import CallbackData


class GenreCallbackData(CallbackData, prefix='genre'):
    """класс обратного вызова жанров"""
    opt: str
    val: Optional[str]


class RankCallbackData(CallbackData, prefix='rank'):
    """класс обратного вызова рейтинга"""
    val: Optional[str]
    sort: Optional[str]
    search: Optional[str]


class TagCallbackData(CallbackData, prefix='tag'):
    """класс обратного вызова тэгов"""
    val: Optional[str]
    page_f: Optional[int]
    page_l: Optional[int]
    save: Optional[bool]


class MediaCallbackData(CallbackData, prefix='media'):
    """класс обратного вызова медиа"""
    page: Optional[int]


class CharByMediaCallbackData(CallbackData, prefix='charByMedia'):
    """класс обратного вызова персонажей по медиа"""
    page_char: Optional[int]
    id_media: Optional[int]


class CharByNameCallbackData(CallbackData, prefix='CharByName'):
    """класс обратного вызова персонажей по имении"""
    name: Optional[str]
    page: Optional[int]


class IterSearchByPhotoResult(CallbackData, prefix='photo_s'):
    """класс итерации медиа по загрузке изображения"""
    page: Optional[int]
    id_media: Optional[int]
    type_coll: Optional[str]
    user_id: Optional[int]


class MediaCollection(CallbackData, prefix='col_media'):
    """класс обратного вызова коллекции медия"""
    id_user: Optional[int]
    id: Optional[int]
    col_type: Optional[str]
    type: Optional[str]
    page: Optional[str]


class CharCollection(CallbackData, prefix='col_char'):
    """класс обратного вызова коллекции персонажей"""
    id_user: Optional[int]
    id: Optional[int]


class ListOfCollections(CallbackData, prefix='choose_coll_anime'):
    """класс обратного вызова при выборе коллекции"""
    id_user: Optional[int]
    type_coll: Optional[str]
    type_media: Optional[str]


class IterObjectsInCol(CallbackData, prefix='list_of_obj'):
    """класс итерации объектов коллекции"""
    count: Optional[int]
    id_user: Optional[int]
    type_coll: Optional[str]
    type_media: Optional[str]
    is_drop: Optional[bool]
    id_obj: Optional[int]
