"""модуль регистрации нового юзера в БД"""
import psycopg2

conn = psycopg2.connect(dbname='anilist',
                        user='postgres',
                        password='pet_project',
                        host='localhost')
cursor = conn.cursor()

TEMP_ADD_USER = "INSERT INTO users(telegram_id, user_name) VALUES ({0},'{1}')"
TEMP_ADD_USER_COL = "INSERT INTO {0}(telegram_id) VALUES ({1})"


def add_user(id_user, name):
    """функция добавления нового юзера в базу данных"""
    cursor.execute(TEMP_ADD_USER.format(id_user, name))
    cursor.execute(TEMP_ADD_USER_COL.format('favorite', id_user))
    cursor.execute(TEMP_ADD_USER_COL.format('planned', id_user))
    cursor.execute(TEMP_ADD_USER_COL.format('in_process', id_user))
    cursor.execute(TEMP_ADD_USER_COL.format('finished', id_user))
    conn.commit()
    cursor.close()
