__author__ = 'harithan'

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup


driver = webdriver.Firefox()
wait = WebDriverWait(driver, 10)

driver.get('https://www.linkedin.com')

username = driver.find_element_by_id('session_key-login')
password = driver.find_element_by_id('session_password-login')
submit_button = driver.find_element_by_id('login')

username.send_keys('Your Email')
password.send_keys('Your Password')
submit_button.submit()
#modify the below link based on area and search criteria
driver.get('http://www.linkedin.com/vsearch/p?orig=FCTD&keywords=tech%20recruiter&openFacets=G,N,CC&f_G=us%3A70')
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,'results_count')))
soup = BeautifulSoup(driver.page_source, 'xml')
variable = soup.find(attrs={'class': 'title'})['href']
# This loop will run as long as linkedin suggests people matching the keywords and profile.
while 1:
    driver.get(variable)
    soup = BeautifulSoup(driver.page_source, 'xml')
    future = soup.find(attrs={'class': 'recommendation-link'})['href']
    variable = future
