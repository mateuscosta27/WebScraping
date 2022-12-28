
import sys,os
from time import sleep
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QFileDialog, QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(411, 120)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_content = QtWidgets.QFrame(self.centralwidget)
        self.frame_content.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_content.setObjectName("frame_content")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_content)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_select_directory = QtWidgets.QPushButton(self.frame_content)
        self.btn_select_directory.setMinimumSize(QtCore.QSize(150, 30))
        self.btn_select_directory.setMaximumSize(QtCore.QSize(150, 30))
        self.btn_select_directory.setObjectName("btn_select_directory")
        self.gridLayout.addWidget(self.btn_select_directory, 0, 2, 1, 1)
        self.le_directory = QtWidgets.QLineEdit(self.frame_content)
        self.le_directory.setReadOnly(True)
        self.le_directory.setObjectName("le_directory")
        self.gridLayout.addWidget(self.le_directory, 0, 0, 1, 2)
        self.btn_create_folder = QtWidgets.QPushButton(self.frame_content)
        self.btn_create_folder.setMinimumSize(QtCore.QSize(100, 30))
        self.btn_create_folder.setMaximumSize(QtCore.QSize(100, 30))
        self.btn_create_folder.setObjectName("btn_create_folder")
        self.gridLayout.addWidget(self.btn_create_folder, 1, 0, 1, 1)
        self.btn_exit = QtWidgets.QPushButton(self.frame_content)
        self.btn_exit.setMinimumSize(QtCore.QSize(80, 30))
        self.btn_exit.setMaximumSize(QtCore.QSize(80, 30))
        self.btn_exit.setObjectName("btn_exit")
        self.gridLayout.addWidget(self.btn_exit, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.frame_content)
        self.fram_version = QtWidgets.QFrame(self.centralwidget)
        self.fram_version.setMinimumSize(QtCore.QSize(0, 30))
        self.fram_version.setMaximumSize(QtCore.QSize(16777215, 30))
        self.fram_version.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fram_version.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fram_version.setObjectName("fram_version")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.fram_version)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_version = QtWidgets.QLabel(self.fram_version)
        self.btn_version.setMinimumSize(QtCore.QSize(20, 20))
        self.btn_version.setMaximumSize(QtCore.QSize(200, 20))
        self.btn_version.setObjectName("btn_version")
        self.horizontalLayout.addWidget(self.btn_version)
        self.verticalLayout.addWidget(self.fram_version)
        MainWindow.setCentralWidget(self.centralwidget)


        ###Botões###
        self.btn_select_directory.clicked.connect(self.select_directory)
        self.btn_create_folder.clicked.connect(self.create_folders)
        self.btn_exit.clicked.connect(self.exit_system)

        
  
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Configuração"))
        self.btn_select_directory.setText(_translate("MainWindow", "Selecionar Diretorio"))
        self.btn_create_folder.setText(_translate("MainWindow", "Criar Pastas"))
        self.btn_exit.setText(_translate("MainWindow", "Sair"))
        self.btn_version.setText(_translate("MainWindow", "Versão 0.0.1 SNAPSHOT"))



    def select_directory(self):
        selected_directory = QFileDialog.getExistingDirectory(directory="C:/")
        self.select = selected_directory
        self.le_directory.setText(selected_directory)

    def disable_button(self):
        self.btn_select_directory.setEnabled(False)
        self.btn_create_folder.setEnabled(False)

    def create_folders(self):

        if self.le_directory.text() == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Preencha o caminho do diretorio")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()
        else:
            
            self.disable_button()
            diretorios = [self.select+'/tmp/Arquivos',self.select+'/tmp/Bancos',self.select+'/tmp/Driver']
            for diretorio in diretorios:
                if not os.path.exists(diretorio):
                    os.makedirs(diretorio)
                    sleep(0.5)
                    self.le_directory.setText(diretorio)
                    print(diretorio)
                else:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Question)
                    msg.setText(f"O diretorio já {diretorio}  existe! Deseja continuar?")

                    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

                    retval = msg.exec_()

            create_folder = QMessageBox()
            create_folder.setWindowTitle("Sucesso!")
            create_folder.setIcon(QMessageBox.Information)
            create_folder.setText("Pastas criadas com sucesso!")
            create_folder.setStandardButtons(QMessageBox.Ok)
            create_folder.exec_()


    def exit_system(self):
        exit()   

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
