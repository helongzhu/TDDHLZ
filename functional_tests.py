from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.path = 'E:\anaconda\geckodriver.exe' #import
        self.brower = webdriver.Firefox()
        
    def tearDown(self):
        self.brower.quit() #close the webpage after functional test
    
    def test_can_start_a_list_and_retrieve_it_later(self):
        #Edith has heard about a cool new onlin to-do app. She goes to check out its homepage
        self.brower.get('http://localhost:9000')

        #She notices the page title and header mention to-do lists
        self.assertIn('To-Do',self.brower.title)
        header_text = self.brower.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        #She is invited to enter a to-do item straight away
        inputbox = self.brower.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        #She types "Buy peacock feathers" into a text box(Edith's hobby
        #is tying fly-fishing lures)
        inputbox.send_keys('Buy peacock feathers')

        #When she hits enter, the page updates, and now the page lists
        #"1:Buy peacock feathers" as an item in a to-do list table
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.brower.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1:Buy peacock feathers', [row.text for row in rows])

        self.assertIn('2:Use peacock feathers to make a fly', [row.text for row in rows])

        #There is still a text box inviting her to add another item.
        #She enters "Use peacock feathers to make a fly"
        #(Edith is very methodical)
        self.fail('Finish the test!')

        #She is invited to enter a to-do item straight away
        #She blabla

if __name__ == '__main__':
    unittest.main(warnings='ignore')