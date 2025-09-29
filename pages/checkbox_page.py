import os
import random
from playwright.sync_api import expect
from pages.base_page import BasePage
# from pages.test_data import radio_button_page_data as data

title_text_locator = '.text-center'
expected_title_text = 'Check Box'
expand_all_button_name = 'Expand all'
collapse_all_button_name = 'Collapse all'
all_checkboxes_names_locator = '.rct-title'
expected_checkboxes_list = ['Home', 'Desktop', 'Notes', 'Commands', 'Documents', 'WorkSpace', 'React', 'Angular', 'Veu', 'Office', 'Public', 'Private', 'Classified', 'General', 'Downloads', 'Word File.doc', 'Excel File.doc']
toggle_button_locator = 'xpath=//button[@title="Toggle"]'
random_checkbox_name = expected_checkboxes_list[random.randint(1,len(expected_checkboxes_list)-1)]

class CheckboxPage(BasePage):
    page_url = 'https://demoqa.com/checkbox'

    def check_title(self):
        expect(self.page.locator(title_text_locator)).to_have_text(expected_title_text)

    def expand_all_checkboxes(self):
        self.page.get_by_role("button", name=expand_all_button_name).click()

    def get_actual_checkboxes_list(self):
        actual_checkboxes_list = []
        for name in self.page.locator(all_checkboxes_names_locator).all():
            actual_checkboxes_list.append(name.text_content())
        return actual_checkboxes_list

    def check_all_checkboxes_is_visible(self):
        for checkbox_name in expected_checkboxes_list:
            assert checkbox_name in self.get_actual_checkboxes_list()
        self.page.screenshot(type='jpeg', path=f'{os.getcwd()}/screenshots/expand_all_checkboxes.jpg') # dodaty v alure

    def collapse_all_checkboxes(self):
        self.page.get_by_role("button", name=collapse_all_button_name).click()

    def check_all_checkboxes_is_not_visible(self):
        del expected_checkboxes_list[0]
        for checkbox_name in expected_checkboxes_list:
            assert checkbox_name not in self.get_actual_checkboxes_list()
        self.page.screenshot(type='jpeg', path=f'{os.getcwd()}/screenshots/collapse_all_checkboxes.jpg') # dodaty v alure

    def mark_all_checkboxes(self):
        self.page.locator(all_checkboxes_names_locator).click()

    def get_result_text(self):
        return self.page.locator('#result').text_content()

    def check_all_checkboxes_is_marked(self):
        self.expand_all_checkboxes()
        for name in expected_checkboxes_list:
            if name == 'Word File.doc':
                assert 'wordFile' in self.get_result_text()
            elif name == 'Excel File.doc':
                assert 'excelFile' in self.get_result_text()
            else:
                assert name.lower() in self.get_result_text()
        self.page.screenshot(type='jpeg', path=f'{os.getcwd()}/screenshots/all_checkboxes_is_marked.jpg') # dodaty v alure

    def open_all_toggles(self):
        self.expand_all_checkboxes()
        toggles_amount = len(self.page.locator(toggle_button_locator).all())
        self.collapse_all_checkboxes()
        for toggle in range(toggles_amount):
            self.page.locator(f'xpath=(//button[@title="Toggle"])[{toggle}+1]').click()
        # self.page.screenshot(type='jpeg', path=f'{os.getcwd()}/screenshots/all_checkboxes_is_marked.jpg') # dodaty v alure

    def mark_check_box(self, checkbox_name=random_checkbox_name):
        self.page.get_by_text(checkbox_name).click()
        self.page.screenshot(type='jpeg', path=f'{os.getcwd()}/screenshots/all_checkboxes_is_marked.jpg') # dodaty v alure

    def unmark_check_box(self, checkbox_name=random_checkbox_name):
        self.page.get_by_text(checkbox_name).click()
        self.page.screenshot(type='jpeg', path=f'{os.getcwd()}/screenshots/all_checkboxes_is_marked.jpg') # dodaty v alure


    def check_marked_checkboxes(self):
        if random_checkbox_name == 'Desktop':
            assert 'desktop' in self.get_result_text()
            assert 'notes' in self.get_result_text()
            assert 'commands' in self.get_result_text()
        elif random_checkbox_name == 'Downloads':
            assert 'downloads' in self.get_result_text()
            assert 'wordFile' in self.get_result_text()
            assert 'excelFile' in self.get_result_text()
        elif random_checkbox_name == 'WorkSpace':
            assert 'workspace' in self.get_result_text()
            assert 'react' in self.get_result_text()
            assert 'angular' in self.get_result_text()
            assert 'veu' in self.get_result_text()
        elif random_checkbox_name == 'Office':
            assert 'office' in self.get_result_text()
            assert 'public' in self.get_result_text()
            assert 'private' in self.get_result_text()
            assert 'classified' in self.get_result_text()
            assert 'general' in self.get_result_text()
        elif random_checkbox_name == 'Documents':
            assert 'documents' in self.get_result_text()
            assert 'workspace' in self.get_result_text()
            assert 'react' in self.get_result_text()
            assert 'angular' in self.get_result_text()
            assert 'veu' in self.get_result_text()
            assert 'office' in self.get_result_text()
            assert 'public' in self.get_result_text()
            assert 'private' in self.get_result_text()
            assert 'classified' in self.get_result_text()
            assert 'general' in self.get_result_text()
        elif random_checkbox_name == 'Word File.doc':
            assert 'wordFile' in self.get_result_text()
        elif random_checkbox_name == 'Excel File.doc':
            assert 'excelFile' in self.get_result_text()
        else:
            assert random_checkbox_name.lower() in self.get_result_text()

    # def unmark_random_check_box(self):


    def check_result_text_missing(self):
        expect(self.get_result_text()).to_be_hidden()