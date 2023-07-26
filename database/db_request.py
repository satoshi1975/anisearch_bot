"""функция запрос к БД для вывода объектов"""
import psycopg2

conn = psycopg2.connect(dbname='anilist',
                        user='postgres',
                        password='pet_project',
                        host='localhost')
cursor = conn.cursor()

TEMP_REQ = "SELECT {0} from {1} WHERE telegram_id = {2}"


def col_request(type_media, type_collection, id_user):
    """функция запроса к БД"""
    cursor.execute(TEMP_REQ.format(*[type_media, type_collection, id_user]))

    res = cursor.fetchall()[0][0]
    return res
