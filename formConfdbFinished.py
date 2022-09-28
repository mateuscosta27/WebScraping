
from PyQt5 import QtCore, QtGui, QtWidgets
from formConfdb import *
from formPrincipal import *


class Ui_formConfdbFinished(object):
    def setupUi(self, formConfdbFinished):
        formConfdbFinished.setObjectName("formConfdbFinished")
        formConfdbFinished.resize(365, 185)
        formConfdbFinished.setMinimumSize(QtCore.QSize(365, 185))
        formConfdbFinished.setMaximumSize(QtCore.QSize(365, 185))
        formConfdbFinished.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(formConfdbFinished)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_title = QtWidgets.QLabel(self.centralwidget)
        self.lbl_title.setGeometry(QtCore.QRect(0, 0, 361, 61))
        self.lbl_title.setObjectName("lbl_title")
        self.btn_start = QtWidgets.QPushButton(self.centralwidget)
        self.btn_start.setGeometry(QtCore.QRect(80, 80, 190, 45))
        self.btn_start.setStyleSheet("QPushButton{\n"
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
        self.btn_start.setObjectName("btn_start")
        self.btn_exit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_exit.setGeometry(QtCore.QRect(80, 130, 190, 45))
        self.btn_exit.setStyleSheet("QPushButton{\n"
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
        self.btn_exit.setObjectName("btn_exit")
        formConfdbFinished.setCentralWidget(self.centralwidget)

        self.retranslateUi(formConfdbFinished)
        QtCore.QMetaObject.connectSlotsByName(formConfdbFinished)
        
        
         ##Botões do Sistema##
        self.btn_start.clicked.connect(self.start_main) ## Inicia modulo principal
        self.btn_exit.clicked.connect(self.exit_system) ## Encerra o sistema
        
    ###Função de inicio modulo principal###    
    def start_main(self):
        self.formPrincipal = QtWidgets.QMainWindow()
        self.ui = Ui_formPrincipal()
        self.ui.setupUi(self.formPrincipal)
        self.formPrincipal.show()
        
    ###Função para fechar formulario formFinish###    
    def close_formfinish(self):
        fi = Ui_formConfdbFinished()
        fi.close()
    ###Função de sair do sistema###         
    def exit_system(self):
        sys.exit()
        
        
        

    def retranslateUi(self, formConfdbFinished):
        _translate = QtCore.QCoreApplication.translate
        formConfdbFinished.setWindowTitle(_translate("formConfdbFinished", "Assistente de Configuração"))
        self.lbl_title.setText(_translate("formConfdbFinished", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#037f8c;\">CONFIGURAÇÃO CONCLUÍDA!</span></p></body></html>"))
        self.btn_start.setText(_translate("formConfdbFinished", "Iniciar"))
        self.btn_exit.setText(_translate("formConfdbFinished", "Sair"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    formConfdbFinished = QtWidgets.QMainWindow()
    ui = Ui_formConfdbFinished()
    ui.setupUi(formConfdbFinished)
    formConfdbFinished.show()
    sys.exit(app.exec_())
