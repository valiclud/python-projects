'''
Created on 7. 7. 2023

@author: valic
'''
import mysql.connector
from integration.DAOInterface import DAOInterface

class CustomerDAODatabase(DAOInterface):

    def __init__(self):
        # Creating connection object
        self.mydb = mysql.connector.connect(
            host = "localhost",
            port = 3304,
            user = "root",
            password = "lukasa",
            database= "addressary"
        )
     
    def createCustomer(self, name, surname, address):
        mycursor = self.mydb.cursor()
        sql = "INSERT INTO Addressary (Forname, Surname, Address) VALUES (%s, %s, %s)"
        val = (name, surname, address)
        mycursor.execute(sql, val)
        
        self.mydb.commit()
        
    def updateCustomer(self, customerId, name, surname, address):
        mycursor = self.mydb.cursor()
        sql = "UPDATE Addressary SET Forname = %s, Surname = %s, address = %s WHERE id_addressary = %s"
        val = (name, surname, address, int(customerId))
        mycursor.execute(sql, val)
        self.mydb.commit()

    def deleteCustomer(self, CustomerId):
        mycursor = self.mydb.cursor()
        sql = "DELETE FROM Addressary WHERE id_addressary = '%d'" % (int(CustomerId))
        mycursor.execute(sql)
        self.mydb.commit()
    
    def getAllCustomers(self):
        mycursor = self.mydb.cursor()
        mycursor.execute("SELECT * FROM ADDRESSARY")
        result = mycursor.fetchall()
        return self.convertToDictionaryList(result)
    
    def findByCustomerId(self, customerId):
        mycursor = self.mydb.cursor()
        sql = "SELECT id_addressary FROM Addressary WHERE id_addressary = '%d'" % (int(customerId))
        mycursor.execute(sql)
        result = mycursor.fetchone()
        return result
    
    def close(self):
        self.mydb.close()
        
    def convertToDictionaryList(self, customers_data):
        diction = []
        for l in customers_data:
            dctr = {}   
            dctr['customerId'] = l[0]
            dctr['name'] = l[1]
            dctr['surname'] = l[2]
            dctr['address'] = l[3]
            diction.append(dctr)
        return diction