import sys  

from PyQt6.QtWidgets import *  
from PyQt6.QtCore import *
from presentation.dialog.CreateDialog import CreateDialog
from presentation.dialog.UpdateDialog import UpdateDialog
from presentation.dialog.DeleteDialog import DeleteDialog

from integration.CustomerDAOFile import CustomerDAOFile
from integration.CustomerDAODatabase import CustomerDAODatabase
from integration.DAOInterface import DAOInterface

   
#Main Window  
class MainWindow( QWidget):  
    
    def __init__(self, DAOInterface):  
        super().__init__()  
        self._DAOInterface = DAOInterface
        self.title = 'Addressary'  
        # Setting the Position  
        self.left = 0  
        self.top = 0  
        self.width = 500  
        self.height = 350  
  
        self.setWindowTitle(self.title)  
        self.setGeometry(self.left, self.top, self.width, self.height)  
          
        # introducing a table  
        self.creatingTable()
        
        # introducing a button
        self.buttonNew = QPushButton('Create New Customer')
        self.buttonNew.clicked.connect(lambda:CreateDialog(self))
        self.buttonDelete = QPushButton('Delete Customer')
        self.buttonDelete.clicked.connect(lambda:DeleteDialog(self))
        self.buttonUpdate = QPushButton('Update Customer') 
        self.buttonUpdate.clicked.connect(lambda:UpdateDialog(self))
  
        # Adding Widgets  
        self.layout = QVBoxLayout()  
        self.layout.addWidget(self.tableNew) ;
        self.layout.addWidget(self.buttonNew)
        self.layout.addWidget(self.buttonUpdate)
        self.layout.addWidget(self.buttonDelete)  
        self.setLayout(self.layout)  
  
        # Displaying the window  
        self.show()  
  
    #Creating the table  
    def creatingTable(self):  
        self.tableNew = QTableWidget()  
        self.tableNew.setColumnCount(4)  
        self.tableNew.setHorizontalHeaderLabels(['Id', 'Name', 'Surname', 'Address'])
        self.tableNew.horizontalHeader().setStretchLastSection(True)  
        self.tableNew.setSortingEnabled(True)
        self.tableNew.sortByColumn(0, Qt.SortOrder.AscendingOrder)
        self.refreshtable()
        
    def refreshtable(self):
        self.tableNew.setRowCount(len(list(self._DAOInterface.getAllCustomers())))
        row = 0
        for e in self._DAOInterface.getAllCustomers():
            self.tableNew.setItem(row, 0, QTableWidgetItem(str(e['customerId'])))
            self.tableNew.setItem(row, 1, QTableWidgetItem(e['name']))
            self.tableNew.setItem(row, 2, QTableWidgetItem(e['surname']))
            self.tableNew.setItem(row, 3, QTableWidgetItem(str(e['address'])))
            row += 1
            
    def closeEvent(self, event):
        self._DAOInterface.close()
