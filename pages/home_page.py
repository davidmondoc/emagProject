from selenium.webdriver.common.by import By
from pages.base_page import Base_page

class Home_page(Base_page):
    GENIUS_LINK=(By.LINK_TEXT, 'eMAG Genius')

    def site_acces(self):
        self.chrome.get('https://www.emag.ro/')

    def click_genius_link(self):
        self.chrome.find_element(*self.GENIUS_LINK).click()
