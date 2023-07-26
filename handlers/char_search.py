"""модуль поиска персонажа по имени"""
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from API import api_char_request
from keyboards.searching_kb import make_search_char_keyboard
from filters.handler_filters import CharByNameCallbackData

router = Router()


class CharFields(StatesGroup):
    reg_name = State()
    media = State()


@router.message(Command(commands='char_search'))
async def char_search(message: Message, state: FSMContext):
    """запрос на ввод имени"""
    await message.delete()
    await message.answer(text="Enter characters name:")
    await state.set_state(CharFields.reg_name)


@router.message(CharFields.reg_name)
async def reg_char_name(message: Message):
    """регистрация введного имени"""
    search_dict = {"search": message.text, "page": 1}
    response = api_char_request.char_request(search_dict)
    await message.answer_photo(photo=response['img'],
                               caption=response['caption'],
                               reply_markup=make_search_char_keyboard(
                                   name=message.text,
                                   page=2,
                                   link=response['url']))


@router.callback_query(CharByNameCallbackData.filter())
async def iter_char_list(callback: CallbackQuery,
                         callback_data: CharByNameCallbackData,
                         state: FSMContext):
    """итерация результатов поиска"""
    await callback.message.delete()
    search_dict = {"search": callback_data.name, 'page': callback_data.page}
    response = api_char_request.char_request(search_dict)
    await callback.message.answer_photo(photo=response['img'],
                                        caption=response['caption'],
                                        reply_markup=make_search_char_keyboard(
                                            callback_data.name,
                                            page=callback_data.page,
                                            link=response["url"]))
