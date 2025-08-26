from playwright.sync_api import expect
from pages.base_page import BasePage
from playwright.sync_api import Page
# from pages.test_data import buttons_page_data as data

radio_button_yes_locator = 'Yes'
radio_button_no_locator = 'No'
radio_button_impressive_locator = 'Impressive'
result_text_locator = '.mt-3'
expected_result_text = 'You have selected '

class RadioButtonPage(BasePage):
    page_url = 'https://demoqa.com/radio-button'

    def chose_radio_yes(self):
        self.page.get_by_text(radio_button_yes_locator).click()

    def chose_radio_impressive(self):
        self.page.get_by_text(radio_button_impressive_locator).click()

    def check_radio_no_is_disabled(self):
        self.page.get_by_text(radio_button_no_locator).is_disabled()

    def check_result_text(self, chosen_radio_name):
        expect(self.page.locator(result_text_locator)).to_be_visible()
        expect(self.page.locator(result_text_locator)).to_have_text(f'{expected_result_text}{chosen_radio_name}')