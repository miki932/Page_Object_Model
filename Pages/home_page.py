"""
from Pages.base_page import Base_Page
from Resources.locators import HomePageLocators


class Home_Page(Base_Page):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get('http://www.youtube.com')

    def search_video(self, video_text):
        self.enter_text(HomePageLocators.yt_search_field, video_text)
        self.click(HomePageLocators.yt_search_button)
"""