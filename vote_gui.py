# Form implementation generated from reading ui file 'vote_gui.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(827, 695)
        MainWindow.setMinimumSize(QtCore.QSize(827, 695))
        MainWindow.setMaximumSize(QtCore.QSize(827, 695))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(parent=self.centralwidget)
        self.title.setGeometry(QtCore.QRect(260, 20, 291, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.id_input = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.id_input.setGeometry(QtCore.QRect(310, 110, 231, 41))
        self.id_input.setObjectName("id_input")
        self.id_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.id_label.setGeometry(QtCore.QRect(250, 110, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.id_label.setFont(font)
        self.id_label.setObjectName("id_label")
        self.candidates_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.candidates_label.setGeometry(QtCore.QRect(290, 180, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.candidates_label.setFont(font)
        self.candidates_label.setObjectName("candidates_label")
        self.bianca_radio = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.bianca_radio.setGeometry(QtCore.QRect(280, 250, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.bianca_radio.setFont(font)
        self.bianca_radio.setObjectName("bianca_radio")
        self.edward_radio = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.edward_radio.setGeometry(QtCore.QRect(280, 290, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.edward_radio.setFont(font)
        self.edward_radio.setObjectName("edward_radio")
        self.felicia_radio = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.felicia_radio.setGeometry(QtCore.QRect(280, 330, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.felicia_radio.setFont(font)
        self.felicia_radio.setObjectName("felicia_radio")
        self.submit_push = QtWidgets.QPushButton(parent=self.centralwidget)
        self.submit_push.setGeometry(QtCore.QRect(280, 370, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.submit_push.setFont(font)
        self.submit_push.setObjectName("submit_push")
        self.result_push = QtWidgets.QPushButton(parent=self.centralwidget)
        self.result_push.setGeometry(QtCore.QRect(280, 430, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.result_push.setFont(font)
        self.result_push.setObjectName("result_push")
        self.output_text_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.output_text_label.setGeometry(QtCore.QRect(250, 510, 371, 111))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.output_text_label.setFont(font)
        self.output_text_label.setText("")
        self.output_text_label.setObjectName("output_text_label")
        self.title.raise_()
        self.id_input.raise_()
        self.id_label.raise_()
        self.candidates_label.raise_()
        self.bianca_radio.raise_()
        self.edward_radio.raise_()
        self.submit_push.raise_()
        self.result_push.raise_()
        self.output_text_label.raise_()
        self.felicia_radio.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 827, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Voting Application"))
        self.title.setText(_translate("MainWindow", "Voting Application"))
        self.id_label.setText(_translate("MainWindow", "ID"))
        self.candidates_label.setText(_translate("MainWindow", "CANDIDATES"))
        self.bianca_radio.setText(_translate("MainWindow", "Bianca"))
        self.edward_radio.setText(_translate("MainWindow", "Edward"))
        self.felicia_radio.setText(_translate("MainWindow", "Felicia"))
        self.submit_push.setText(_translate("MainWindow", "Submit"))
        self.result_push.setText(_translate("MainWindow", "Results"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
