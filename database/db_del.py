"""запрос к базе данных на удаление объектов"""
import psycopg2

conn = psycopg2.connect(dbname='anilist',
                        user='postgres',
                        password='pet_project',
                        host='localhost')
cursor = conn.cursor()

# temp_add= "UPDATE {0} SET {1} = array_append({2},{3}) where telegram_id={4}"
TEMP_REM = "UPDATE {0} SET {1} = array_remove({2},{3}) where telegram_id={4}"


def rem(arr_data):
    """функция удаления данных"""
    cursor.execute(TEMP_REM.format(*arr_data))
    # cursor.execute(temp_add.format(*arr_data))
    conn.commit()
