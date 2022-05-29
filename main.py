from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from table import Table
from input_form import InputForm

from db_connection import *

import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(800, 600)

        self.inputForm = InputForm()

        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)
        self.mainLayout = QVBoxLayout(self.centralWidget)

        self.buttons_layout = QHBoxLayout()
        self.buttons_layout.setAlignment(Qt.AlignLeft)

        self.mainLayout.addLayout(self.buttons_layout)

        self.add_button = QPushButton('Добавить', self.centralWidget)
        self.delete_button = QPushButton('Удалить', self.centralWidget)

        self.buttons_layout.addWidget(self.add_button)
        self.buttons_layout.addWidget(self.delete_button)

        self.table = Table(self.centralWidget)

        self.mainLayout.addWidget(self.table)

        data = readQuery()

        for row in data:
            id, name, age = row
            self.table.addRow(id, name, age)

        self.add_button.pressed.connect(self.inputForm.show)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())