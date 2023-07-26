import bot
from Photo_api import file_searching

PATH = '/home/seksualka/PycharmProjects/pythonProject_ai/images_for_searching/'


async def get_id_list(file_id):

    path_res = PATH + file_id + '.jpg'
    file_info = await bot.bot.get_file(file_id)
    file_path = file_info.file_path
    await bot.bot.download_file(file_path, path_res)
    return file_searching.get_file_name(path_res)
