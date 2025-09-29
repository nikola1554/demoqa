from playwright.sync_api import Page
from pages.checkbox_page import CheckboxPage

def test_title(page: Page):
    checkbox_page = CheckboxPage(page)
    checkbox_page.open_page()
    checkbox_page.check_title()

def test_expand_all(page: Page):
    checkbox_page = CheckboxPage(page)
    checkbox_page.open_page()
    checkbox_page.expand_all_checkboxes()
    checkbox_page.check_all_checkboxes_is_visible()

def test_collapse_all(page: Page):
    checkbox_page = CheckboxPage(page)
    checkbox_page.open_page()
    checkbox_page.expand_all_checkboxes()
    checkbox_page.collapse_all_checkboxes()
    checkbox_page.check_all_checkboxes_is_not_visible()

def test_mark_all_checkboxes(page: Page):
    checkbox_page = CheckboxPage(page)
    checkbox_page.open_page()
    checkbox_page.mark_all_checkboxes()
    checkbox_page.check_all_checkboxes_is_marked()

def test_open_all_menu(page: Page):
    checkbox_page = CheckboxPage(page)
    checkbox_page.open_page()
    checkbox_page.open_all_toggles()
    checkbox_page.check_all_checkboxes_is_visible()

def test_mark_random_checkbox(page: Page):
    checkbox_page = CheckboxPage(page)
    checkbox_page.open_page()
    checkbox_page.expand_all_checkboxes()
    checkbox_page.mark_random_check_box()
    checkbox_page.check_marked_checkboxes()

def test_result_text_disappear_after_unmark_checkbox(page: Page):
    checkbox_page = CheckboxPage(page)
    checkbox_page.open_page()
    checkbox_page.expand_all_checkboxes()
    checkbox_page.mark_check_box()
    checkbox_page.mark_check_box()
    # checkbox_page.check_result_text_missing()




#after unmark random checkbox text result dissapire