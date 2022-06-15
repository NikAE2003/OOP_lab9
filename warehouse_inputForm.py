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
        self.manager_label = QLabel('Заведующий', self)

        self.name_lineEdit = QLineEdit(self)
        self.manager_lineEdit = QLineEdit(self)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.name_label)
        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.manager_label)
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.name_lineEdit)
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.manager_lineEdit)

        self.mainLayout.addLayout(self.formLayout)