"""модуль запросов к коллекциям"""
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from database import db_request
from filters import templates
from aiogram.fsm.state import StatesGroup, State
from API import api_char_request, api_requests
from keyboards.searching_kb import make_list_of_collections, iter_objects_in_col
from filters.handler_filters import ListOfCollections, IterObjectsInCol
from aiogram.types import CallbackQuery
from database import db_del

router = Router()


@router.message(Command(commands='collections_anime'))
async def choose_coll_anime(message: Message, state: FSMContext):
    """выбор коллекии аниме"""
    await message.delete()
    await message.answer(text="choose collection of anime:",
                         reply_markup=make_list_of_collections(
                             message.from_user.id, type="anime_type"))


@router.message(Command(commands='collections_manga'))
async def choose_coll_manga(message: Message, state: FSMContext):
    """выбор коллекии аниме"""
    await message.delete()
    await message.answer(text="choose collection of manga:",
                         reply_markup=make_list_of_collections(
                             message.from_user.id, type="manga_type"))


@router.message(Command(commands='favourite_characters'))
async def list_of_favourite_char(message: Message, state: FSMContext):
    """список любимых персонажей"""

    media_id = db_request.col_request('char_type', 'favorite',
                                      message.from_user.id)
    res = api_char_request.char_request({'id': media_id[0]})
    await message.answer_photo(photo=res['img'],
                               caption=res['caption'],
                               reply_markup=iter_objects_in_col(
                                   page=0,
                                   id_media=media_id[1],
                                   url=res['url'],
                                   type_coll='favorite',
                                   type_media='char_type',
                                   id_user=message.from_user.id,
                                   id_obj=res['id']))
    # await message.answer(text="choose collection of anime:",reply_markup=make_list_of_collections(message.from_user.id,
    #                                                                                            type="char_type"))


####################################################################################################
@router.callback_query(ListOfCollections.filter())
async def iter_col(callback: CallbackQuery, callback_data: ListOfCollections):
    """вывод результатов поиска по коллекции"""
    media_id = db_request.col_request(callback_data.type_media,
                                      callback_data.type_coll,
                                      callback.from_user.id)
    # if callback_data.type_media=='char_type':
    #     print(api_char_request.char_request({'id':media_id[0]}))
    #     res=api_char_request.char_request({'id':media_id[0]})
    #     await callback.message.answer_photo(photo=res['img'],caption=res['caption'],
    #                                         reply_markup=iter_objects_in_col(page=0, id_media=media_id[1],
    #                                                                          url=res['url'],
    #                                                                          type_coll=callback_data.type_coll,
    #                                                                          type_media=callback_data.type_media,
    #                                                                          id_user=callback.from_user.id,
    #                                                                          id_obj=res['id']))
    #
    # else:
    res = api_requests.show_media({'id_media': media_id[0]}, 1)

    await callback.message.answer_photo(
        photo=res['img'],
        caption=templates.templates_media(res),
        reply_markup=iter_objects_in_col(page=0,
                                         id_media=media_id[0],
                                         url=res['url'],
                                         type_coll=callback_data.type_coll,
                                         type_media=callback_data.type_media,
                                         id_user=callback.from_user.id,
                                         id_obj=res['id']))
    await callback.message.delete()


@router.callback_query(IterObjectsInCol.filter())
async def iter_obj_col(callback: CallbackQuery,
                       callback_data: IterObjectsInCol):
    """итерация объектов коллекции"""
    await callback.message.delete()

    if callback_data.is_drop is True:
        db_del.rem([
            callback_data.type_coll, callback_data.type_media,
            callback_data.type_media, callback_data.id_obj,
            callback_data.id_user
        ])

    media_id = db_request.col_request(callback_data.type_media,
                                      callback_data.type_coll,
                                      callback_data.id_user)

    if callback_data.type_media == 'char_type':
        try:
            res = api_char_request.char_request(
                {'id': media_id[callback_data.count]})

            await callback.message.answer_photo(
                photo=res['img'],
                caption=res['caption'],
                reply_markup=iter_objects_in_col(
                    page=callback_data.count,
                    id_media=media_id[1],
                    url=res['url'],
                    type_coll=callback_data.type_coll,
                    type_media=callback_data.type_media,
                    id_user=callback.from_user.id,
                    id_obj=res['id']))
        except:
            res = api_char_request.char_request(
                {'id': media_id[callback_data.count - 1]})

            await callback.message.answer_photo(
                photo=res['img'],
                caption=res['caption'],
                reply_markup=iter_objects_in_col(
                    page=callback_data.count - 1,
                    id_media=media_id[0],
                    url=res['url'],
                    type_coll=callback_data.type_coll,
                    type_media=callback_data.type_media,
                    id_user=callback.from_user.id,
                    id_obj=res['id']))

    else:
        try:
            res = api_requests.show_media(
                {'id_media': media_id[callback_data.count]}, 1)
            await callback.message.answer_photo(
                photo=res['img'],
                caption=templates.templates_media(res),
                reply_markup=iter_objects_in_col(
                    page=callback_data.count,
                    id_media=media_id[1],
                    url=res['url'],
                    type_coll=callback_data.type_coll,
                    type_media=callback_data.type_media,
                    id_user=callback.from_user.id,
                    id_obj=res['id']))
        except:
            res = api_requests.show_media(
                {'id_media': media_id[callback_data.count - 1]}, 1)
            await callback.message.answer_photo(
                photo=res['img'],
                caption=templates.templates_media(res),
                reply_markup=iter_objects_in_col(
                    page=callback_data.count - 1,
                    id_media=media_id[0],
                    url=res['url'],
                    type_coll=callback_data.type_coll,
                    type_media=callback_data.type_media,
                    id_user=callback.from_user.id,
                    id_obj=res['id']))
