from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from db_connection import *

class Table(QTableWidget):
    def __init__(self, tableName:str, columnsNames:str, columnsWidths:list, parent = None):
        super().__init__(parent = parent)

        self._name = tableName
        self._columns_names = columnsNames
        self._row_count = 0
        self._names_list = columnsNames.split(', ')
        
        self.verticalHeader().setVisible(False)

        self._columns = []
        for i in range(len(self._names_list)):
            self._columns.append((self._names_list[i], columnsWidths[i] if columnsWidths != [] else 0))

        self.setColumnCount(len(self._names_list))
        for i in range(len(self._names_list)):
            name, width = self._columns[i]
            if width == 0:
                self.horizontalHeader().setSectionResizeMode(i, QHeaderView.Stretch)
            else:
                self.setColumnWidth(i, width)

        self.setHorizontalHeaderLabels(self._names_list)

        self.fillTable()
        
        self.cellClicked.connect(self.select)

    def select(self, row):
        self.selectRow(row)

    def fillTable(self):
        self._row_count = 0
        self.setRowCount(0)
        data = readQuery(self._name, self._columns_names)

        for row in data:
            self._row_count += 1
            self.setRowCount(self._row_count)
            for i in range(len(self._names_list)):
                self.setItem(self._row_count-1, i, QTableWidgetItem(str(row[self._names_list[i]])))

    def changeData(self, row):
        query = f'UPDATE {self._name} SET'
        for i in range(len(self._names_list)):
            name = self._names_list[i]
            data = self.item(row, i).text()
            if name == 'id':
                where = f' WHERE id = {self.item(row, i).text()};'
            else: 
                if query != f'UPDATE {self._name} SET':
                    query += ', ' 
                query += f'{name} = {data}'
            query += where
        print(query)
        writeQuery(query)