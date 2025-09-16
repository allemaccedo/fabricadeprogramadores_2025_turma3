from selenium import webdriver
import time

driver = webdriver.Chrome()
time.sleep (10)
driver.get ("")
driver.maximize_window()
driver.quit()