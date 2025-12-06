from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("https://indeedemo-fyc.watch.indee.tv/login")
signin = driver.find_element(By.ID,"sign-in-button")
print(signin)
