import sys  

from PyQt6.QtWidgets import *  
from PyQt6.QtCore import *
from presentation.dialog.CreateDialog import CreateDialog
from presentation.dialog.UpdateDialog import UpdateDialog
from presentation.dialog.DeleteDialog import DeleteDialog
   
#Main Window  
class MainWindow( QWidget):  
    #singltone
    def __new__(cls, CustomerDAOFile):
        if not hasattr(cls, 'instance'):
            cls.instance = super(MainWindow, cls).__new__(cls)
        return cls.instance
    
    def __init__(self, CustomerDAOFile):  
        super().__init__()  
        self._CustomerDAOFile = CustomerDAOFile
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
        self.tableNew.setRowCount(len(self._CustomerDAOFile._customers_data))
        row = 0
        for e in self._CustomerDAOFile._customers_data:
            self.tableNew.setItem(row, 0, QTableWidgetItem(str(e['customerId'])))
            self.tableNew.setItem(row, 1, QTableWidgetItem(e['name']))
            self.tableNew.setItem(row, 2, QTableWidgetItem(e['surname']))
            self.tableNew.setItem(row, 3, QTableWidgetItem(str(e['address'])))
            row += 1
            
    def closeEvent(self, event):
        self._CustomerDAOFile.pickle_dump('customers.plk', self._CustomerDAOFile._customers_data)

'''    def deletedialog(self):
        text, ok = QInputDialog.getText(self, 'Deleting Customer', 'Customer ID')
        if ok:
            self.layout.setText(str(text))
''' 