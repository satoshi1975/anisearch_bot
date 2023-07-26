"""запрос к БД на регистрацию объекта"""
import psycopg2

conn = psycopg2.connect(dbname='anilist',
                        user='postgres',
                        password='pet_project',
                        host='localhost')
cursor = conn.cursor()

TEMP_ADD = "UPDATE {0} SET {1} = array_append({2},{3}) where telegram_id={4}"
TEMP_REM = "UPDATE {0} SET {1} = array_remove({2},{3}) where telegram_id={4}"


def add(arr_data):
    """функция запроса на добавление в БД"""
    cursor.execute(TEMP_REM.format(*arr_data))
    cursor.execute(TEMP_ADD.format(*arr_data))
    conn.commit()


# def rem(arr_data):
#     cursor.execute(TEMP_REM, arr_data)
#     conn.commit()
#     cursor.close()
