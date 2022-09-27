import threading
from PyQt5 import QtCore, QtGui, QtWidgets
from model import *
from model.Model import Betano
from formFinish import *
from multiprocessing import Process
import threading

class Ui_formPrincipal(object):
    def setupUi(self, formPrincipal):
        formPrincipal.setObjectName("formPrincipal")
        formPrincipal.resize(800, 400)
        formPrincipal.setMinimumSize(QtCore.QSize(800, 400))
        formPrincipal.setMaximumSize(QtCore.QSize(800, 400))
        formPrincipal.setWindowOpacity(1.0)
        formPrincipal.setToolTip("")
        formPrincipal.setStyleSheet("background-color: rgb(255, 255, 255);")
        formPrincipal.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(formPrincipal)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_title = QtWidgets.QLabel(self.centralwidget)
        self.lbl_title.setGeometry(QtCore.QRect(142, 20, 532, 46))
        self.lbl_title.setObjectName("lbl_title")
        self.btn_sair = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sair.setGeometry(QtCore.QRect(690, 350, 101, 41))
        self.btn_sair.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(3, 127, 140);")
        self.btn_sair.setObjectName("btn_sair")
        self.btn_coletar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_coletar.setGeometry(QtCore.QRect(270, 140, 275, 41))
        self.btn_coletar.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(3, 127, 140);")
        self.btn_coletar.setObjectName("btn_coletar")
        self.btn_visJogos = QtWidgets.QPushButton(self.centralwidget)
        self.btn_visJogos.setGeometry(QtCore.QRect(270, 240, 275, 41))
        self.btn_visJogos.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(3, 127, 140);")
        self.btn_visJogos.setObjectName("btn_visJogos")
        self.btn_visPossibilidades = QtWidgets.QPushButton(self.centralwidget)
        self.btn_visPossibilidades.setGeometry(QtCore.QRect(270, 190, 275, 41))
        self.btn_visPossibilidades.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(3, 127, 140);")
        self.btn_visPossibilidades.setObjectName("btn_visPossibilidades")
        self.btn_simular = QtWidgets.QPushButton(self.centralwidget)
        self.btn_simular.setGeometry(QtCore.QRect(270, 290, 275, 41))
        self.btn_simular.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(3, 127, 140);")
        self.btn_simular.setObjectName("btn_simular")
        formPrincipal.setCentralWidget(self.centralwidget)

        self.retranslateUi(formPrincipal)
        QtCore.QMetaObject.connectSlotsByName(formPrincipal)
        
        
        ###Botões Modulo principal###
        
        self.btn_sair.clicked.connect(self.sair_sistema)
        self.btn_coletar.clicked.connect(self.parallel_process)
        
        
        
        ###funções sistema###
    def collect(self):
        betano = Betano()
        betano.open_web_site()
        betano.close_banner()
         
    def parallel_process(self):
        self.thread2 = threading.Thread(target=self.disable_buttons)  
        self.thread1 = threading.Thread(target=self.collect)
        self.thread2.start()
        self.thread1.start()
        
          
    def disable_buttons(self):
       
        self.btn_coletar.setDisabled(True)
        self.btn_visPossibilidades.setDisabled(True)
        self.btn_visPossibilidades.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
        "color: rgb(255, 255, 255);\n"
        "background-color: rgb(184, 184, 184);")
        self.btn_visJogos.setDisabled(True)
        self.btn_visJogos.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
        "color: rgb(255, 255, 255);\n"
        "background-color: rgb(184, 184, 184);")
        self.btn_simular.setDisabled(True)
        self.btn_simular.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
        "color: rgb(255, 255, 255);\n"
        "background-color: rgb(184, 184, 184);")
        
                
        
                        
               
       
                      
    def sair_sistema(self):
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
