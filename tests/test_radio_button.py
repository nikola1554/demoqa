from playwright.sync_api import Page
from pages.radio_button_page import RadioButtonPage

def test_yes_radio_button(page: Page):
    radio_button_page = RadioButtonPage(page)
    radio_button_page.open_page()
    radio_button_page.chose_radio_yes()
    radio_button_page.check_result_text('Yes')

def test_impressive_radio_button(page: Page):
    radio_button_page = RadioButtonPage(page)
    radio_button_page.open_page()
    radio_button_page.chose_radio_impressive()
    radio_button_page.check_result_text('Impressive')

def test_no_radio_button(page: Page):
    radio_button_page = RadioButtonPage(page)
    radio_button_page.open_page()
    radio_button_page.check_radio_no_is_disabled()