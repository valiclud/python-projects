'''
Created on 7. 7. 2023

@author: valic
'''
import mysql.connector
from typing import Tuple

from integration.DAOInterface import DAOInterface
from core.CustomerId import CustomerId

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
     
    def createCustomer(self, name: str, surname: str, address: str) -> None:
        mycursor = self.mydb.cursor()
        sql = "INSERT INTO Addressary (Forname, Surname, Address) VALUES (%s, %s, %s)"
        val = (name, surname, address)
        mycursor.execute(sql, val)
        
        self.mydb.commit()
        
    def updateCustomer(self, idCustomer: int, name: str, surname: str, address: str) -> None:
        mycursor = self.mydb.cursor()
        sql = "UPDATE Addressary SET Forname = %s, Surname = %s, address = %s WHERE id_addressary = %s"
        val = (name, surname, address, int(idCustomer))
        mycursor.execute(sql, val)
        self.mydb.commit()

    def deleteCustomer(self, customerId: CustomerId) -> None:
        mycursor = self.mydb.cursor()
        sql = "DELETE FROM Addressary WHERE id_addressary = '%d'" % (int(customerId))
        mycursor.execute(sql)
        self.mydb.commit()
    
    def getAllCustomers(self)-> [{'customerId': CustomerId, 'name': str, 'surname': str, 'address': str}]:
        mycursor = self.mydb.cursor()
        mycursor.execute("SELECT * FROM ADDRESSARY")
        result = mycursor.fetchall()
        return self.convertToDictionaryList(result)
    
    def findByCustomerId(self, customerId: int) -> {'customerId': CustomerId, 'name': str, 'surname': str, 'address': str}:
        mycursor = self.mydb.cursor()
        sql = "SELECT * FROM Addressary WHERE id_addressary = '%d'" % (int(customerId))
        mycursor.execute(sql)
        result = mycursor.fetchone()
        return result
    
    def findLastCustomerId(self)-> []:
        mycursor = self.mydb.cursor()
        mycursor.execute("SELECT LAST_INSERT_ID()")
        result = mycursor.fetchone()
        return result
    
    def close(self) -> None:
        self.mydb.close()
        
    def convertToDictionaryList(self, customers_data: Tuple[int, str, str, str]) -> [{'customerId': CustomerId, 'name': str, 'surname': str, 'address': str}]:
        diction = []
        for l in customers_data:
            dctr = {}   
            dctr['customerId'] = CustomerId(int(l[0]))
            dctr['name'] = l[1]
            dctr['surname'] = l[2]
            dctr['address'] = l[3]
            diction.append(dctr)
        return diction