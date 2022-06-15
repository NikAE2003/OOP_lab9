from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from table import Table

from db_connection import *

import sys
import styleSheets
import product_inputForm
import warehouse_inputForm


class Warehouse_listForm(QWidget):
    def __init__(self):
        super().__init__()

        self.mainLayout = QVBoxLayout(self)
        self.buttonsLayout = QHBoxLayout()
        self.buttonsLayout.setContentsMargins(0,0,0,0)
        self.buttonsLayout.setAlignment(Qt.AlignLeft)

        self.add = QPushButton('Создать', self)
        self.delete = QPushButton('Удалить', self)

        self.buttonsLayout.addWidget(self.add)
        self.buttonsLayout.addWidget(self.delete)
        self.mainLayout.addLayout(self.buttonsLayout)

        self.table = Table("Склад", 'id, Наименование, Заведующий складом', [15, 0, 0], parent = self)
        self.mainLayout.addWidget(self.table)

class Product_listForm(QWidget):
    def __init__(self):
        super().__init__()

        self.mainLayout = QVBoxLayout(self)
        self.buttonsLayout = QHBoxLayout()
        self.buttonsLayout.setContentsMargins(0,0,0,0)
        self.buttonsLayout.setAlignment(Qt.AlignLeft)

        self.add = QPushButton('Создать', self)
        self.delete = QPushButton('Удалить', self)

        self.buttonsLayout.addWidget(self.add)
        self.buttonsLayout.addWidget(self.delete)
        self.mainLayout.addLayout(self.buttonsLayout)

        self.table = Table("Товар", 'id, Наименование, Артикул, Цена, Количество, Склад', [15, 0, 0, 0, 0, 0], parent = self)
        self.mainLayout.addWidget(self.table)

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self._openedForms = []

        self.resize(700, 500)

        self.centralWidget = QWidget()
        self.centralWidget.setStyleSheet(styleSheets.main)
        self.centralLayout = QVBoxLayout(self.centralWidget)

        self.tabWidget = QTabWidget(self.centralWidget)

        self.warehouses = Warehouse_listForm()
        self.products = Product_listForm()

        self.tabWidget.addTab(self.warehouses, 'Склады')
        self.tabWidget.addTab(self.products, "Товары")

        self.centralLayout.addWidget(self.tabWidget)
        self.setCentralWidget(self.centralWidget)

        self.connecting()

    def connecting(self):
        self.warehouses.add.pressed.connect(self.addWarehouse)
        self.products.add.pressed.connect(self.addProduct)
        self.warehouses.table.cellDoubleClicked.connect(self.openWarehouse)
        self.products.table.cellDoubleClicked.connect(self.openProduct)

    def openWarehouse(self, row):
        id = int(self.warehouses.table.item(row, 0).text())

        data = readQuery('Склад', 'Наименование, Заведующий складом', id)

        name, manager = data[0]['Наименование'], data[0]['Заведующий складом']

        form = warehouse_inputForm.InputForm(id)
        form.name_lineEdit.setText(name)
        form.manager_lineEdit.setText(manager)

        self._openedForms.append(form)
        self.tabWidget.addTab(form, f'{name} (склад)')
        form.Close.pressed.connect(self.closeForm)  
        form.save.pressed.connect(self.writeWarehouse)

    def openProduct(self, row):
        id = int(self.products.table.item(row, 0).text())

        data = readQuery('Товар', 'Наименование, Артикул, Цена, Количество, Склад', id)

        name = data[0]['Наименование']
        articul = data[0]['Артикул']
        price = data[0]['Цена']
        count = data[0]['Количество']
        warehouse = data[0]['Склад']

        form = product_inputForm.InputForm(id)
        form.name_lineEdit.setText(name)
        form.articul_lineEdit.setText(articul)
        form.price_spinBox.setValue(int(price))
        form.count_spinBox.setValue(int(count))
        form.warehouse_spinBox.setValue(int(warehouse))

        self._openedForms.append(form)
        self.tabWidget.addTab(form, f'{name} (товар)')
        form.Close.pressed.connect(self.closeForm)        
    
    def addWarehouse(self):
        form = warehouse_inputForm.InputForm()
        self._openedForms.append(form)
        self.tabWidget.addTab(form, 'Создать склад')
        form.Close.pressed.connect(self.closeForm)
        form.save.pressed.connect(self.writeWarehouse)
    
    def addProduct(self):
        form = product_inputForm.InputForm()
        self._openedForms.append(form)
        self.tabWidget.addTab(form, 'Создать товар')
        form.Close.pressed.connect(self.closeForm)
    
    def writeWarehouse(self):
        form = self.sender().parent()
        id = form._id

        name = form.name_lineEdit.text()
        manager = form.manager_lineEdit.text()

        if id is None:
            query = f"""
            INSERT INTO "Склад"
            ("Наименованиe", 
            "Заведующий складом")
            VALUES
            ("{name}",
            "{manager}");
            """
        else:
            query = f"""
            UPDATE "Склад"
            SET
            "Наименование" = "{name}",
            "Заведующий складом" = "{manager}"
            WHERE id = {id};
            """
        print(query)
        writeQuery(query)

        self.warehouses.table.fillTable()

    def closeForm(self):
        sender = self.sender()
        index = self._openedForms.index(sender.parent())
        self.tabWidget.removeTab(index + 2)
        print(self._openedForms)
        self._openedForms.remove(sender.parent())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())