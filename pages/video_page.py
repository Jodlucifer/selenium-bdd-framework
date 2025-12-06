from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class VideoPage(BasePage):
    PLAY_BUTTON = (By.CSS_SELECTOR, "div[id='vid-01j912fjvcqsxac8aetepjeesh'] button[aria-label='Play Video']")
    EPISODES = (By.CSS_SELECTOR, "div[class='mb-6']")
    PAUSE_BUTTON = (By.XPATH, "//div[@class='jw-icon jw-icon-inline jw-button-color jw-reset jw-icon-playback']")
    CONTINUE_WATCHING = (By.XPATH, "//button[contains(text(),'Continue Watching')]")
    VOLUME_SLIDER = (By.CSS_SELECTOR, ".volume-slider-selector")
    SETTINGS_BUTTON = (By.CSS_SELECTOR, "div[aria-label='Settings'][role='button']")

    def play_and_pause_video(self, duration):
        self.click(self.EPISODES)
        time.sleep(10)
        self.click(self.PLAY_BUTTON)
        time.sleep(10)
        iframe = self.driver.find_element(By.XPATH, "//iframe[@id='video_player']")
        self.driver.switch_to.frame(iframe)
        time.sleep(5)
        pause_button = self.driver.find_element(By.CSS_SELECTOR,
                                                "div[class='jw-icon jw-icon-inline jw-button-color jw-reset jw-icon-playback']")

        self.driver.execute_script("arguments[0].scrollIntoView({behavior:'smooth',block:'center'});", pause_button)
        self.driver.execute_script("arguments[0].click();", pause_button)

    def continue_watching(self):
        # time.sleep(5)
        continue_button = self.driver.find_element(By.CSS_SELECTOR,
                                                   "div[class='jw-icon jw-icon-inline jw-button-color jw-reset jw-icon-playback']")

        self.driver.execute_script("arguments[0].scrollIntoView({behavior:'smooth',block:'center'});", continue_button)
        self.driver.execute_script("arguments[0].click();", continue_button)

    def set_volume(self, volume_level):
        speaker_icon = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".jw-icon-volume"))
        )
        ActionChains(self.driver).move_to_element(speaker_icon).perform()
        WebDriverWait(self.driver, 2)
        self.driver.execute_script(f"jwplayer().setVolume({volume_level});")

    def change_resolution(self, resolution):
        settings_button = (By.CSS_SELECTOR, "div[aria-label='Settings'][role='button']")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(settings_button)
        ).click()
        resolution_option = (By.CSS_SELECTOR, f"button[aria-label='{resolution}']")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(resolution_option)
        ).click()

    def pause_video(self):
        self.click(self.PAUSE_BUTTON)
