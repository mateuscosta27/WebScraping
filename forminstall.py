

from asyncio import selector_events
from time import sleep
from PyQt5 import QtCore, QtGui, QtWidgets
from model import Install
from formFinish import *

class Ui_formInstall(object):
    def setupUi(self, formInstall):
        formInstall.setObjectName("formInstall")
        formInstall.resize(620, 250)
        formInstall.setMaximumSize(QtCore.QSize(620, 250))
        formInstall.setFocusPolicy(QtCore.Qt.ClickFocus)
        formInstall.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(formInstall)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_title = QtWidgets.QLabel(self.centralwidget)
        self.lbl_title.setGeometry(QtCore.QRect(0, 0, 601, 111))
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
        self.br_progress = QtWidgets.QProgressBar(self.centralwidget)
        self.br_progress.setEnabled(True)
        self.br_progress.setGeometry(QtCore.QRect(40, 120, 561, 23))
        self.br_progress.setProperty("value", 0)
        self.br_progress.setTextVisible(False)
        self.br_progress.setObjectName("br_progress")
        self.br_progress.setVisible(False)
        formInstall.setCentralWidget(self.centralwidget)

        self.retranslateUi(formInstall)
        QtCore.QMetaObject.connectSlotsByName(formInstall)
        
        ###Botões do sistema###
        self.btn_start.clicked.connect(self.iniciar) ## insere os diretorios do sistema ##
        self.btn_start.clicked.connect(self.progresso) ## inicia a barra de progresso##
        self.btn_exit.clicked.connect(self.sair_sistema) ## sai do sistema##
        
    def iniciar(self): ##Inicia a funação Install para criação dos diretorios##
        install = Install()
        install.download_driver()
        install.database()
        
        
    def progresso(self): ## inicia a barra de progresso##
        barra = self.br_progress
        barra.setVisible(True)
        barra.setEnabled(True)
        barra.setTextVisible(True)
        sleep(0.01)
        for i in range(101):
            sleep(0.01)
            barra.setProperty("value", i)
        
        if i == 100:
            sleep(0.5)
            self.finish_form()
            sleep(0.5)
            self.sair_install()
            
            
            
            
    ###Função que chama o formFinish##  
    def finish_form(self):
        self.formFinish = QtWidgets.QMainWindow()
        self.ui = Ui_formFinish()
        self.ui.setupUi(self.formFinish)
        self.formFinish.show()
       
    ##Função fecha o forminstall###
    def sair_install(self):
        formInstall.close()
    ###Função sai do sistema###               
    def sair_sistema(self):
        sys.exit()
         

    def retranslateUi(self, formInstall):
        _translate = QtCore.QCoreApplication.translate
        formInstall.setWindowTitle(_translate("formInstall", "Assitente de Instalação"))
        self.lbl_title.setText(_translate("formInstall", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#037f8c;\">BEM VINDO AO ASSISTENTE DE INSTALAÇÃO - GAE</span></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#037f8c;\">GERENCIADOR DE APOSTAS ESPORTIVAS</span></p></body></html>"))
        self.btn_start.setText(_translate("formInstall", "Iniciar instalação"))
        self.btn_exit.setText(_translate("formInstall", "Sair"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    formInstall = QtWidgets.QMainWindow()
    ui = Ui_formInstall()
    ui.setupUi(formInstall)
    formInstall.show()
    sys.exit(app.exec_())
