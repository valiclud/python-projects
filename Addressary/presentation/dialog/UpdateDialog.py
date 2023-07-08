'''
Created on 5. 7. 2023

@author: valic
'''
from presentation.dialog.AbstractDialog import AbstractDialog

class UpdateDialog(AbstractDialog):

    def __init__(self, app_self):
        self.app_self = app_self
        d = self.dialog("Updating Customer")
        
        self.idLabel(d, 0)
        idLine = self.idLine(d, 0)
        self.nameLabel(d, 30)
        nameLine = self.nameLine(d, 30)
        self.surnameLabel(d, 30)
        surnameLine = self.nameLine(d, 60)
        self.addressLabel(d, 30)
        addressLine = self.nameLine(d, 90)
        
        b1 = self.okButton(d, 30)
        b1.clicked.connect(lambda:self.saveaction(d, idLine, nameLine, surnameLine, addressLine))
        self.cancelButton(d, 30)
        d.exec()
        
    def saveaction(self, d, idLine, name, surname, address):
        if (self.app_self._DAOInterface.findByCustomerId(int(idLine.text())) == None):
            self.errordialog('CustomerId: %s does not exist' %idLine.text())
            return
        self.app_self._DAOInterface.updateCustomer(idLine.text(), name.text(), surname.text(), address.text())
        self.app_self.refreshtable()
        d.close()
