from sqlite3 import connect, Error

def readQuery(tableName: str = '', fieldsNames: str = '', input_query = ''):
    try:
        #ПОДКЛЮЧЕНИЕ К БАЗЕ ДАННЫХ
        with connect(r'db/database.db') as connection:
            #ОБРАБОТКА ЗАПРОСА
            cursor = connection.cursor()

            if input_query == '':
                query = 'SELECT '
                for name in fieldsNames.split(', '):
                    if query != 'SELECT ':
                        query += ', '
                    query += f'"{name}"'
                query += f' FROM "{tableName}";'

                cursor.execute(query)
                query_result = cursor.fetchall()

                result = []
                for row in query_result:
                    result_row = {}
                    for i in range(len(fieldsNames.split(', '))):
                        result_row[fieldsNames.split(', ')[i]] = row[i]
                    result.append(result_row)

            else:
                query = input_query
                cursor.execute(query)
                result = cursor.fetchall()

            return result

    except Error as e:
        print(e)


def writeQuery(query):
    try:
        #ПОДКЛЮЧЕНИЕ К БАЗЕ ДАННЫХ
        with connect(r'db/database.db') as connection:
            #ОБРАБОТКА ЗАПРОСА
            cursor = connection.cursor()
            
            cursor.execute(query)
            connection.commit()

    except Error as e:
        print(e)
