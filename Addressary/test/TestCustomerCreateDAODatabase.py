'''
Created on 11. 7. 2023

@author: valic
'''
import unittest

from integration.CustomerDAODatabase import CustomerDAODatabase

class TestCustomerCreateDAODatabase(unittest.TestCase):


    def setUp(self):
        self.dao = CustomerDAODatabase()
        self.dao.createCustomer('a', 'b', 'c')

    def tearDown(self):
        customerId = self.dao.findLastCustomerId()
        self.dao.deleteCustomer(customerId[0])
        self.dao.close()

    def testCustomerCreateDAODatabase(self):
        customerIdLast = self.dao.findLastCustomerId()
        customer = self.dao.findByCustomerId(customerIdLast[0])
        assert customerIdLast[0] == customer[0]
        assert "a" == customer[1]
        assert "b" == customer[2]
        assert "c" == customer[3]

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()