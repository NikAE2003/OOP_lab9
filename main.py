from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from table import Table

from db_connection import *

import sys
import styleSheets

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.resize(700, 500)

        self.centralWidget = QWidget()
        self.centralWidget.setStyleSheet(styleSheets.main)
        self.centralLayout = QVBoxLayout(self.centralWidget)

        self.tabWidget = QTabWidget(self.centralWidget)
        self.tabWidget.addTab(Table("Склад", self.tabWidget, 'id, Наименование, Заведующий складом', [15, 0, 0]), "Склады")
        self.tabWidget.addTab(Table("Товар", self.tabWidget, 'id, Наименование, Артикул, Цена, Количество', [15, 0, 0, 0, 0]), "Товары")


        self.centralLayout.addWidget(self.tabWidget)
        self.setCentralWidget(self.centralWidget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())