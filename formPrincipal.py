
from PyQt5 import QtCore, QtGui, QtWidgets
from time import sleep
from formConfdb import *
from model import Install
from formConfdbFinished import *



class Ui_formPrincipal(object):
    def setupUi(self, formPrincipal):
        formPrincipal.setObjectName("formPrincipal")
        formPrincipal.resize(800, 400)
        formPrincipal.setMinimumSize(QtCore.QSize(800, 400))
        formPrincipal.setMaximumSize(QtCore.QSize(800, 400))
        formPrincipal.setWindowOpacity(1.0)
        formPrincipal.setToolTip("")
        formPrincipal.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"\n"
"\n"
"border-color: rgb(4, 35, 38);")
        formPrincipal.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(formPrincipal)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_title = QtWidgets.QLabel(self.centralwidget)
        self.lbl_title.setGeometry(QtCore.QRect(142, 20, 532, 46))
        self.lbl_title.setObjectName("lbl_title")
        self.btn_sair = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sair.setGeometry(QtCore.QRect(690, 350, 101, 41))
        self.btn_sair.setStyleSheet("QPushButton{\n"
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
        self.btn_sair.setObjectName("btn_sair")
        self.btn_coletar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_coletar.setGeometry(QtCore.QRect(270, 140, 275, 41))
        self.btn_coletar.setStyleSheet("QPushButton{\n"
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
        self.btn_coletar.setObjectName("btn_coletar")
        self.btn_visJogos = QtWidgets.QPushButton(self.centralwidget)
        self.btn_visJogos.setGeometry(QtCore.QRect(270, 240, 275, 41))
        self.btn_visJogos.setStyleSheet("QPushButton{\n"
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
        self.btn_visJogos.setObjectName("btn_visJogos")
        self.btn_visPossibilidades = QtWidgets.QPushButton(self.centralwidget)
        self.btn_visPossibilidades.setGeometry(QtCore.QRect(270, 190, 275, 41))
        self.btn_visPossibilidades.setStyleSheet("QPushButton{\n"
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
        self.btn_visPossibilidades.setObjectName("btn_visPossibilidades")
        self.btn_simular = QtWidgets.QPushButton(self.centralwidget)
        self.btn_simular.setGeometry(QtCore.QRect(270, 290, 275, 41))
        self.btn_simular.setStyleSheet("QPushButton{\n"
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
        self.btn_simular.setObjectName("btn_simular")
        formPrincipal.setCentralWidget(self.centralwidget)

        self.retranslateUi(formPrincipal)
        QtCore.QMetaObject.connectSlotsByName(formPrincipal)
        
        ###Botões do sistema###
        self.btn_start.clicked.connect(self.conf_db) ## insere os diretorios do sistema ##
        self.btn_start.clicked.connect(self.progress) ## inicia a barra de progresso##
        self.btn_exit.clicked.connect(self.exit_system) ## sai do sistema##
        
    ###função de configuração###   
    def conf_db(self): ##Inicia a funação conf_db para criação dos diretorios##
        install = Install()
        install.download_driver()
        install.database()
        
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
            sleep(0.5)
            self.form_final()
            sleep(0.5)
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
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

    def retranslateUi(self, formPrincipal):
        _translate = QtCore.QCoreApplication.translate
        formPrincipal.setWindowTitle(_translate("formPrincipal", "Modulo Principal"))
        self.lbl_title.setText(_translate("formPrincipal", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#037f8c;\">BEM VINDO AO  APOSTADORPRO</span></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#037f8c;\">Torne sua possibilidades em jogos certeiros</span></p></body></html>"))
        self.btn_sair.setText(_translate("formPrincipal", "Sair"))
        self.btn_coletar.setText(_translate("formPrincipal", "Coletar Dados"))
        self.btn_visJogos.setText(_translate("formPrincipal", "Visualizar Jogos"))
        self.btn_visPossibilidades.setText(_translate("formPrincipal", "Visualizar Possibilidades de Aposta"))
        self.btn_simular.setText(_translate("formPrincipal", "Simular Aposta"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    formPrincipal = QtWidgets.QMainWindow()
    ui = Ui_formPrincipal()
    ui.setupUi(formPrincipal)
    formPrincipal.show()
    sys.exit(app.exec_())
