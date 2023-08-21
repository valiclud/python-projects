'''
Created on 21. 8. 2023

@author: valic
'''
from PyQt6.QtWidgets import QWidget, QPushButton, QGridLayout, QFormLayout, QVBoxLayout, QComboBox, QLabel, QLineEdit, QTableWidget, QTableWidgetItem
from PyQt6.QtCore import Qt

from pyqtgraph import PlotWidget, plot

import matplotlib.pyplot as plt
import pyqtgraph as pg

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Rocket Flight Simulation'  
        # Setting the Position  
        self.left = 0  
        self.top = 0  
        self.width = 500  
        self.height = 450
        self.setWindowTitle(self.title)  
        self.setGeometry(self.left, self.top, self.width, self.height)  
        self.buttonNew = QPushButton('Calculate Flight')
        
        self.createTypeCombo()
        self.createNameRocketCombo()
        self.createWindDirCombo()
        self.createWindLine()
        self.createRocketSpeedLine()
        self.createRocketDistanceLine()
        
        self.typeLabel = QLabel(self)
        self.typeLabel.setText('Rocket Type:')
        self.rocketNameLabel = QLabel(self)
        self.rocketNameLabel.setText('Rocket Name:')
        self.windLabel = QLabel(self)
        self.windLabel.setText('Wind Direction:')
        
        # Adding Widgets  
        self.mainLayout = QVBoxLayout()  
        
        self.formLayout = QFormLayout()
        self.formLayout.addWidget(self.typeLabel)
        self.formLayout.addWidget(self.typeCombo)
        self.formLayout.addWidget(self.rocketNameLabel)
        self.formLayout.addWidget(self.nameRocketCombo)
        self.formLayout.addWidget(self.rocketSpeedLabel)
        self.formLayout.addWidget(self.rocketSpeedLine)
        self.formLayout.addWidget(self.rocketDistLabel)
        self.formLayout.addWidget(self.rocketDistLine)
        self.formLayout.addWidget(self.windLabel)
        self.formLayout.addWidget(self.windDirCombo)
        self.formLayout.addWidget(self.windSpeedLabel)
        self.formLayout.addWidget(self.windLine)
        self.formLayout.addWidget(self.buttonNew)
        
        self.win = pg.GraphicsLayoutWidget()
        self.view = self.win.addViewBox()
        self.graph_item = pg.GraphItem()
        self.view.addItem(self.graph_item)
        self.graphWidget = pg.PlotWidget()
        height = [1,2,3,4,5,6,7,8,9,10]
        time = [0,25,35,43,43,43,43,43,43,43]
        self.graphWidget.plot(height, time)
        
        self.mainLayout.addLayout(self.formLayout)
        self.mainLayout.addWidget(self.graphWidget)
        self.setLayout(self.mainLayout)  

    def createTypeCombo(self):
        self.typeCombo = QComboBox(self)
        self.typeCombo.addItem("Ground - Ground")
        self.typeCombo.addItem("Air - Ground")
        self.typeCombo.addItem("Air - Air")
        
    def createNameRocketCombo(self):
        self.nameRocketCombo = QComboBox(self)
        self.nameRocketCombo.addItem("Kinzhal")
        self.nameRocketCombo.addItem("Zircon")
        self.nameRocketCombo.addItem("Avantgard")
        
    def createWindDirCombo(self):
        self.windDirCombo = QComboBox(self)
        self.windDirCombo.addItem("Back")
        self.windDirCombo.addItem("Front")
        self.windDirCombo.addItem("Front- Left Side")
    
    def createWindLine(self):
        self.windSpeedLabel = QLabel(self)
        self.windSpeedLabel.setText('Wind Speed [m/s]:')
        self.windLine = QLineEdit(self)
        self.windLine.move(80, 20)
        self.windLine.resize(200, 32)
        self.windSpeedLabel.move(20, 20)  
        
    def createRocketSpeedLine(self):
        self.rocketSpeedLabel = QLabel(self)
        self.rocketSpeedLabel.setText('Rocket Speed [m/s]:')
        self.rocketSpeedLine = QLineEdit(self)
        self.rocketSpeedLine.move(80, 20)
        self.rocketSpeedLine.resize(200, 32)
        self.rocketSpeedLabel.move(20, 20) 
        
    def createRocketDistanceLine(self):
        self.rocketDistLabel = QLabel(self)
        self.rocketDistLabel.setText('Rocket Distance [km]:')
        self.rocketDistLine = QLineEdit(self)
        self.rocketDistLine.move(80, 20)
        self.rocketDistLine.resize(200, 32)
        self.rocketDistLabel.move(20, 20) 
        
    def closeEvent(self, event):
        pass