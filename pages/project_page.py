from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProjectPage(BasePage):
    ALL_TITLES = (By.XPATH, "//div[@class='mb-20 grid justify-start gap-x-5 gap-y-10']")
    DETAILS_TAB = (By.XPATH, "//a[@id='detailsSection']")
    VIDEOS_TAB = (By.XPATH, "//a[@id='videosSection']")
    BACK_BUTTON = (By.XPATH, "//button[contains(text(),'Back')]")
    LOGOUT_BUTTON = (By.XPATH, "//a[@id='signOutSideBar']")

    def navigate_to_project(self, project_name):
        self.click(self.ALL_TITLES)
        project_locator = (By.XPATH, f"//img[@alt='Test automation project']")
        self.click(project_locator)

    def switch_to_details(self):
        self.click(self.DETAILS_TAB)

    def switch_to_videos(self):
        self.click(self.VIDEOS_TAB)

    def exit_project(self):
        self.driver.back()

    def logout(self):
        self.click(self.LOGOUT_BUTTON)
