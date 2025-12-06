from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    PIN_INPUT = (By.NAME, "Pin")

    def enter_pin_and_login(self, pin):
        self.type_text(self.PIN_INPUT, pin)
        self.driver.find_element(*self.PIN_INPUT).submit()

