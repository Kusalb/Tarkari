from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Firefox()
emailelement = driver.find_element(By.XPATH, '')