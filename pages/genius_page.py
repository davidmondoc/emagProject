from selenium.webdriver.common.by import By
from base_page import Base_page

class Genius_page(Base_page):
    FREE_TRIAL_BTN=(By.LINK_TEXT, 'ÎNCEARCĂ GRATUIT 3 LUNI')
    TRY_NOW_BTN=(By.LINK_TEXT, 'Încerc acum')


    def genius_link_check(self):
        actual_url=self.chrome.current_url
        expected='https://www.emag.ro/genius?ref=hdr_emag-genius'
        self.assertEqual (expected, actual_url, 'expected link is not the same with actual url')

    def click_free_trial(self):
        self.chrome.find_element(*self.FREE_TRIAL_BTN).click()

    def check_if_btn_displayed(self):
        self.chrome.find_element(*self.TRY_NOW_BTN).is_displayed()


