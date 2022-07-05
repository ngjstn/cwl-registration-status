from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, ElementNotVisibleException, WebDriverException
from selenium.webdriver.common.by import By
from selenium import webdriver 
from email.message import EmailMessage
import smtplib 
import yaml
import time 
import datetime 
import yaml
import errno

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
            sub = ['CWL SCRAPE - ', self.start_title.split('-')[0], self.start_title.split('-')[1]]
            self.subject = "".join(sub)
            print(self.start_title)
        except (NoSuchElementException, ElementClickInterceptedException, WebDriverException) as e: 
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
        except (NoSuchElementException, ElementClickInterceptedException, ElementNotVisibleException) as e: 
            print('ERROR: %s' % e) 
            return 

        try: 
            login_status = self.driver.find_element(By.XPATH, "//form[@id = 'fm1']/section[1]/span").text
            if 'Login Failed' in login_status: 
                print('ERROR: %s' % login_status)
        except NoSuchElementException: 
            pass 

        if 'Your account is inactive' in self.driver.title: 
            print('ERROR: %s' % self.driver.title)
        elif self.start_title in self.driver.title: 
            print('Login successful') 
        time.sleep(3)
    

    # implement webdriver page refresh function so that we don't just keep taking the same outdated elements
    def get_registration_seat_status(self): 
        try: 
            self.write_to_file(self.start_title, 'w') 
            self.write_to_file('\n', 'a')
            current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(current_time)
            self.write_to_file('\n', 'a')
            self.write_to_file(current_time, 'a')
            self.write_to_file('\n', 'a')
            xpath = list("//table[contains(@class, 'table')][4]/tbody/tr[i]")

            for i in range(1,5): 
                xpath[47] = str(i)
                output = self.driver.find_element(By.XPATH, "".join(xpath)).text
                print(output) 
                self.write_to_file(output, 'a')
                self.write_to_file('\n', 'a')
        except NoSuchElementException as e: 
            print('ERROR: %s' % e)
        time.sleep(3)


    def write_to_file(self, text, mode='w'): 
        try: 
            file = open('body.txt', mode)
            file.write(text)
        except IOError as e: 
            if e.errno == errno.ENOENT: 
                print('ERROR: File not found') 
            elif e.errno == errno.EACCES: 
                print('ERROR: Permission denied')
            else: 
                print(e)


    def get_sms_address(self, phone_num): 
        number = phone_num
        carrier = self.props['recipient']['carrier'].lower()
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
    def send_email(self, sms=False): 
        if sms: 
            recipient = self.get_sms_address(self.props['recipient']['phone_number'])
        else: 
            recipient = self.props['recipient']['gmail']
        bot_un = self.props['gmail_sms']['auth']['address']
        bot_pw = self.props['gmail_sms']['auth']['token']

        message = EmailMessage()
        message['from'] = bot_un
        message['to'] = recipient 
        message['subject'] = self.subject  
        with open('body.txt') as file: 
            print(file.read())
            body = file.read()
            # message.set_content(file.read())
            message.set_content(body)
        # message.set_content(body) 

        # initialize SMTP client
        with smtplib.SMTP('smtp.gmail.com', SSL_PORT) as smtp: 
            smtp.starttls() 
            smtp.login(bot_un, bot_pw)
            print('Sending Email to %s...' % recipient)
            try:
                smtp.send_message(message)
            except smtp.SMTPException as e: 
                print('ERROR: %s' % e)
            print('Sent')


    # def __enter__(self): 
    #     print('Enter') 

    # def __exit__(self, exc_type, exc_val, exc_tb): 
    #     print('Exit')
    #     self.driver.quit() 




if __name__ == '__main__': 
    scraper = CWLscraper() 
    # print(scraper.get_sms_address())
    scraper.get_registration_seat_status()
    scraper.send_email()

 
    # scraper.cwl_login()
        

    