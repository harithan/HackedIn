__author__ = 'harithan'
from time import sleep
from random import randint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
user = 'your user name here'
passw = 'your password here'
driver = webdriver.Firefox()
wait = WebDriverWait(driver, 10)
driver.get('https://www.linkedin.com')
username = driver.find_element_by_id('session_key-login')
password = driver.find_element_by_id('session_password-login')
submit_button = driver.find_element_by_id('login')
username.send_keys(user)
password.send_keys(passw)
submit_button.submit()
driver1 = webdriver.Firefox()

driver1.get('https://www.linkedin.com')
username1 = driver1.find_element_by_id('session_key-login')
password1 = driver1.find_element_by_id('session_password-login')
submit_button1 = driver1.find_element_by_id('login')
username1.send_keys(user)
password1.send_keys(passw)
submit_button1.submit()
#modify the below link based on area and search criteria
driver.get('https://www.linkedin.com/vsearch/p?keywords=IT%20Recruiter&title=IT%20Recruiter&titleScope=CP&trk=tyah&trkInfo=tarId%3A1418423381547,tas%3Ait%20recruiter,idx%3A1-1-1&rsid=1766873661418423384066&openFacets=N,G,CC&orig=FCTD&f_G=us%3A70')
WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.ID, 'results_count')))
soup = BeautifulSoup(driver.page_source, 'xml')
variable = soup.find(attrs={'class': 'title'})['href']
# This loop will run as long as linkedin suggests people matching the keywords and profile.
b = 1
x = 1
while 1:
    print x

    if b:
        b = 0
        driver.get(variable)
        #sleep(randint(1, 4))
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.ID, 'control_gen_4')))
        soup = BeautifulSoup(driver.page_source, 'xml')
        try:
            future = soup.find(attrs={'class': 'recommendation-link'})['href']
            x += 1
            variable = future
        except TypeError:
            print'Oops blacklisted by linkedIn if this message repeats more than twice'
    else:
        b = 1
        driver1.get(variable)
        #sleep(randint(1, 4))
        WebDriverWait(driver1, 10).until(ec.presence_of_element_located((By.ID, 'control_gen_4')))
        soup = BeautifulSoup(driver1.page_source, 'xml')
        try:
            future = soup.find(attrs={'class': 'recommendation-link'})['href']
            x += 1
            variable = future
        except TypeError:
            print'Oops blacklisted by linkedIn if this message repeats more than twice'
