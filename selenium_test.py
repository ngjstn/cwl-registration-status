from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException 
from selenium import webdriver 
import time 
import datetime 

def cwl_login(driver, login_name, password): 
    print('Navigating to CWL Login form...')

    driver.find_element(By.XPATH, "//input[@name = 'IMGSUBMIT']").click()
    print('Current Page: %s' % driver.title) 

    form = driver.find_element(By.XPATH, "//form[@id = 'fm1']")
    print('Inputting login credentials')
    form.find_element(By.NAME, 'username').send_keys(login_name)
    form.find_element(By.NAME, 'password').send_keys(password)

    print('Submitting Form')
    driver.find_element(By.XPATH, "//input[@type = 'submit']").click()

    print('Current Page: %s' % driver.title)
    if 'Your account is inactive' in driver.title: 
        print('ERROR: Failed to login. Check your CWL credentials')
        return False 
    else: 
        print('Login successful')
        return True 
    # time.sleep(5)


def get_registration_seat_status(driver): 
    # title_xpath = list("//table[contains(@class, 'table')][4]/tbody/tr[i]/td")
    # value_xpath = list("//table[contains(@class, 'table')][4]/tbody/tr[i]/td/strong")
    # print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    try: 
        while True:
            print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            xpath = title_xpath = list("//table[contains(@class, 'table')][4]/tbody/tr[i]")
            # x = driver.find_element(By.XPATH, "//table[contains(@class, 'table')][4]/tbody")
            # y = x.find_element(By.CSS_SELECTOR, '*')
            # y = x.find_elements(By.CSS_SELECTOR, "*")
            for i in range(1,5): 
                # title_xpath[47] = str(i)
                # value_xpath[47] = str(i)
                xpath[47] = str(i)
                print(driver.find_element(By.XPATH, "".join(xpath)).text) 
                # row_title = driver.find_element(By.XPATH, "".join(title_xpath)).text
                # row_value = driver.find_element(By.XPATH, "".join(value_xpath)).text
                # print('%s %s' % (row_title, row_value))
            time.sleep(300)
    except NoSuchElementException as e: 
        print('ERROR: %s' % e)
    # time.sleep(5)


if __name__ == '__main__': 
    un = 'test'
    pw = 'password'
    driver_exec_path = "C:\\Users\justin.ng\\Documents\\tests_vscode\\cwl_registration_status\\webdriver\\chromedriver.exe"
    website = "https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-section&dept=CPEN&course=311&section=101"
    # options = webdriver.ChromeOptions().add_experimental_option("excludeSwitches", ["enable-logging"])
    print('Starting web driver automation')
    with webdriver.Chrome(executable_path=driver_exec_path) as driver: 
        driver.set_window_size(1080, 800)
        driver.get(website) 
        print('*** %s ***' % driver.title)

        #cwl_login(driver, un, pw)
        get_registration_seat_status(driver)

    time.sleep(5)
    print('Closing web driver')