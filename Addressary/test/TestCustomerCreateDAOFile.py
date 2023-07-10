'''
Created on 10. 7. 2023

@author: valic
'''
import unittest
import os

from integration.CustomerDAOFile import CustomerDAOFile

class TestCustomerCreateDAOFile(unittest.TestCase):

    
    def setUp(self):
        dao = CustomerDAOFile()
        dao.createCustomer('a', 'b', 'c')
        dao.close()

    def tearDown(self):
        dao = CustomerDAOFile()
        customerId = dao.findLastCustomerId()
        dao.deleteCustomer(customerId.customerId)
        dao.close()

    def testCustomerCreateDAOFile(self):
        dao = CustomerDAOFile()
        customerIdLast = dao.findLastCustomerId()
        customer = dao.findByCustomerId(customerIdLast.customerId)
        assert customerIdLast == customer.get('customerId')
        assert "a" == customer.get('name')
        assert "b" == customer.get('surname')
        assert "c" == customer.get('address')
        dao.close()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
