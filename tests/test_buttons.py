from playwright.sync_api import Page, expect

def test_click_me_button(page: Page):
    page.goto("https://demoqa.com/")
    page.get_by_text('Elements').click()
    page.get_by_text('Buttons').click()
    page.locator('xpath=(//*[@class="btn btn-primary"])[3]').click()
    expect(page.locator('#dynamicClickMessage')).to_be_visible()
    expect(page.locator('#dynamicClickMessage')).to_have_text('You have done a dynamic click')