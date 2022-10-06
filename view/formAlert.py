import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from formPossibility import *


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_formAlert(object):
    def setupUi(self, formAlert):
        formAlert.setObjectName("formAlert")
        formAlert.resize(300, 140)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(30)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(formAlert.sizePolicy().hasHeightForWidth())
        formAlert.setSizePolicy(sizePolicy)
        formAlert.setMinimumSize(QtCore.QSize(300, 140))
        formAlert.setMaximumSize(QtCore.QSize(300, 140))
        formAlert.setWindowOpacity(0.8)
        self.centralwidget = QtWidgets.QWidget(formAlert)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_cancel = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cancel.setGeometry(QtCore.QRect(160, 90, 100, 30))
        self.btn_cancel.setMinimumSize(QtCore.QSize(0, 0))
        self.btn_cancel.setMaximumSize(QtCore.QSize(120, 45))
        self.btn_cancel.setStyleSheet("QPushButton{\n"
"    border-style: none;\n"
"    border-width: 2px;\n"
"    font: 75 11pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(3, 127, 140);\n"
"    border-radius: 12px;\n"
"    border-bottom-color: rgb(4, 35, 38);\n"
"    border-right-color:  rgb(4, 35, 38);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    border-style: insetset;\n"
"    border-width: 2px;\n"
"    font: 75 11pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(3, 127, 140);\n"
"    border-radius: 8px;\n"
"    border-top-color: rgb(4, 35, 38);\n"
"    border-left-color:  rgb(4, 35, 38);\n"
"}")
        self.btn_cancel.setObjectName("btn_cancel")
        self.btn_yes = QtWidgets.QPushButton(self.centralwidget)
        self.btn_yes.setGeometry(QtCore.QRect(40, 90, 100, 30))
        self.btn_yes.setMinimumSize(QtCore.QSize(100, 30))
        self.btn_yes.setMaximumSize(QtCore.QSize(100, 30))
        self.btn_yes.setStyleSheet("QPushButton{\n"
"    border-style: none;\n"
"    border-width: 2px;\n"
"    font: 75 11pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(3, 127, 140);\n"
"    border-radius: 12px;\n"
"    border-bottom-color: rgb(4, 35, 38);\n"
"    border-right-color:  rgb(4, 35, 38);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    border-style: insetset;\n"
"    border-width: 2px;\n"
"    font: 75 11pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(3, 127, 140);\n"
"    border-radius: 8px;\n"
"    border-top-color: rgb(4, 35, 38);\n"
"    border-left-color:  rgb(4, 35, 38);\n"
"}")
        self.btn_yes.setObjectName("btn_yes")
        self.lbl_title = QtWidgets.QLabel(self.centralwidget)
        self.lbl_title.setGeometry(QtCore.QRect(9, 9, 281, 50))
        self.lbl_title.setMinimumSize(QtCore.QSize(0, 0))
        self.lbl_title.setMaximumSize(QtCore.QSize(600, 50))
        self.lbl_title.setObjectName("lbl_title")
        formAlert.setCentralWidget(self.centralwidget)

        self.retranslateUi(formAlert)
        QtCore.QMetaObject.connectSlotsByName(formAlert)

    def retranslateUi(self, formAlert):
        _translate = QtCore.QCoreApplication.translate
        formAlert.setWindowTitle(_translate("formAlert", "Alerta!"))
        self.btn_cancel.setText(_translate("formAlert", "Cancelar"))
        self.btn_yes.setText(_translate("formAlert", "Sim"))
        self.lbl_title.setText(_translate("formAlert", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#037f8c;\">Tem certeza</span></p><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#037f8c;\">que deseja sair desta tela?</span></p></body></html>"))
    ###Botões do sistema###
        self.btn_yes.clicked.connect(self.return_main)
        self.btn_cancel.clicked.connect(self.close_alert)
        
    ###funções so sistema###
    def return_main(self):
        formAlert.close()
        self.formViewResult = QtWidgets.QMainWindow()
        self.ui = Ui_formViewResult()
        self.ui.setupUi(self.formViewResult)
        self.formViewResult.close()
        
    def close_alert(self):
        formAlert.close()   

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    formAlert = QtWidgets.QMainWindow()
    ui = Ui_formAlert()
    ui.setupUi(formAlert)
    formAlert.show()
    sys.exit(app.exec_())
