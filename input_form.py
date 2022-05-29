from asyncore import write
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from db_connection import writeQuery

class InputForm(QMainWindow):
    def __init__(self, id = None):
        super().__init__()
        
        self._id = id

        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)

        self.mainLayout = QVBoxLayout(self.centralWidget)
        self.mainLayout.setContentsMargins(5, 5, 5, 5)
        self.mainLayout.setAlignment(Qt.AlignTop)

        self.buttons_layout = QHBoxLayout()
        self.buttons_layout.setContentsMargins(0,0,0,0)
        self.buttons_layout.setAlignment(Qt.AlignLeft)

        self.form_layout = QFormLayout()
        self.form_layout.setContentsMargins(0,0,0,0)

        self.mainLayout.addLayout(self.buttons_layout)
        self.mainLayout.addLayout(self.form_layout)

        self.writeAndClose_button = QPushButton(self.centralWidget, text = 'Сохранить и закрыть')
        self.write_button = QPushButton(self.centralWidget, text = 'Сохранить')

        self.buttons_layout.addWidget(self.writeAndClose_button)
        self.buttons_layout.addWidget(self.write_button)

        self.name_label = QLabel(self.centralWidget, text = 'Имя')
        self.age_label = QLabel(self.centralWidget, text = 'Возраст')

        self.name_lineEdit = QLineEdit(self.centralWidget)
        self.age_spinBox = QSpinBox(self.centralWidget)
        self.age_spinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.form_layout.setWidget(0, QFormLayout.LabelRole, self.name_label)
        self.form_layout.setWidget(0, QFormLayout.FieldRole, self.name_lineEdit)
        self.form_layout.setWidget(1, QFormLayout.LabelRole, self.age_label)
        self.form_layout.setWidget(1, QFormLayout.FieldRole, self.age_spinBox)

        self.write_button.pressed.connect(self.write)
        self.writeAndClose_button.pressed.connect(self.writeAndClose)

    def write(self):
        if self._id is None:
            query = f"""
            INSERT INTO student(name, age)
            VALUES 
                ("{self.name_lineEdit.text()}", 
                {self.age_spinBox.value()})
            """
        else:
            query = f"""
            UPDATE 
                student
            SET
                name = "{self.name_lineEdit.text()}",
                age = {self.age_spinBox.value()}
            WHERE
                id = {self._id}
            """
        writeQuery(query)

    def writeAndClose(self):
        self.write()
        self.close()