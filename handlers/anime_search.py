"""Модуль поиска медиа"""
from aiogram import Router, F
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram.types import Message
from keyboards import lists
from aiogram.types import CallbackQuery
from filters import handler_filters
from API import api_requests
from filters.templates import templates_media
from database import db_reg

from keyboards.searching_kb import make_row_keyboard,\
    make_genre_keyboard,make_rank_keyboard,make_tags_keyboard,\
    make_media_keyboard,make_char_by_media_keyboard

router = Router()


class MediaFields(StatesGroup):
    type_media = State()
    choose_search_options = State()
    choosing_media_name = State()
    choosing_media_rank = State()
    choosing_media_genre = State()
    choosing_media_tags = State()


##############################################################################
@router.message(Command(commands=['anime_search']))
async def choose_type_a(message: Message, state: FSMContext):
    """регистрация типа аниме"""
    await state.clear()
    await message.delete()
    await message.answer(text='choose search options:',
                         reply_markup=make_row_keyboard(
                             lists.media_search_options))
    await state.set_state(MediaFields.choose_search_options)
    await state.update_data(type='ANIME')


###############################################################################
@router.message(Command(commands=['manga_search']))
async def choose_type_m(message: Message, state: FSMContext):
    """регистрация типа manga"""
    await state.clear()
    await message.delete()
    await message.answer(text='choose search options:',
                         reply_markup=make_row_keyboard(
                             lists.media_search_options))
    await state.set_state(MediaFields.choose_search_options)
    await state.update_data(type='MANGA')


###############################################################################
@router.message(MediaFields.choose_search_options, F.text == '\U0001F50E')
async def show_result(message: Message, state: FSMContext):
    """кнопка выдачи результатов"""
    await message.delete()
    res = api_requests.show_media(await state.get_data(), 1)
    print(await state.get_data())
    await message.answer_photo(photo=res['img'],
                               caption=templates_media(res),
                               reply_markup=make_media_keyboard(
                                   1,
                                   res['url'],
                                   res['id'],
                                   user_id=message.from_user.id,
                                   media_type=res['type'],
                                   col=None))
    # try:
    #     res=api_requests.show_media(await state.get_data(),1)
    #
    #     await message.answer_photo(photo=res['img'],caption=templates_media(res),
    #                                reply_markup=make_media_keyboard(1,res['url'],res['id'],user_id=message.from_user.id,
    #                                                                 media_type=res['type']))
    # except:
    #     await message.answer(text="No result. Try again")
    #     await state.clear()
    #     await state.set_state(MediaFields.choose_search_options)


##############################################


@router.callback_query(handler_filters.MediaCallbackData.filter())
async def iter_media(callback: CallbackQuery,
                     callback_data: handler_filters.MediaCallbackData,
                     state: FSMContext):
    """функция итерации медиа из результатов поиска"""
    await callback.message.delete()
    try:
        res = api_requests.show_media(await state.get_data(),
                                      callback_data.page)
    except:
        res = api_requests.show_media(await state.get_data(),
                                      callback_data.page - 1)
        callback_data.page -= 1
    await callback.message.answer_photo(photo=res['img'],
                                        caption=templates_media(res),
                                        reply_markup=make_media_keyboard(
                                            callback_data.page,
                                            res['url'],
                                            res['id'],
                                            callback.from_user.id,
                                            media_type=res['type'],
                                            col=None))


############################################################################
@router.callback_query(handler_filters.MediaCollection.filter())
async def collection_media(callback: CallbackQuery,
                           callback_data: handler_filters.MediaCollection,
                           state: FSMContext):
    """кнопка добавления в колекцию"""
    if callback_data.type == 'ANIME':
        type_m = 'anime_type'
    elif callback_data.type == "MANGA":
        type_m = 'manga_type'
    else:
        type_m = 'char_type'
    res = api_requests.show_media(await state.get_data(), callback_data.page)

    tup = [
        callback_data.col_type, type_m, type_m, callback_data.id,
        callback_data.id_user
    ]
    db_reg.add(tup)
    await edit_coll(message=callback.message,
                    page=callback_data.page,
                    url=res['url'],
                    id_media=res['id'],
                    user_id=callback.from_user.id,
                    media_type=res['type'],
                    col=callback_data.col_type)


    # await callback.message.answer_photo(photo=res['img'],caption=templates_media(res),
    #                                     reply_markup=make_media_keyboard(page=callback_data.page,url=res['url'],id=res['id']
    #                                                                      ,user_id=callback.from_user.id,
    #                                                                      media_type=res['type'],col=callback_data.col_type))
async def edit_coll(message: Message, page, url, id_media, user_id, media_type,
                    col):
    """функция изменения клавиатуры при выборе коллекции"""
    await message.edit_reply_markup(
        reply_markup=make_media_keyboard(page=page,
                                         url=url,
                                         id=id_media,
                                         user_id=user_id,
                                         media_type=media_type,
                                         col=col))
    # if data.col_type=='planned':
    #     db_reg.add(('planned', type, type, data.id, data.id_user))
    #     await callback.message.answer(text='Media has been added to the "I`ll be watching" collection')
    # elif data.col_type=='in_process':
    #     db_reg.add((data.col_type, type, type, data.id, data.id_user))
    #     await callback.message.answer(text='Media has been added to the "watch now" collection')
    # elif data.col_type=='finished':
    #     db_reg.add(('planned', type, type, data.id, data.id_user))
    #     await callback.message.answer(text='Media has been added to the "completed" collection')
    # else:
    #     db_reg.add(('planned', type, type, data.id, data.id_user))
    #     await callback.message.answer(text='Media has been added to the "favorite" collection')


#     await message.answer_photo(photo=res['img'],caption=templates_media(res),reply_markup=make_media_keyboard(1,res['url']))

#     await state.update_data(photo=res['img'])
# @router.callback_query(handler_filters.MediaCallbackData.filter())
# async def media_change(callback:CallbackQuery,callback_data:handler_filters.MediaCallbackData,state=FSMContext):
#
#     data=await state.get_data()
#     res = api_requests.test(data,callback_data.page)
#
#     await edit_media_res(message=callback.message,res=res,id=callback.message.message_id)
# async def edit_media_res(message:Message,res,id):
#     # res_p=await state.get_data()
#     message.edit
#
#     print(res["img"])
#     print(a)
#     await bot.edit_message_media(media=a,chat_id=message.chat.id,message_id=id)

########################################################################################################
#######################################################################################################

#############################################################################################################


@router.callback_query(handler_filters.CharByMediaCallbackData.filter())
async def show_char(callback: CallbackQuery,
                    callback_data: handler_filters.CharByMediaCallbackData):
    """кнопка списка персонажей медиа"""
    await callback.message.delete()
    search_res = api_requests.show_char(callback_data.id_media,
                                        callback_data.page_char)
    await callback.message.answer_photo(
        photo=search_res['image']['large'],
        caption=f'{search_res["name"]["full"]}\n'
        f'age:{search_res["age"]}',
        reply_markup=make_char_by_media_keyboard(
            callback_data.page_char,
            url=search_res['siteUrl'],
            id_media=callback_data.id_media,
            user_id=callback.from_user.id,
            char_id=search_res['id']))


# @router.callback_query(handler_filters.CharCollection.filter())
# async def collection_char(callback:CallbackQuery,callback_data:handler_filters.CharCollection,state:FSMContext):
#     await callback.message.delete()


########################################################################################################
@router.message(MediaFields.choose_search_options, F.text == 'name')
async def choose_media_name(message: Message, state: FSMContext):
    """ввод тайтла"""
    await message.delete()
    await message.answer(text=f'Please, enter title:')
    await state.set_state(MediaFields.choosing_media_name)


################################################
@router.message(MediaFields.choosing_media_name)
async def reg_media_name(message: Message, state: FSMContext):
    """функция регистрации введеного названия медиа"""
    await state.update_data(name_title=message.text)
    await state.set_state(MediaFields.choose_search_options)
    await state.get_data()


genres = {}


#########################################################################
@router.message(MediaFields.choose_search_options, F.text == 'genres')
async def choose_genre(message: Message):
    """запрос жанра"""
    genres[message.from_user.id] = []
    await message.answer(text="Choose genre",
                         reply_markup=make_genre_keyboard([]))


@router.callback_query(handler_filters.GenreCallbackData.filter())
async def genre_change(callback: CallbackQuery,
                       callback_data: handler_filters.GenreCallbackData,
                       state: FSMContext):
    """регистрация выборов жанра"""
    if callback_data.val is not None:
        if callback_data.opt == 'add':
            genres[callback.from_user.id] = genres.get(
                callback.from_user.id) + [callback_data.val]
        else:
            genres[callback.from_user.id].remove(callback_data.val)
        await edit_mes_genre(message=callback.message)
    else:
        await state.update_data(genres=genres[callback.from_user.id])
        res_dict = await state.get_data()
        await save_options(callback.message)


async def edit_mes_genre(message: Message):
    """функция изменения вида выбранных жанров"""
    await message.edit_text(text='choose',
                            reply_markup=make_genre_keyboard(
                                genres[message.chat.id]))


##############################################################################
@router.message(MediaFields.choose_search_options, F.text == ('tags'))
async def choose_tags(message: Message, state: FSMContext):
    """выбор тэгов"""
    await message.answer(text='enter the tags separated by commas:',
                         reply_markup=make_tags_keyboard(0, 8, None, [None]))
    await state.set_state(MediaFields.choosing_media_tags)
    await state.update_data(tags=[])


@router.callback_query(handler_filters.TagCallbackData.filter())
async def tag_change(callback: CallbackQuery,
                     callback_data: handler_filters.TagCallbackData,
                     state: FSMContext):
    """регистрая выбранных тэгов"""
    data = await state.get_data()
    if callback_data.save is True:
        await save_options(message=callback.message)
        await state.set_state(MediaFields.choose_search_options)
    else:
        if callback_data.val is not None:
            if callback_data.val in data['tags']:
                await state.update_data(data['tags'].remove(callback_data.val))
            else:
                await state.update_data(data['tags'].append(callback_data.val))
        choice = None
        if callback_data.val is not None:
            choice = callback_data.val

        await edit_tag_list(callback.message, callback_data.page_f,
                            callback_data.page_l, choice, data['tags'])


async def edit_tag_list(message: Message, p_f, p_l, choice, list_tags):
    """изменение вида выбранных тэгов"""
    await message.edit_text(text=f'list:{", ".join(list_tags)}',
                            reply_markup=make_tags_keyboard(
                                p_f, p_l, choice, list_tags))


#################################################################################
@router.message(MediaFields.choose_search_options, F.text == ('rank'))
async def get_rank(message: Message):
    """вывод списка рейтингов"""
    await message.answer(text='choose rank:',
                         reply_markup=make_rank_keyboard(
                             items=lists.media_rank, choose=None))


@router.callback_query(handler_filters.RankCallbackData.filter())
async def rank_change(callback: CallbackQuery,
                      callback_data: handler_filters.RankCallbackData,
                      state: FSMContext):
    """регистрация выбранного рейтинга и выбор типа сортировки"""
    if callback_data.val is not None:
        await state.update_data(rank=callback_data.val)
        await edit_mes_rank(callback.message, callback_data.val)
        # a = await state.get_data()
    else:
        await state.update_data(sort=callback_data.sort)
        res = await state.get_data()
        await save_options(callback.message)

    await state.set_state(MediaFields.choose_search_options)


async def edit_mes_rank(message: Message, choose):
    """сохранение параметров рейтинга"""
    if choose == 'search?':
        await message.edit_text(text=f'choose rank:{choose}',
                                reply_markup=make_rank_keyboard(
                                    lists.media_rank, choose))
    else:
        await message.edit_text(text=f'choose rank:{choose}',
                                reply_markup=make_rank_keyboard(
                                    lists.media_rank, choose))


##########################################################################


async def save_options(message: Message):
    """удаление сообщения после выбора"""
    await message.delete()
