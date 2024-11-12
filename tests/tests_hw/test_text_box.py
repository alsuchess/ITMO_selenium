from pages.text_box import TextBox
from conftest import browser

def test_clear(browser):
    text_box = TextBox(browser)
    text_box.visit()

    a = 'tester'
    b = 'test'

    text_box.name.send_keys(a)
    text_box.address.send_keys(b)
    text_box.submit_btn.click_force()

    assert text_box.form.get_text() == f'Name:{a}\nCurrent Address :{b}'
