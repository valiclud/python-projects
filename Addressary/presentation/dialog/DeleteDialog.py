'''
Created on 5. 7. 2023

@author: valic
'''
from presentation.dialog.AbstractDialog import AbstractDialog

class DeleteDialog(AbstractDialog):

    def __init__(self, app_self):
        self.app_self = app_self
        d = self.dialog("Deleting Customer")
        
        self.idLabel(d, 0)
        idLine = self.idLine(d, 0)
        
        b1 = self.okButton(d, -80)
        b1.clicked.connect(lambda:self.deleteaction(d, idLine))
        self.cancelButton(d, -80)
        d.exec()
        
    def deleteaction(self, d, customerId):
        self.app_self._CustomerDAOFile.deleteCustomer(customerId.text())
        self.app_self.refreshtable()
        d.close()
    