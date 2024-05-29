'''
Created on 18. 10. 2023

@author: valic
'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

class TestSearchProducts(unittest.TestCase):

    def setUp(self):
        self.service = Service()
        self.options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=self.service, options=self.options)
        
        #self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.get("http://localhost:8089/design")
        
    def test_in_tacocloud_localhost(self):
        self.enterTacoLunchData()
        self.assertCurrentUrl("http://localhost:8089/orders/current")
        self.enterTacoOrderData()
        time.sleep(1)
        self.assertCurrentUrl("http://localhost:8089/")
        self.selectAllOrderPage()
        time.sleep(1)
        self.assertCurrentUrl("http://localhost:8089/allOrdersForm")
        self.assertAllOrdersData()
        
    def tearDown(self):
        self.driver.close()
        
    def enterTacoLunchData(self):
        self.driver.find_element(By.ID, 'ingredients1').click()
        self.driver.find_element(By.ID, 'ingredients2').click()
        self.driver.find_element(By.ID, 'ingredients4').click()
        input_text_fname = self.driver.find_element(By.ID, 'name')
        input_text_fname.send_keys("Lunch 2")
        button_ingredients = self.driver.find_element(By.TAG_NAME, 'button')
        button_ingredients.click()
        
    def assertCurrentUrl(self, required_url):
        current_url = self.driver.current_url
        assert(current_url == required_url)
        
    def enterTacoOrderData(self):
        self.driver.find_element(By.ID, 'clientDto.deliveryName').send_keys("Ludvík Valíček")
        self.driver.find_element(By.ID, 'clientDto.deliveryStreet').send_keys("Balabánova 4")
        self.driver.find_element(By.ID, 'clientDto.deliveryCity').send_keys("Praha")
        self.driver.find_element(By.ID, 'clientDto.deliveryState').send_keys("ČR")
        self.driver.find_element(By.ID, 'clientDto.deliveryZip').send_keys("18200")
        self.driver.find_element(By.ID, 'ccNumber').send_keys("12345678")
        self.driver.find_element(By.ID, 'ccExpiration').send_keys("12/23")
        self.driver.find_element(By.ID, 'ccVV').send_keys("789")
        self.driver.find_element(By.TAG_NAME, 'form').submit()
        
    def selectAllOrderPage(self):
        #driver.find_element(By.LINK_TEXT, 'All Orders Overview').click()
        self.driver.find_element(By.XPATH, '//a[contains(@href, "/allOrdersForm")]').click()
        
    def assertAllOrdersData(self):
        #mytable = driver.find_element(By.CLASS_NAME,"table-bordered")
        mytable = self.driver.find_element(By.TAG_NAME,"tbody")
        rows = mytable.find_elements(By.CSS_SELECTOR, 'tr')
        assert(rows[0].text == "{0}\n{1}\n{2}\n{3}\n{4}".format("Ludvík Valíček Balabánova 4 Praha ČR 18200 12345678 12/23",
                                                                "Lunch 2", "Flour Tortilla", "Corn Tortilla", "Carnitas"))
        for row in rows:
            for cell in row.find_elements(By.TAG_NAME, 'td'):
                print(cell.text)

        
if __name__ == "__main__":
    unittest.main()