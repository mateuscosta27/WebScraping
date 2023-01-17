import sys
from Views.StringConnection import *
from Data.ConfigConnection import *
from Data.ApplicationContext import *
import sqlite3

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog




class ConfConnection(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_StringConnection()
        self.ui.setupUi(self)

        self.config = ConfigConnection()

        ###Botões###
        ##definindo botão invisivel##
        self.ui.btn_testConnection.setVisible(False)

        ##funções botões###
        self.ui.btn_exit.clicked.connect(self.exit_system)
        self.ui.btn_testConnection.clicked.connect(self.test_connection_status)
        self.ui.btn_instalation.clicked.connect(self.localdb)


    def localdb(self):
        self.config.selectDir()
        self.ui.le_localDb.setText(self.config.pathConnection)
        self.ui.btn_instalation.setVisible(False)
        
        check_le = self.ui.le_localDb

        if check_le!='':

            self.ui.btn_testConnection.setGeometry(460,41,150,45)
            self.ui.btn_testConnection.setVisible(True)
        self.ui.le_localDb.setDisabled(True)

   

    def test_connection_status(self):

        try:
            icon_Connect = QIcon()
            icon_Connect.addFile(u"../src/icon_connectDB.svg", QSize(), QIcon.Normal, QIcon.Off)
            self.ui.btn_statusConection.setIcon(icon_Connect)
            icon_check = QIcon()
            icon_check.addFile(u"../src/icon_check.svg", QSize(), QIcon.Normal, QIcon.Off)
            self.ui.btn_testConnection.setIcon(icon_check)
            self.ui.btn_testConnection.setText("Conectado")
        except sqlite3.Error as e:
            icon_diconnect = QIcon()
            icon_diconnect.addFile(u"./src/icon_disconnectDB.svg", QSize(), QIcon.Normal, QIcon.Off)
            self.ui.btn_statusConection.setIcon(icon_diconnect)
            icon_uncheck = QIcon()
            icon_uncheck.addFile(u"./src/icon_uncheck.svg", QSize(), QIcon.Normal, QIcon.Off)
            self.ui.btn_testConnection.setIcon(icon_check)
        self.config.create_directory()
        self.context_connection()


    def context_connection(self):
        conn = ApplicationContext()
        conn.connect()
    def exit_system(self):
        self.close()
       







  














if __name__ =="__main__":
    app = QApplication(sys.argv)
    window = ConfConnection()
    window.show()
    sys.exit(app.exec())