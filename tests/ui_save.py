import sys
from PyQt5.QtWidgets import QApplication, QFileDialog

app = QApplication(sys.argv)

selected_directory = QFileDialog.getExistingDirectory(directory="/C:/tmp")
print(selected_directory)



