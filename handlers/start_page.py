"""модуль регистрации нового юзера"""
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from keyboards import lists
from database import reg_user
# from aiogram.fsm.context import FSMContext
# from database import db_request
# from filters import templates
# from aiogram.fsm.state import StatesGroup, State
# from API import api_char_request, api_requests
# from keyboards.searching_kb import make_list_of_collections, iter_objects_in_col
# from filters.handler_filters import ListOfCollections, IterObjectsInCol
# from aiogram.types import CallbackQuery

router = Router()


@router.message(Command(commands='start'))
async def start_new_user(message: Message):
    """вывод приветственного сообщения и регистрации в БД"""
    try:
        reg_user.add_user(message.from_user.id, message.from_user.username)
    except:
        pass
    if type(message.from_user.first_name) == str and type(
            message.from_user.last_name) == str:
        name = message.from_user.first_name + " " + message.from_user.last_name
    else:
        name = 'friend'
    await message.answer(
        f'Hello, {name} \n Use /help to find out more about my abilities')


@router.message(Command(commands='help'))
async def help(message: Message):
    """вывод подсказки"""
    await message.answer(text=lists.preview_text)
