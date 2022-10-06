import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from formMain import *
from formPossibility import *

class ViewResult(QtWidgets.QWidget, Ui_formViewResult):
    def __init__(self):
        super().__init__()
        self.ui = Ui_formViewResult()
        self.ui.setupUi(self)
       

class ModuloPrincipal(QtWidgets.QWidget, Ui_formPrincipal):
    def __init__(self):
        super().__init__()
        self.ui = Ui_formPrincipal()
        self.ui.setupUi(self)
        

        self.viewResult = ViewResult()
        self.ui.btn_visPossibilidades.clicked.connect(self.viewTable)

    def viewTable(self):
        self.viewResult.show()
        self.hide()
        
    
    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    formPrincipal = QtWidgets.QMainWindow()
    ui = Ui_formPrincipal()
    ui.setupUi(formPrincipal)
    formPrincipal.show()
    sys.exit(app.exec_())