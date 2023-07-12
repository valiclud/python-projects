'''
Created on 12. 7. 2023

@author: valic
'''
import unittest

from integration.CustomerDAOFile import CustomerDAOFile

class TestCustomerDeleteDAOFile(unittest.TestCase):


    def setUp(self):
        self.dao = CustomerDAOFile()
        self.dao.createCustomer('a', 'b', 'c')

    def tearDown(self):
        self.dao.close()

    def testCustomerDeleteDAOFile(self):
        self.dao = CustomerDAOFile()
        customerId = self.dao.findLastCustomerId()
        self.dao.deleteCustomer(customerId.customerId)
        customer = self.dao.findByCustomerId(customerId.customerId)
        assert None == customer

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()