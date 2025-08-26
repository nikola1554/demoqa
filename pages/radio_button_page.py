from playwright.sync_api import expect
from pages.base_page import BasePage
from pages.test_data import radio_button_page_data as data

class RadioButtonPage(BasePage):
    page_url = data.page_url

    def chose_radio_yes(self):
        self.page.get_by_text(data.radio_button_yes_locator).click()

    def chose_radio_impressive(self):
        self.page.get_by_text(data.radio_button_impressive_locator).click()

    def check_radio_no_is_disabled(self):
        self.page.get_by_text(data.radio_button_no_locator).is_disabled()

    def check_result_text(self, chosen_radio_name):
        expect(self.page.locator(data.result_text_locator)).to_be_visible()
        expect(self.page.locator(data.result_text_locator)).to_have_text(f'{data.expected_result_text}{chosen_radio_name}')