from playwright.sync_api import expect
from pages.base_page import BasePage
from pages.test_data import buttons_page_data as data


class ButtonsPage(BasePage):
    page_url = data.page_url

    def click_button_click_me(self):
        self.page.locator(data.click_me_button_selector).click()

    def check_result_text_click_me_button(self):
        expect(self.page.locator(data.result_text_click_me_button_selector)).to_be_visible()
        expect(self.page.locator(data.result_text_click_me_button_selector)).to_have_text(data.expected_text_click_me_button)

    def click_double_click_me_button(self):
        self.page.locator(data.double_click_me_button_selector).dblclick()

    def check_result_text_double_click_me_button(self):
        expect(self.page.locator(data.result_text_double_click_me_button_selector)).to_be_visible()
        expect(self.page.locator(data.result_text_double_click_me_button_selector)).to_have_text(data.expected_text_double_click_me_button)

    def click_right_click_me_button(self):
        self.page.locator(data.right_click_me_button_selector).click(button="right")

    def check_result_text_right_click_me_button(self):
        expect(self.page.locator(data.result_text_right_click_me_button_selector)).to_be_visible()
        expect(self.page.locator(data.result_text_right_click_me_button_selector)).to_have_text(data.expected_text_right_click_me_button)