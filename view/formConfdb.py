import os
import sys
from time import sleep

from PyQt5 import QtCore, QtGui, QtWidgets
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from controller import Controller
from formConfdbFinished import *



class Ui_formConfdb(object):
    def setupUi(self, formConfdb):
        formConfdb.setObjectName("formConfdb")
        formConfdb.resize(620, 250)
        formConfdb.setMinimumSize(QtCore.QSize(620, 250))
        formConfdb.setMaximumSize(QtCore.QSize(620, 250))
        formConfdb.setFocusPolicy(QtCore.Qt.ClickFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("src/config_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        formConfdb.setWindowIcon(icon)
        formConfdb.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(formConfdb)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_title = QtWidgets.QLabel(self.centralwidget)
        self.lbl_title.setGeometry(QtCore.QRect(0, 0, 620, 115))
        self.lbl_title.setObjectName("lbl_title")
        self.btn_start = QtWidgets.QPushButton(self.centralwidget)
        self.btn_start.setGeometry(QtCore.QRect(100, 160, 200, 45))
        self.btn_start.setMinimumSize(QtCore.QSize(200, 45))
        self.btn_start.setMaximumSize(QtCore.QSize(200, 45))
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
        self.btn_exit.setGeometry(QtCore.QRect(320, 160, 200, 45))
        self.btn_exit.setMinimumSize(QtCore.QSize(200, 45))
        self.btn_exit.setMaximumSize(QtCore.QSize(200, 45))
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
        self.br_progress = QtWidgets.QProgressBar(self.centralwidget)
        self.br_progress.setEnabled(True)
        self.br_progress.setGeometry(QtCore.QRect(20, 120, 580, 25))
        self.br_progress.setMinimumSize(QtCore.QSize(580, 25))
        self.br_progress.setMaximumSize(QtCore.QSize(580, 25))
        self.br_progress.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(1, 31, 38);")
        self.br_progress.setProperty("value", 0)
        self.br_progress.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.br_progress.setTextVisible(True)
        self.br_progress.setVisible(False)
        self.br_progress.setObjectName("br_progress")
        formConfdb.setCentralWidget(self.centralwidget)

        self.retranslateUi(formConfdb)
        QtCore.QMetaObject.connectSlotsByName(formConfdb)
        
         ###Botões do sistema###
        self.btn_start.clicked.connect(self.conf_db) ## insere os diretorios do sistema ##
        self.btn_start.clicked.connect(self.progress) ## inicia a barra de progresso##
        self.btn_exit.clicked.connect(self.exit_system) ## sai do sistema##
        
    ###função de configuração###   
    def conf_db(self): ##Inicia a funação conf_db para criação dos diretorios##
        confdb = Controller()
        confdb.controller_confdb()
        
    ##Função da barra de progresso###   
    def progress(self): ## inicia a barra de progresso##
        barra = self.br_progress
        barra.setVisible(True)
        barra.setEnabled(True)
        barra.setTextVisible(True)
        sleep(0.01)
        for i in range(101):
            sleep(0.01)
            barra.setProperty("value", i)
        
        if i == 100:
            sleep(0.8)
            self.form_final()
            self.exit_install()
            
                          
    ###Função que chama o formFinish##  
    def form_final(self):
        self.formConfdbFinished = QtWidgets.QMainWindow()
        self.ui = Ui_formConfdbFinished()
        self.ui.setupUi(self.formConfdbFinished)
        self.formConfdbFinished.show()
       
    ##Função fecha o forminstall###
    def exit_install(self):
        formConfdb.close()
    ###Função sai do sistema###               
    def exit_system(self):
        sys.exit()
        

    def retranslateUi(self, formConfdb):
        _translate = QtCore.QCoreApplication.translate
        formConfdb.setWindowTitle(_translate("formConfdb", "Assitente de Instalação"))
        self.lbl_title.setText(_translate("formConfdb", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#037f8c;\">BEM VINDO AO ASSISTENTE DE CONFIGURAÇÃO - APOSTADORPRO</span></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#037f8c;\">GERENCIADOR DE APOSTAS ESPORTIVAS</span></p></body></html>"))
        self.btn_start.setText(_translate("formConfdb", "Iniciar Configuração"))
        self.btn_exit.setText(_translate("formConfdb", "Sair"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    formConfdb = QtWidgets.QMainWindow()
    ui = Ui_formConfdb()
    ui.setupUi(formConfdb)
    formConfdb.show()
    sys.exit(app.exec_())
