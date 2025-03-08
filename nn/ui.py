import random
import string
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(766, 549)
        MainWindow.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_generate = QtWidgets.QPushButton(self.centralwidget)
        self.btn_generate.setGeometry(QtCore.QRect(270, 360, 181, 91))
        self.btn_generate.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"color: rgb(0, 0, 0);\n"
"border: 3px solid darkblue;\n"
"border-radius: 5px")
        self.btn_generate.setObjectName("btn_generate")
        self.cb_numbers = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_numbers.setGeometry(QtCore.QRect(80, 250, 221, 71))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.cb_numbers.setFont(font)
        self.cb_numbers.setObjectName("cb_numbers")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(80, 160, 231, 81))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.result = QtWidgets.QLabel(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(270, 110, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.result.setFont(font)
        self.result.setAlignment(QtCore.Qt.AlignCenter)
        self.result.setObjectName("result")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(270, 60, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.title.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 766, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.btn_generate.clicked.connect(self.generate_password)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_generate.setText(_translate("MainWindow", "Згенерувати"))
        self.cb_numbers.setText(_translate("MainWindow", "Використовувати числа"))
        self.checkBox_2.setText(_translate("MainWindow", "Використовувати алфавіт"))
        self.result.setText(_translate("MainWindow", "Результат"))
        self.title.setText(_translate("MainWindow", "Генератор Паролів"))

    def generate_password(self):
        password_length = 4

        characters = ""

        if self.cb_numbers.isChecked():
            characters += string.digits

        if self.checkBox_2.isChecked():
            characters += string.ascii_letters

        if not characters:
            self.result.setText("Не вибрано жодної опції!")
            return

        password = ''.join(random.choice(characters) for _ in range(password_length))

        self.result.setText(password)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
