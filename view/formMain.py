import os
import sys
import threading
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from formConfdb import *
from formConfdbFinished import *
from controller.Controller import Controller
from PyQt5 import QtCore, QtGui, QtWidgets
from formPossibility import *

class Ui_formPrincipal(object):
    def setupUi(self, formPrincipal):
        formPrincipal.setObjectName("formPrincipal")
        formPrincipal.resize(800, 400)
        formPrincipal.setMinimumSize(QtCore.QSize(800, 400))
        formPrincipal.setMaximumSize(QtCore.QSize(800, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("src/principal_icon.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        formPrincipal.setWindowIcon(icon)
        formPrincipal.setWindowOpacity(1.0)
        formPrincipal.setToolTip("")
        formPrincipal.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "border-radius: 20px;\n"
                                    "\n"
                                    "\n"
                                    "border-color: rgb(4, 35, 38);")
        formPrincipal.setTabShape(QtWidgets.QTabWidget.Rounded)
        formPrincipal.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks | QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(formPrincipal)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_title = QtWidgets.QLabel(self.centralwidget)
        self.lbl_title.setGeometry(QtCore.QRect(142, 20, 535, 75))
        self.lbl_title.setMinimumSize(QtCore.QSize(535, 75))
        self.lbl_title.setMaximumSize(QtCore.QSize(535, 75))
        self.lbl_title.setObjectName("lbl_title")
        self.btn_sair = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sair.setGeometry(QtCore.QRect(690, 350, 105, 45))
        self.btn_sair.setMinimumSize(QtCore.QSize(105, 45))
        self.btn_sair.setMaximumSize(QtCore.QSize(105, 45))
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
        self.btn_coletar.setGeometry(QtCore.QRect(270, 140, 280, 45))
        self.btn_coletar.setMinimumSize(QtCore.QSize(280, 45))
        self.btn_coletar.setMaximumSize(QtCore.QSize(280, 45))
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
        self.btn_visJogos.setGeometry(QtCore.QRect(270, 240, 280, 45))
        self.btn_visJogos.setMinimumSize(QtCore.QSize(280, 45))
        self.btn_visJogos.setMaximumSize(QtCore.QSize(280, 45))
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
        self.btn_visPossibilidades.setGeometry(QtCore.QRect(270, 190, 280, 45))
        self.btn_visPossibilidades.setMaximumSize(QtCore.QSize(280, 45))
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
        self.btn_simular.setGeometry(QtCore.QRect(270, 290, 280, 45))
        self.btn_simular.setMaximumSize(QtCore.QSize(280, 45))
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

    ###Botões do Sistema###

        self.btn_sair.clicked.connect(self.exit_system)
        self.btn_coletar.clicked.connect(self.thred_process)
        self.btn_visPossibilidades.clicked.connect(self.open_possibilities)
        

        
        
    ###funções sistema###
    
    def collect(self):
        """Função cria objeto da classe controller para coletar os dados
           Function creates object from the controller class to collect the data
        """
        
        ##Estilo padrão do botão desabilitado##
        ##Style default of the button desabled##
        style_disabled = ("QPushButton{\n"
                          "    border-style: none;\n"
                          "    border-width: 2px;\n"
                          "    font: 75 11pt \"MS Shell Dlg 2\";\n"
                          "    color: rgb(255, 255, 255);\n"
                          "    background-color: rgb(184, 184, 184);\n"
                          "    border-radius: 12px;\n"
                          "    border-bottom-color: rgb(4, 35, 38);\n"
                          "    border-right-color:  rgb(4, 35, 38);\n"
                          "}\n")
        
        
        ##Estilo padrão do botão habilitado##
        ##Style default of the button enaabled##
        style_enabled = ("QPushButton{\n"
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
        ##Este bloco desabilita os botões impedindo o clique##
        ##This block disables the buttons preventing clicking##  
        self.btn_coletar.setEnabled(False)  
        self.btn_visPossibilidades.setEnabled(False)
        self.btn_visJogos.setEnabled(False)
        self.btn_simular.setEnabled(False)
        self.btn_visPossibilidades.setStyleSheet(style_disabled)
        self.btn_visJogos.setStyleSheet(style_disabled)
        self.btn_simular.setStyleSheet(style_disabled)
        
        ##Instância de Classe##
        ##class instance##
        controller = Controller()
        controller.controller_pixbet()
        controller.controller_betano()
        controller.create_tables()
        ##Volta valor padrão dos botões##
        ##Volta valor padrão dos botões##
        self.btn_coletar.setEnabled(True)
        self.btn_visPossibilidades.setEnabled(True)
        self.btn_visJogos.setEnabled(True)
        self.btn_simular.setEnabled(True)
        self.btn_visPossibilidades.setStyleSheet(style_enabled)
        self.btn_visJogos.setStyleSheet(style_enabled)
        self.btn_simular.setStyleSheet(style_enabled)

    def thred_process(self):
        """Trabalha com thread na coleta
           Works with thread in the collection
        """
        self.thread1 = threading.Thread(target=self.collect)
        self.thread1.start()
           
    def open_possibilities(self):
        """Abre o forma de visualização de possibilidades
           Open the possibilities viewer 
        """
        self.formViewResult = QtWidgets.QMainWindow()
        self.ui = Ui_formViewResult()
        self.ui.setupUi(self.formViewResult)
        self.formViewResult.show()

    def exit_system(self):
        """Sai do sistema
           Exit system
        """
        sys.exit()

    def retranslateUi(self, formPrincipal):
        _translate = QtCore.QCoreApplication.translate
        formPrincipal.setWindowTitle(_translate("formPrincipal", "Modulo Principal"))
        self.lbl_title.setText(_translate("formPrincipal", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#037f8c;\">BEM VINDO AO  APOSTADORPRO</span></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#037f8c;\">Torne suas possibilidades em jogos certeiros</span></p></body></html>"))
        self.btn_sair.setText(_translate("formPrincipal", "Sair"))
        self.btn_coletar.setText(_translate("formPrincipal", "Coletar Dados"))
        self.btn_visJogos.setText(_translate("formPrincipal", "Visualizar Jogos"))
        self.btn_visPossibilidades.setText(_translate("formPrincipal", " Possibilidades"))
        self.btn_simular.setText(_translate("formPrincipal", "Simular Aposta"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    formPrincipal = QtWidgets.QMainWindow()
    ui = Ui_formPrincipal()
    ui.setupUi(formPrincipal)
    formPrincipal.show()
    sys.exit(app.exec_())
