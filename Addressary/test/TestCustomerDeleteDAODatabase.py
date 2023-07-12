'''
Created on 12. 7. 2023

@author: valic
'''
import unittest

from integration.CustomerDAODatabase import CustomerDAODatabase

class Test(unittest.TestCase):


    def setUp(self):
        self.dao = CustomerDAODatabase()
        self.dao.createCustomer('a', 'b', 'c')


    def tearDown(self):
        self.dao.close()


    def testName(self):
        customerId = self.dao.findLastCustomerId()
        self.dao.deleteCustomer(customerId[0])
        customer = self.dao.findByCustomerId(customerId[0])
        assert None == customer


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()