from selenium import webdriver


def before_all(context):
    print(">>> Initializing WebDriver...")
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
