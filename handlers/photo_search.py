"""модуль поиска аниме по изображению"""
from aiogram import Router, F
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command

from aiogram.types import Message, CallbackQuery
from keyboards.searching_kb import make_photo_search_keyboard, make_iter_search_by_photo
from API.api_requests import show_media
from Photo_api import url_searching, uploads_photo
from filters.templates import templates_media
from filters.handler_filters import IterSearchByPhotoResult
from database import db_reg

path = '/home/seksualka/PycharmProjects/pythonProject_ai/images_for_searching/'

router = Router()


class PhotoSearching(StatesGroup):
    choose_option = State()
    get_photo = State()
    get_url = State()


@router.message(Command(commands=['photo_search']))
async def req_photo(message: Message, state: FSMContext):
    """выбор между ссылкой на изображение или загрузкой из галереи"""
    await message.delete()
    await message.answer(text="Choose search option:",
                         reply_markup=make_photo_search_keyboard())

    await state.set_state(PhotoSearching.choose_option)


@router.message(PhotoSearching.choose_option, F.text == 'upload photo')
async def get_photo(message: Message, state: FSMContext):
    """запрос загрузки изображения"""
    await state.clear()
    await message.answer(text="upload your image:")
    await state.set_state(PhotoSearching.get_photo)


@router.message(PhotoSearching.get_photo)
async def get_p(message: Message, state: FSMContext):
    """регистрация загруженого изображения"""
    id_list = await uploads_photo.get_id_list(message.photo[0].file_id)
    await state.update_data(id_list=id_list)
    first_res = show_media({'id_media': id_list[0]}, page=1)
    await message.answer_photo(photo=first_res['img'],
                               caption=templates_media(first_res),
                               reply_markup=make_iter_search_by_photo(
                                   0,
                                   first_res['url'],
                                   col=None,
                                   user_id=message.from_user.id,
                                   media_id=id_list[0]))


@router.callback_query(IterSearchByPhotoResult.filter())
async def iter_res(callback: CallbackQuery,
                   callback_data: IterSearchByPhotoResult, state: FSMContext):
    """итерация результатов поиска"""
    if callback_data.type_coll is not None:
        db_reg.add([
            callback_data.type_coll, 'anime_type', 'anime_type',
            callback_data.id_media, callback.from_user.id
        ])
        await edit_kb(
            message=callback.message,
            page=callback_data.page,
            url=
            'https://yandex.ru/search/?clid=2353835&text=gthtdjlxbr&lr=11246',
            media_id=callback_data.id_media,
            user_id=callback.from_user.id,
            type_coll=callback_data.type_coll)
    else:
        id_media = await state.get_data()
        await callback.message.delete()
        res = show_media({'id_media': id_media['id_list'][callback_data.page]},
                         page=1)

        await callback.message.answer_photo(
            photo=res['img'],
            caption=templates_media(res),
            reply_markup=make_iter_search_by_photo(
                callback_data.page,
                res['url'],
                col=callback_data.type_coll,
                user_id=callback_data.user_id,
                media_id=callback_data.id_media))


async def edit_kb(message: Message, page, url, media_id, user_id, type_coll):
    """изменение клавиатуры после выбора коллекции"""
    await message.edit_reply_markup(reply_markup=make_iter_search_by_photo(
        page=page, url=url, col=type_coll, user_id=user_id, media_id=media_id))


##############################################################################################
@router.message(PhotoSearching.choose_option, F.text == 'by url')
async def get_photo(message: Message, state: FSMContext):
    """запрос ссылки на изображение"""
    await state.clear()
    await message.delete()
    await message.answer(text="enter url:")
    await state.set_state(PhotoSearching.get_url)


@router.message(PhotoSearching.get_url)
async def reg_url(message: Message, state: FSMContext):
    """регистрация ссылки и вывод результата"""
    await message.delete()
    id_list = url_searching.url_request(message.text)
    await state.update_data(id_list=id_list)
    first_res = show_media({'id_media': id_list[0]}, page=1)
    await message.answer_photo(photo=first_res['img'],
                               caption=templates_media(first_res),
                               reply_markup=make_iter_search_by_photo(
                                   0,
                                   first_res['url'],
                                   col=None,
                                   user_id=message.from_user.id,
                                   media_id=id_list[0]))


# def download_file(file: types.File):
#     file_path = file.file_path
#     destination = r"C:\folder\file.txt"
#     destination_file = bot.bot.download_file(file_path, destination)
