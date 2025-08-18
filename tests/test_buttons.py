from playwright.sync_api import Page
from pages.buttons_page import ButtonsPage

def test_click_me_button(page: Page):
    buttons_page = ButtonsPage(page)
    buttons_page.open_page()
    buttons_page.click_button_click_me()
    buttons_page.check_result_text_click_me_button()

def test_double_click_me_button(page: Page):
    buttons_page = ButtonsPage(page)
    buttons_page.open_page()
    buttons_page.click_double_click_me_button()
    buttons_page.check_result_text_double_click_me_button()

def test_right_click_me_button(page: Page):
    buttons_page = ButtonsPage(page)
    buttons_page.open_page()
    buttons_page.click_right_click_me_button()
    buttons_page.check_result_text_right_click_me_button()