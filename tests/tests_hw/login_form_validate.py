from pages.automation_practice_form import AutomationPracticeForm
from conftest import browser

def test_placeholder(browser):
    automation_practice_form = AutomationPracticeForm(browser)
    automation_practice_form.visit()

    assert automation_practice_form.first_name.get_dom_attribute(name='placeholder')
    assert automation_practice_form.last_name.get_dom_attribute(name='placeholder')
    assert automation_practice_form.user_email.get_dom_attribute(name='placeholder')
    assert automation_practice_form.user_email.get_dom_attribute(name='pattern')

    automation_practice_form.submit_btn.click_force()

    assert automation_practice_form.form.get_dom_attribute(name='class') == 'was-validated'
