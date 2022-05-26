# from PyQt5.QtWidgets import *
# from PyQt5.QtGui import *
# from PyQt5.QtCore import *
from mysql.connector import connect, Error
# import sys



if __name__ == '__main__':
    try:
        with connect(
            host = 'localhost',
            user = 'root',
            password = 'nikae29683',
            database = 'Phonebook'
        ) as connection:
            show_table_query = 'describe people'
            with connection.cursor() as cursor:
                cursor.execute(show_table_query)
                result = cursor.fetchall()
                for row in result:
                    print(row)
    except Error as e:
        print(e)