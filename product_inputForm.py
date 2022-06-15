from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class InputForm(QWidget):
    def __init__(self, id:int = None):
        super().__init__()
        
        self._id = id

        self.mainLayout = QVBoxLayout(self)

        self.buttonsLayout = QHBoxLayout()
        self.buttonsLayout.setContentsMargins(0,0,0,0)
        self.buttonsLayout.setAlignment(Qt.AlignLeft)

        self.save = QPushButton('Сохранить', self)
        self.Close = QPushButton('Закрыть', self)
        
        self.buttonsLayout.addWidget(self.save)
        self.buttonsLayout.addWidget(self.Close)
        self.mainLayout.addLayout(self.buttonsLayout)

        self.formLayout = QFormLayout()
        self.formLayout.setContentsMargins(0,0,0,0)

        self.name_label = QLabel('Наименование', self)
        self.articul_label = QLabel('Артикул', self)
        self.priсe_label = QLabel('Цена', self)
        self.count_label = QLabel('Количество', self)
        self.warehouse_label = QLabel('Склад', self)

        self.name_lineEdit = QLineEdit(self)
        self.articul_lineEdit = QLineEdit(self)
        self.price_spinBox = QSpinBox(self)
        self.price_spinBox.setButtonSymbols(QSpinBox.NoButtons)
        self.price_spinBox.setMaximum(10000000)
        self.count_spinBox = QSpinBox(self)
        self.count_spinBox.setButtonSymbols(QSpinBox.NoButtons)
        self.count_spinBox.setMaximum(10000000)
        self.warehouse_spinBox = QSpinBox(self)
        self.warehouse_spinBox.setButtonSymbols(QSpinBox.NoButtons)
        self.warehouse_spinBox.setMaximum(10000000)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.name_label)
        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.articul_label)
        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.priсe_label)
        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.count_label)
        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.warehouse_label)
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.name_lineEdit)
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.articul_lineEdit)
        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.price_spinBox)
        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.count_spinBox)
        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.warehouse_spinBox)

        self.mainLayout.addLayout(self.formLayout)