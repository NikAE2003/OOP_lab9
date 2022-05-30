from sqlite3 import connect, Error

def readQuery(query = 'SELECT * FROM student;'):
    try:
        #ПОДКЛЮЧЕНИЕ К БАЗЕ ДАННЫХ
        with connect(r'db/mydb.db') as connection:
            #ОБРАБОТКА ЗАПРОСА
            cursor = connection.cursor()

            cursor.execute(query)
            return cursor.fetchall()   

    except Error as e:
        print(e)


def writeQuery(query):
    try:
        #ПОДКЛЮЧЕНИЕ К БАЗЕ ДАННЫХ
        with connect(r'db/mydb.db') as connection:
            #ОБРАБОТКА ЗАПРОСА
            cursor = connection.cursor()
            
            cursor.execute(query)
            connection.commit()

    except Error as e:
        print(e)
