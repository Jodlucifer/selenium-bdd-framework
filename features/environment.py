from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def before_all(context):
    print(">>> Initializing WebDriver...")
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
