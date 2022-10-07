# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'formPrincipal.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_formPrincipal(object):
    def setupUi(self, formPrincipal):
        formPrincipal.setObjectName("formPrincipal")
        formPrincipal.resize(800, 400)
        formPrincipal.setMinimumSize(QtCore.QSize(800, 400))
        formPrincipal.setMaximumSize(QtCore.QSize(800, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("src/principal_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        formPrincipal.setWindowIcon(icon)
        formPrincipal.setWindowOpacity(1.0)
        formPrincipal.setToolTip("")
        formPrincipal.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"\n"
"\n"
"border-color: rgb(4, 35, 38);")
        formPrincipal.setTabShape(QtWidgets.QTabWidget.Rounded)
        formPrincipal.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
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
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(5, 379, 411, 16))
        self.label.setStyleSheet("font: 8pt \"Arial Rounded MT Bold\";\n"
"color: rgb(0, 0, 0);")
        self.label.setObjectName("label")
        formPrincipal.setCentralWidget(self.centralwidget)

        self.retranslateUi(formPrincipal)
        QtCore.QMetaObject.connectSlotsByName(formPrincipal)

    def retranslateUi(self, formPrincipal):
        _translate = QtCore.QCoreApplication.translate
        formPrincipal.setWindowTitle(_translate("formPrincipal", "Modulo Principal"))
        self.lbl_title.setText(_translate("formPrincipal", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#037f8c;\">BEM VINDO AO  APOSTADORPRO</span></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#037f8c;\">Torne sua possibilidades em jogos certeiros</span></p></body></html>"))
        self.btn_sair.setText(_translate("formPrincipal", "Sair"))
        self.btn_coletar.setText(_translate("formPrincipal", "Coletar Dados"))
        self.btn_visJogos.setText(_translate("formPrincipal", "Visualizar Jogos"))
        self.btn_visPossibilidades.setText(_translate("formPrincipal", " Possibilidades"))
        self.btn_simular.setText(_translate("formPrincipal", "Simular Aposta"))
        self.label.setText(_translate("formPrincipal", "Todos os direitos reservados ©  MaTTecnologia Aplicada 2022"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    formPrincipal = QtWidgets.QMainWindow()
    ui = Ui_formPrincipal()
    ui.setupUi(formPrincipal)
    formPrincipal.show()
    sys.exit(app.exec_())
