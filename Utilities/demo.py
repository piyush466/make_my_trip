import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.makemytrip.com/hotels/")
driver.implicitly_wait(10)
driver.maximize_window()
print("pa")

driver.find_element(By.XPATH, "//span[text()='Price per Night']").click()
driver.find_element(By.XPATH, "//li[text()='₹5000+']").click()
time.sleep(6)
driver.quit()
print("pass")
