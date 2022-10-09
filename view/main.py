
import sys
import os
import sqlite3
from PyQt5.QtCore import QPropertyAnimation
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import Qt
from PyQt5.QtGui import *
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from ui_main import *



    
class ModuloPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Main()
        self.ui.setupUi(self)
        

        ################################################
        #Toggle Buton
        self.ui.btn_menu.clicked.connect(self.side_menu)
        
        
        
    ###################################################   
    #Animação do menu
 
    def side_menu(self):
        width = self.ui.frame_side.width()
        btn_width = self.ui.frame_btn_menu.width()

        if width == 0:
            new_width = 290
    
        else:
            new_width = 0
   
        self.animation = QtCore.QPropertyAnimation(self.ui.frame_side, b"maximumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(new_width)
        self.animation.setEasingCurve(QtCore.QEasingCurve.Type(5))
        self.animation.start()
    
    
    ###################################################   
    #Paginas do sistema
        self.ui.btn_coletar.clicked.connect(lambda: self.ui.pages.setCurrentWidget(self.ui.page_home))  
        
    
        
           
    
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = ModuloPrincipal()
    w.show()
    sys.exit(app.exec_())