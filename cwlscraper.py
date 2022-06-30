from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException 
from selenium import webdriver 
from email.message import EmailMessage
import smtplib 
import yaml
import time 
import datetime 
import yaml 


class CWLscraper(object): 
    def __init__(self): 
        with open('config.yaml') as file: 
            try: 
                self.props = yaml.safe_load(file)
            except yaml.YAMLError as e: 
                print('ERROR: %s' % e)
        # with webdriver.Chrome(executable_path=self.props['driver']['exec_path']) as web_drive:
        #     self.driver = web_drive 
        #     self.driver = webdriver.Chrome(executable_path=self.props['driver']['exec_path'])
        #     self.driver.get(self.props['driver']['scrape_dest'])
        #     self.driver.set_window_size(1080, 800)
        #     print('CWLscraper object created')
        try: 
            self.driver = webdriver.Chrome(executable_path=self.props['driver']['exec_path'])
            self.driver.get(self.props['driver']['scrape_dest'])
            self.driver.set_window_size(1080, 800)
            print('CWLscraper object created')
        except Exception as e: 
            print('ERROR: %s' % e)

    def cwl_login(self): 
        print('Navigating to CWL Login form...')
        self.driver.find_element(By.XPATH, "//input[@name = 'IMGSUBMIT']").click()
        print('Current Page: %s' % self.driver.title) 

        form = self.driver.find_element(By.XPATH, "//form[@id = 'fm1']")
        print('Inputting login credentials')
        form.find_element(By.NAME, 'username').send_keys(scraper.props['cwl']['username'])
        form.find_element(By.NAME, 'password').send_keys(scraper.props['cwl']['password'])

        print('Submitting Form')
        scraper.driver.find_element(By.XPATH, "//input[@type = 'submit']").click()

        print('Current Page: %s' % self.driver.title)

        # need to change this assertion for invalid logins 
        if 'Your account is inactive' in self.driver.title: 
            print('ERROR: Failed to login. Check your CWL credentials')
            return False 
        else: 
            print('Login successful') 
            return True 

    
    # def __enter__(self): 
    #     print('Enter') 

    # def __exit__(self, exc_type, exc_val, exc_tb): 
    #     print('Exit')
    #     self.driver.quit() 


if __name__ == '__main__': 
    scraper = CWLscraper() 
    scraper.cwl_login()
    scraper.driver.close()
    # with CWLscraper() as scraper: 
    #     scraper.cwl_login()
    