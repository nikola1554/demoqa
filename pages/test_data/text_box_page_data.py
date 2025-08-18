import random
import string

def generate_random_value(length=16):
    return ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(length)])

page_url = "https://demoqa.com/text-box"
user_name_field_selector = "#userName"
email_field_selector = '#userEmail'
current_address_field_selector = '#currentAddress'
permanent_address_field_selector = '#permanentAddress'
submit_button_selector = '#submit'
random_user_name = generate_random_value()
random_user_email = f'{generate_random_value(random.randint(1,16))}@{generate_random_value(random.randint(1,16))}.com'
random_permanent_address = generate_random_value()
random_current_address = generate_random_value()
name_result_text_selector = '#name'
email_result_text_selector = '#email'
current_address_result_text_selector = "css=p[id='currentAddress']"
permanent_address_result_text_selector = "css=p[id='permanentAddress']"
expected_name = f'Name:{random_user_name}'
expected_email = f'Email:{random_user_email}'
expected_current_address = f'Current Address :{random_current_address}'
expected_permanent_address = f'Permananet Address :{random_permanent_address}'
incorrect_email = 'foxintheforest@blahblah.uiii'