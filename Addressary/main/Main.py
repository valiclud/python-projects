'''
Created on 3. 7. 2023

@author: valic
'''

import sys

from PyQt6.QtWidgets import QApplication
#need to leave as line 25 or 26 
from integration.CustomerDAOFile import CustomerDAOFile
from integration.CustomerDAODatabase import CustomerDAODatabase
from presentation.MainWindow import MainWindow

class Main():

    def __init__(self):
        pass
        
if __name__ == '__main__':  
  
    # creating the pyqt5 application      
    base = QApplication(sys.argv)  
  
    #daoname = 'CustomerDAOFile'
    daoname = 'CustomerDAOFile'
    if (daoname == 'CustomerDAODatabase'):
        dao = globals()['CustomerDAODatabase']
    else :
        dao = globals()['CustomerDAOFile']
  
    MainWindow(dao())  
  
    sys.exit(base.exec())          