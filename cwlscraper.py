from selenium.webdriver.common.by import By
from selenium.common import exceptions 
from selenium import webdriver 
from email.message import EmailMessage
import smtplib 
import yaml
import time 
import datetime 
import yaml

SSL_PORT = 587

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
            self.start_title = self.driver.title
            print(self.start_title)
        except exceptions as e: 
            print('ERROR: %s' % e)


    def cwl_login(self): 
        # Add assertion to check if already logged in
        try: 
            print('Navigating to CWL Login form...')
            self.driver.find_element(By.XPATH, "//input[@name = 'IMGSUBMIT']").click()
            print('Current Page: %s' % self.driver.title) 

            form = self.driver.find_element(By.XPATH, "//form[@id = 'fm1']")
            print('Inputting login credentials')
            form.find_element(By.NAME, 'username').send_keys(self.props['cwl']['username'])
            form.find_element(By.NAME, 'password').send_keys(self.props['cwl']['password'])

            print('Submitting Form')
            self.driver.find_element(By.XPATH, "//input[@type = 'submit']").click()
            print('Current Page: %s' % self.driver.title)
        except exceptions as e: 
            print('ERROR: %s' % e) 
            return 

        try: 
            login_status = self.driver.find_element(By.XPATH, "//form[@id = 'fm1']/section[1]/span").text
            if 'Login Failed' in login_status: 
                print('ERROR: %s' % login_status)
        except exceptions.NoSuchElementException: 
            pass 

        if 'Your account is inactive' in self.driver.title: 
            print('ERROR: %s' % self.driver.title)
            # return False 
        elif self.start_title in self.driver.title: 
            print('Login successful') 
            # return True 
        time.sleep(3)
    

    # implement webdriver page refresh so that we don't just keep taking the same outdated elements
    def get_registration_seat_status(self): 
        try: 
            print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            xpath = list("//table[contains(@class, 'table')][4]/tbody/tr[i]")
            # x = driver.find_element(By.XPATH, "//table[contains(@class, 'table')][4]/tbody")
            for i in range(1,5): 
                xpath[47] = str(i)
                print(self.driver.find_element(By.XPATH, "".join(xpath)).text) 
                # row_title = driver.find_element(By.XPATH, "".join(title_xpath)).text
                # row_value = driver.find_element(By.XPATH, "".join(value_xpath)).text
                # print('%s %s' % (row_title, row_value))
        except exceptions.NoSuchElementException as e: 
            print('ERROR: %s' % e)
        time.sleep(3)


    def get_sms_address(self): 
        number = list(self.props['contact']['phone_number'])
        carrier = self.props['contact']['carrier'].lower()
        carrier_dict = self.props['gmail_sms']['domain']
        print('Parsing %s: %s' % (carrier.upper(), "".join(number)))

        for key in carrier_dict.keys(): 
            if key in carrier: 
                number += carrier_dict.get(key)
                return "".join(number)

        print('Error: %s carrier is not supported' % carrier)
        return None


    # need to implement a file writing system for the email subject/body paragraphs 
    # contains info gathered from get_registration_seat_status()
    def send_email(self): 
        # bot gmail credentials 
        un = self.props['gmail_sms']['auth']['address']
        pw = self.props['gmail_sms']['auth']['token']
        recipient = self.props['contact']['phone_number']

        message = EmailMessage()
        message['from'] = un
        message['to'] = recipient
        message['subject'] = subject 
        message.set_content(body) 

        # initialize STMP server 
        with smtplib.SMTP('smtp.gmail.com', SSL_PORT) as smtp: 
            smtp.starttls() 
            smtp.login(un, pw)
            print('Sending Email to %s...' % recipient)
            smtp.send_message(message)
            print('Sent')


    # def __enter__(self): 
    #     print('Enter') 

    # def __exit__(self, exc_type, exc_val, exc_tb): 
    #     print('Exit')
    #     self.driver.quit() 


def unit_test(): 
    scraper = CWLscraper() 
    print(scraper.get_sms_address())
    # scraper.get_registration_seat_status()
    # scraper.cwl_login()


if __name__ == '__main__': 
    unit_test()
        

    