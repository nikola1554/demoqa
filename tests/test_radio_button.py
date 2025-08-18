from playwright.sync_api import Page, expect

def test_yes_radio_button(page: Page):
   page.goto("https://demoqa.com/")
   page.get_by_text('Elements').click()
   page.get_by_text('Radio Button').click()
   page.get_by_text('Yes').click()
   expect(page.locator('.mt-3')).to_be_visible()
   expect(page.locator('.mt-3')).to_have_text('You have selected Yes')

def test_has_title_radio_button(page: Page):
    page.goto("https://demoqa.com/")
    page.get_by_text('Elements').click()
    page.get_by_text('Radio Button').click()
    expect(page.get_by_role("heading", name="Radio Button")).to_be_visible()