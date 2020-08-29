from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
from selenium.webdriver import ActionChains

class Test(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_HomeTest(self):
        #I check the homepage of the website
        self.browser.get('http://localhost:8000')

        self.assertIn("Aftaab's Website", self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn("Aftaab's Website", header_text)

    def test_CVPage(self):
        self.browser.get('http://localhost:8000/CV_list')

        self.assertIn("CV Builder", self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn("CV Builder", header_text)

    def test_addCV(self):
        self.browser.get('http://localhost:8000/CV/new')
        self.assertIn("CV Builder", self.browser.title)
        inputbox = self.browser.find_element_by_id('id_author')
        self.assertEqual(inputbox.get_attribute('name'), 'author')
        inputbox.send_keys("Test")
        inputbox = self.browser.find_element_by_id('id_Number')
        self.assertEqual(inputbox.get_attribute('name'), 'Number')
        inputbox.clear()
        inputbox.send_keys("0800001066")
        inputbox = self.browser.find_element_by_id('id_Email')
        self.assertEqual(inputbox.get_attribute('name'), 'Email')
        inputbox.clear()
        inputbox.send_keys("testCV@yahoo.com")
        inputbox = self.browser.find_element_by_id('id_Date_of_birth')
        self.assertEqual(inputbox.get_attribute('name'), 'Date_of_birth')
        inputbox.clear()
        inputbox.send_keys("09/11/1978")
        inputbox = self.browser.find_element_by_id('id_Personal_Profile')
        self.assertEqual(inputbox.get_attribute('name'), 'Personal_Profile')
        inputbox.send_keys("I am hardworking individual")
        inputbox = self.browser.find_element_by_id('id_Education')
        self.assertEqual(inputbox.get_attribute('name'), 'Education')
        inputbox.send_keys("Aston Universiity First year:2:1", Keys.ENTER, "A levels AAB")
        inputbox = self.browser.find_element_by_id('id_Employment_History')
        self.assertEqual(inputbox.get_attribute('name'), 'Employment_History')
        inputbox.send_keys("Worked for tesco")
        inputbox = self.browser.find_element_by_id('id_Achievements')
        self.assertEqual(inputbox.get_attribute('name'), 'Achievements')
        inputbox.send_keys("Won a competition")
        inputbox = self.browser.find_element_by_id('id_Interests')
        self.assertEqual(inputbox.get_attribute('name'), 'Interests')
        inputbox.send_keys("Like football")
        inputbox = self.browser.find_element_by_id('id_Skills')
        self.assertEqual(inputbox.get_attribute('name'), 'Skills')
        inputbox.send_keys("Like programming")
        inputbox = self.browser.find_element_by_id('id_References')
        self.assertEqual(inputbox.get_attribute('name'), 'References')
        inputbox.send_keys("jump")
        button = self.browser.find_element_by_css_selector('.save')
        button.click()
        time.sleep(5)

    def test_CVAdded(self):
        self.browser.get('http://localhost:8000/CV2_list')
        time.sleep(1)
        link = self.browser.find_element_by_partial_link_text("Test")
        link.click()
        time.sleep(3)

if __name__ == '__main__':
    unittest.main(warnings='ignore')
