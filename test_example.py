import re

from playwright.sync_api import Page, expect

def test_has_title_radio_button(page: Page):
    page.set_viewport_size({"width": 1840, "height": 1080})
    page.goto("https://demoqa.com/")
    page.get_by_text('Elements').click()
    page.get_by_text('Radio Button').click()
    expect(page.get_by_role("heading", name="Radio Button")).to_be_visible()

def test_yes_radio_button(page: Page):
    page.set_viewport_size({"width": 1840, "height": 1080})
    page.goto("https://demoqa.com/")
    page.get_by_text('Elements').click()
    page.get_by_text('Radio Button').click()
    page.locator('#yesRadio').check()



