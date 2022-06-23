from selenium.webdriver.common.by import By
from selenium import webdriver 
import time 

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
    # seat_summary_table = driver.find_element(By.XPATH, "//table[contains(@class, 'table')][4]/tbody")
    # for i in range()
    print('Total Seats Remaining: %s' % driver.find_element(By.XPATH, "//table[contains(@class, 'table')][4]/tbody/tr[1]/td/strong").text)
    time.sleep(5)


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