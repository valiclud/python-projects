'''
Created on 5. 7. 2023

@author: valic
'''
from presentation.dialog.AbstractDialog import AbstractDialog

class CreateDialog(AbstractDialog):

    def __init__(self, app_self):
        self.app_self = app_self
        d = self.dialog("Creating New Customer")
        
        self.nameLabel(d, 0)
        nameLine = self.nameLine(d, 0)
        self.surnameLabel(d, 0)
        surnameLine = self.nameLine(d, 30)
        self.addressLabel(d, 0)
        addressLine = self.nameLine(d, 60)
        
        b1 = self.okButton(d, 0)
        b1.clicked.connect(lambda:self.saveaction(d, nameLine, surnameLine, addressLine))
        self.cancelButton(d, 0)
        d.exec()
        
    def saveaction(self, d, name, surname, address):
        self.app_self._CustomerDAOFile.createCustomer(name.text(), surname.text(), address.text())
        self.app_self.refreshtable()
        d.close()
