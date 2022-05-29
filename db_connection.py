from mysql.connector import connect, Error

def readQuery(query = 'SELECT * FROM student'):
    try:
        #ПОДКЛЮЧЕНИЕ К БАЗЕ ДАННЫХ
        with connect(
            host = 'localhost',
            user = 'root',
            passwd = '1234',
            database = 'test_db'
        ) as connection:
            #ОБРАБОТКА ЗАПРОСА
            results = []
            with connection.cursor() as cursor:
                cursor.execute(query)
                for c in cursor:
                    results.append(c)
            return results

    except Error as e:
        print(e)


def writeQuery(query):
    try:
        #ПОДКЛЮЧЕНИЕ К БАЗЕ ДАННЫХ
        with connect(
            host = 'localhost',
            user = 'root',
            passwd = '1234',
            database = 'test_db'
        ) as connection:
            #ОБРАБОТКА ЗАПРОСА
            with connection.cursor() as cursor:
                cursor.execute(query)
                connection.commit()

    except Error as e:
        print(e)
