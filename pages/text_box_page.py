from playwright.sync_api import expect
from pages.base_page import BasePage
from pages.test_data import text_box_page_data as data

class TextBoxPage(BasePage):
    page_url = data.page_url

    def fill_user_name_field(self):
        self.page.locator(data.user_name_field_selector).fill(data.random_user_name)

    def fill_email_field(self, email=data.random_user_email):
        self.page.locator(data.email_field_selector).fill(email)

    def fill_current_address_field(self):
        self.page.locator(data.current_address_field_selector).fill(data.random_current_address)

    def fill_permanent_address_field(self):
        self.page.locator(data.permanent_address_field_selector).fill(data.random_permanent_address)

    def fill_all_fields(self):
        self.fill_user_name_field()
        self.fill_email_field()
        self.fill_current_address_field()
        self.fill_permanent_address_field()

    def click_submit_button(self):
        self.page.locator(data.submit_button_selector).click()

    def check_name_result_text(self):
        expect(self.page.locator(data.name_result_text_selector)).to_have_text(data.expected_name)

    def check_email_result_text(self):
        expect(self.page.locator(data.email_result_text_selector)).to_have_text(data.expected_email)

    def check_current_address_result_text(self):
        expect(self.page.locator(data.current_address_result_text_selector)).to_have_text(data.expected_current_address)

    def check_permanent_address_result_text(self):
        expect(self.page.locator(data.permanent_address_result_text_selector)).to_have_text(data.expected_permanent_address)

    def check_all_results(self):
        self.check_name_result_text()
        self.check_email_result_text()
        self.check_current_address_result_text()
        self.check_permanent_address_result_text()

