# test.py
# Author: Sébastien Combéfis, Guillaume de Moffarts
# Version: February 24, 2019

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('http://localhost:5000')

# Test #1
# Enter wrong credentials in the form and submit it
driver.find_element(By.NAME, 'username').send_keys('me')
driver.find_element(By.NAME, 'password').send_keys('mypassword')
driver.find_element(By.ID, 'login').submit()

# Wait for the result to show
try:
    WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, 'connected')))
except:
    print('Test #1 K0: no element with id="connected" found.')

if driver.find_element(By.ID,'connected').text == 'KO':
    print('Test #1 OK: Wrong credentials is correctly refused.')
else:
    print('Test #1 Failed.')
    driver.quit()

# Test #2
# Enter correct credentials in the form and submit it
driver.find_element(By.NAME, 'username').send_keys('me')
driver.find_element(By.NAME, 'password').send_keys('mypwd')
driver.find_element(By.ID, 'login').submit()

# Wait for the result to show
try:
    WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, 'connected')))
except:
    print('Test #2 Failed: no element with id="connected" found.')

if driver.find_element(By.ID,'connected').text == 'OK':
    print('Test #2 OK: Correct credentials is correctly accepted.')
else:
    print('Test #2 Failed.')

driver.quit()
