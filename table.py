from urllib.parse import non_hierarchical
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from db_connection import *

import styleSheets

class TableItem(QWidget):
    def __init__(self, parent, names, data, widths):
        super().__init__(parent)

        self._id = data['id']
        self._names = names
        self._selected = False

        # self.inputForm = InputForm(self)

        self.setStyleSheet(styleSheets.tableItem)

        self.mainLayout = QHBoxLayout(self)
        self.mainLayout.setContentsMargins(0,0,1,0)
        self.mainLayout.setSpacing(2)

        for i in range(len(self._names)):
            self.Item = QLabel(str(data[self._names[i]]), self)
            if len(widths) and widths[i]:
                self.Item.setFixedWidth(widths[i])

            self.mainLayout.addWidget(self.Item)
 

        # self.inputForm.writeAndClose_button.pressed.connect(self.changeData)
        # self.inputForm.write_button.pressed.connect(self.changeData)

    # def changeData(self):
    #     self._name = self.inputForm.name_lineEdit.text()
    #     self._age = self.inputForm.age_spinBox.value()

    #     self.name_label.setText(self._name)
    #     self.age_label.setText(str(self._age))

    # def mouseDoubleClickEvent(self, e):
    #     self.inputForm.show()
    #     self.inputForm.name_lineEdit.setText(self._name)
    #     self.inputForm.age_spinBox.setValue(self._age)

    def mousePressEvent(self, e):
        self._selected = not self._selected
        self.setStyleSheet(styleSheets.tableItem_selected if self._selected else styleSheets.tableItem)



class Table(QFrame):
    def __init__(self, table_name, parent = None, field_names:str = "id, name", widths:list = []):
        super().__init__(parent)

        self._rows_list = []
        self._rows_count = 0
        self._names_str = field_names
        self._names = field_names.split(", ")
        self._table_name = table_name
        self._widths = widths

        self.setStyleSheet('background: #222')

        self.mainLayout = QVBoxLayout(self)
        self.mainLayout.setContentsMargins(2,2,2,2)
        self.mainLayout.setSpacing(2)

        self.headder_widget = QWidget(self)
        self.headder_widget.setStyleSheet(styleSheets.tableHeader)
        self.headder_widget.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        self.headder_layout = QHBoxLayout(self.headder_widget)
        self.headder_layout.setContentsMargins(0,0,0,0)
        self.headder_layout.setSpacing(2)

        for i in range(len(self._names)):
            self.headerItem = QLabel(self._names[i], self.headder_widget)
            if len(self._widths) and self._widths[i]:
                self.headerItem.setFixedWidth(self._widths[i])

            self.headder_layout.addWidget(self.headerItem)

        self.helpWidget = QWidget()
        self.helpWidget.setFixedWidth(16)
        self.headder_layout.addWidget(self.helpWidget)

        self.mainLayout.addWidget(self.headder_widget)

        self.scrollArea = QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea_centralWidget = QWidget(self.scrollArea)
        self.scrollArea.setWidget(self.scrollArea_centralWidget)

        self.scrollArea_mainLayout = QVBoxLayout(self.scrollArea_centralWidget)
        self.scrollArea_mainLayout.setContentsMargins(0,0,0,0)

        self.list_widget = QWidget(self.scrollArea_centralWidget)
        self.list_layout = QVBoxLayout(self.list_widget)
        self.list_layout.setAlignment(Qt.AlignTop)
        self.list_layout.setContentsMargins(0,0,0,0)
        self.list_layout.setSpacing(2)

        self.scrollArea_mainLayout.addWidget(self.list_widget)

        self.mainLayout.addWidget(self.scrollArea)

        self.fillTable()

    
    def fillTable(self):
        for row in self._rows_list:
            self.list_layout.removeWidget(row)
            row.deleteLater()
            self.row = None

        self._rows_list = []
        self._rows_count = 0
        
        data = readQuery(self._table_name, self._names_str)

        for row in data: 
            self._rows_list.append(TableItem(self.list_widget, self._names, row, self._widths))
            self.list_layout.addWidget(self._rows_list[self._rows_count])
            self._rows_count += 1

    # def selectedRows(self):
    #     selection = []
    #     for row in self._rows_list:
    #         if row._selected:
    #             selection.append(row._id)
    #     return selection
    
    # def mousePressEvent(self, e):
    #     for row in self._rows_list:
    #         row._selected = False
            # row.setStyleSheet(styleSheets.tableItem)
