'''
Created on 10. 7. 2023

@author: valic
'''
import unittest
import os

from integration.CustomerDAOFile import CustomerDAOFile

class TestCustomerDAOFile(unittest.TestCase):

    
    def setUp(self):
        print("Current working directory:", os.getcwd())
        dao = CustomerDAOFile()
        dao.createCustomer('a', 'b', 'c')
        dao.close()

    def tearDown(self):
        dao = CustomerDAOFile()
        customerId = dao.findLastCustomerId()
        dao.deleteCustomer(customerId.customerId)
        dao.close()

    def testCustomerDAOFile(self):
        dao = CustomerDAOFile()
        customerIdLast = dao.findLastCustomerId()
        customer = dao.findByCustomerId(customerIdLast.customerId)
        assert customerIdLast == customer.get('customerId')
        dao.close()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
