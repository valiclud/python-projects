'''
Created on 5. 7. 2023

@author: valic
'''
import abc
from PyQt6.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QMessageBox 

class AbstractDialog(abc.ABC):
    
    @abc.abstractmethod
    def __init__(self, app_self):
        self.app_self = app_self
    
    def dialog(self, name):
        d = QDialog()
        d.setWindowTitle(name)
        return d
    
    def idLabel(self, d, shift):
        idLabel = QLabel(d)
        idLabel.setText('Customer Id:')
        idLabel.move(20, 20 + shift)
 
    def idLine(self, d, shift):
        idLine = QLineEdit(d)
        idLine.move(100, 20 + shift)
        idLine.resize(100, 24)
        return idLine
    
    def nameLabel(self, d, shift):
        nameLabel = QLabel(d)
        nameLabel.setText('Name:')
        nameLabel.move(20, 20 + shift)
        
    def nameLine(self, d, shift):
        nameLine = QLineEdit(d)
        nameLine.move(80, 20 + shift)
        nameLine.resize(200, 24)
        return nameLine
    
    def surnameLabel(self, d, shift):
        surnameLabel = QLabel(d)
        surnameLabel.setText('Surname:')
        surnameLabel.move(20, 50 + shift)
        
    def addressLabel(self, d, shift):
        addressLabel = QLabel(d)
        addressLabel.setText('Address:')
        addressLabel.move(20, 80 + shift)
    
    def okButton(self, d, shift):
        okButton = QPushButton("Ok",d)
        okButton.move(50,130 + shift)
        okButton.show()
        return okButton
    
    def cancelButton(self, d, shift):
        cancelButton = QPushButton("Cancel",d)
        cancelButton.move(200,130 + shift)
        cancelButton.show()
        cancelButton.clicked.connect(lambda:self.closeaction(d))
        return cancelButton
    
    def errordialog(self, errortext):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.setWindowTitle("Error Window")
        msg.setText(errortext)
        msg.exec() 
        
    def closeaction(self, d): 
        d.close()