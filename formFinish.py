from PyQt5 import QtCore, QtGui, QtWidgets
from formPrincipal import *
from formPrincipal import Ui_formPrincipal

class Ui_formFinish(object):
    def setupUi(self, formFinish):
        formFinish.setObjectName("formFinish")
        formFinish.resize(620, 250)
        formFinish.setMaximumSize(QtCore.QSize(620, 250))
        formFinish.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(formFinish)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_title = QtWidgets.QLabel(self.centralwidget)
        self.lbl_title.setGeometry(QtCore.QRect(10, 50, 601, 111))
        self.lbl_title.setObjectName("lbl_title")
        self.btn_start = QtWidgets.QPushButton(self.centralwidget)
        self.btn_start.setGeometry(QtCore.QRect(100, 160, 195, 45))
        self.btn_start.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(3, 127, 140);")
        self.btn_start.setObjectName("btn_start")
        self.btn_exit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_exit.setGeometry(QtCore.QRect(300, 160, 195, 45))
        self.btn_exit.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(3, 127, 140);")
        self.btn_exit.setObjectName("btn_exit")
        formFinish.setCentralWidget(self.centralwidget)

        self.retranslateUi(formFinish)
        QtCore.QMetaObject.connectSlotsByName(formFinish)
        
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
        fi = Ui_formFinish()
        fi.close()
    ###Função de sair do sistema###         
    def exit_system(self):
        sys.exit()
        

    def retranslateUi(self, formFinish):
        _translate = QtCore.QCoreApplication.translate
        formFinish.setWindowTitle(_translate("formFinish", "Assistente de Instalação"))
        self.lbl_title.setText(_translate("formFinish", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#037f8c;\">INSTALAÇÃO E CONFIGURAÇÃO CONCLUÍDA!!</span></p></body></html>"))
        self.btn_start.setText(_translate("formFinish", "INICIAR PROGRAMA"))
        self.btn_exit.setText(_translate("formFinish", "Sair"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    formFinish = QtWidgets.QMainWindow()
    ui = Ui_formFinish()
    ui.setupUi(formFinish)
    formFinish.show()
    sys.exit(app.exec_())
