import logging
import asyncio
from aiogram import Router
from handlers import anime_search, char_search, photo_search, collections, start_page
from aiogram import Bot, Dispatcher

logging.basicConfig(level=logging.DEBUG)

API_TOKEN = '5686188962:AAHNDY8zrhkkwk6_BVQvQba8cMQzFVnVoC4'
bot = Bot(token=API_TOKEN, parse_mode='HTML')


async def main():
    dp = Dispatcher()
    dp.include_router(char_search.router)
    dp.include_router(anime_search.router)
    dp.include_router(photo_search.router)
    dp.include_router(collections.router)
    dp.include_router(start_page.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
