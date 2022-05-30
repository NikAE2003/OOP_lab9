from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from input_form import InputForm

from db_connection import *


class TableItem(QWidget):
    def __init__(self, parent, id, name = '', age = 0):
        super().__init__(parent)

        self._id = id
        self._name = name
        self._age = age
        self._selected = False

        self.setMinimumHeight(30)
        self.setStyleSheet('background-color: #333; border-radius: 8px')

        self.inputForm = InputForm(self)

        self.widget = QWidget(self)
        self.widget.resize(100, 30)
        self.layout = QHBoxLayout(self.widget)
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.setSpacing(2)


        self.id_label = QLabel(self)
        self.id_label.setText(str(self._id))
        self.id_label.setAlignment(Qt.AlignLeft)
        self.id_label.setFixedWidth(30)

        self.name_label = QLabel(self)
        self.name_label.setText(str(self._name))
        self.name_label.setAlignment(Qt.AlignLeft)
        self.setMinimumWidth(300)

        self.age_label = QLabel(self)
        self.age_label.setText(str(self._age))
        self.age_label.setAlignment(Qt.AlignLeft)
        self.age_label.setFixedWidth(50)

        self.layout.addWidget(self.id_label)
        self.layout.addWidget(self.name_label)
        self.layout.addWidget(self.age_label)

    def resizeEvent(self, e):
        size = e.size()
        self.widget.resize(size.width(), 30)

    def mousePressEvent(self, e):
        self._selected = not self._selected
        self.setStyleSheet('background-color: #56c' if self._selected else 'background-color: #333')

    def mouseDoubleClickEvent(self, e):
        self.inputForm.show()
        self.inputForm.name_lineEdit.setText(self._name)
        self.inputForm.age_spinBox.setValue(self._age)

class Table(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self._rows_list = []
        self._rows_count = 0

        self.setMinimumHeight(30)
        self.setStyleSheet('background-color: #222')

        self.headder_widget = QWidget(self)
        self.headder_widget.resize(100, 30)
        self.headder_layout = QHBoxLayout(self.headder_widget)
        self.headder_layout.setContentsMargins(2,2,2,2)
        self.headder_layout.setSpacing(2)


        self.id_label = QLabel(self.headder_widget)
        self.id_label.setText('ID')
        self.id_label.setAlignment(Qt.AlignLeft)
        self.id_label.setFixedWidth(30)

        self.name_label = QLabel(self.headder_widget)
        self.name_label.setText('ИМЯ')
        self.name_label.setAlignment(Qt.AlignLeft)
        self.setMinimumWidth(300)

        self.age_label = QLabel(self.headder_widget)
        self.age_label.setText('ВОЗРАСТ')
        self.age_label.setAlignment(Qt.AlignLeft)
        self.age_label.setFixedWidth(50)

        self.headder_layout.addWidget(self.id_label)
        self.headder_layout.addWidget(self.name_label)
        self.headder_layout.addWidget(self.age_label)

        self.table_widget = QWidget(self)
        self.table_widget.setGeometry(0, 30, 100, self.size().height() - 30)
        self.table_layout = QVBoxLayout(self.table_widget)
        self.table_layout.setContentsMargins(2,0,2,2)
        self.table_layout.setSpacing(2)
        self.table_layout.setAlignment(Qt.AlignTop)

        self.fillTable()

    def fillTable(self):
        self._rows_list = []
        self._rows_count = 0
        data = readQuery()
        for row in data:
            id, name, age = row
            self.addRow(id, name, age)

    def selectedRows(self):
        rows = []
        for row in self._rows_list:
            if row._selected:
                rows.append(row._id)
        return rows

    def addRow(self, id, name, age):
        self._rows_list.append(TableItem(self, id, name, age))
        self._rows_count += 1
        self.table_layout.addWidget(self._rows_list[self._rows_count - 1],0, Qt.AlignTop)
        self.setMinimumHeight(30 * (self._rows_count + 1))

    def resizeEvent(self, e):
        size = e.size()
        self.headder_widget.resize(size.width(), 30)
        self.table_widget.resize(size.width(), size.height() - 30)
    