from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.path = 'E:\anaconda\geckodriver.exe' #import
        self.brower = webdriver.Firefox()
        
    def tearDown(self):
        self.brower.quit()
    
    def test_can_start_a_list_and_retrieve_it_later(self):
        #Edith has heard about a cool new onlin to-do app. She goes to check out its homepage
        self.brower.get('http://localhost:8000')

        #She notices the page title and header mention to-do lists
        self.assertIn('To-Do',self.brower.title)
        self.fail('Finish the test!')

        #She is invited to enter a to-do item straight away
        #She blabla

if __name__ == '__main__':
    unittest.main(warnings='ignore')