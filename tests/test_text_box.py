from playwright.sync_api import Page
from pages.text_box_page import TextBoxPage
from pages.test_data import text_box_page_data as data

def test_text_box_fill_all_fields(page:Page):
    text_box_page = TextBoxPage(page)
    text_box_page.open_page()
    text_box_page.fill_all_fields()
    text_box_page.click_submit_button()
    text_box_page.check_all_results()

# will be fixed later
# def test_incorrect_email(page:Page):
#     text_box_page = TextBoxPage(page)
#     text_box_page.open_page()
#     text_box_page.fill_email_field(data.incorrect_email)
#     text_box_page.click_submit_button()
#     text_box_page.check_email_result_text()