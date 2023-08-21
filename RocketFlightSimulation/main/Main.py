'''
Created on 21. 8. 2023

@author: valic
'''
import sys

from PyQt6.QtWidgets import QApplication
from presentation.MainWindow import MainWindow

class Main:

    def __init__(self):
        pass
 
if __name__ == '__main__':
    # creating the pyqt5 application      
    base = QApplication(sys.argv) 
    
    mainwin = MainWindow()
    mainwin.show()  
  
    sys.exit(base.exec())       