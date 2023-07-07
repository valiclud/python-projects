'''
Created on 3. 7. 2023

@author: valic
'''

import sys
import mysql.connector

from PyQt6.QtWidgets import QApplication 
from integration.CustomerDAOFile import CustomerDAOFile
from presentation.MainWindow import MainWindow

class Main():

    def __init__(self):
        pass
        
        
if __name__ == '__main__':  
  
    # Creating connection object
    mydb = mysql.connector.connect(
        host = "localhost",
        port = 3304,
        user = "root",
        password = "lukasa"
    )
 
    # Printing the connection object
    print(mydb)
  
  
  
  
    # creating the pyqt5 application      
    base = QApplication(sys.argv)  
  
    classname=globals()['CustomerDAOFile']
    dao = classname()
    #dao = CustomerDAOFile()
    window = MainWindow(dao)  
  
    # starting the application   
    sys.exit(base.exec())          