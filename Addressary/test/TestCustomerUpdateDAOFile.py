'''
Created on 10. 7. 2023

@author: valic
'''
import unittest

from integration.CustomerDAOFile import CustomerDAOFile

class TestCustomerUpdateDAOFile(unittest.TestCase):


    def setUp(self):
        dao = CustomerDAOFile()
        dao.createCustomer('a', 'b', 'c')
        dao.close()

    def tearDown(self):
        dao = CustomerDAOFile()
        customerId = dao.findLastCustomerId()
        dao.deleteCustomer(customerId.customerId)
        dao.close()

    def testCustomerUpdateDAOFile(self):
        dao = CustomerDAOFile()
        customerIdLast = dao.findLastCustomerId()
        dao.updateCustomer(customerIdLast.customerId, 'd', 'e', 'f')
        customer = dao.findByCustomerId(customerIdLast.customerId)
        assert customerIdLast == customer.get('customerId')
        assert "d" == customer.get('name')
        assert "e" == customer.get('surname')
        assert "f" == customer.get('address')
        dao.close()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()