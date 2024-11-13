from pages.text_box import TextBox
from conftest import browser

def test_clear(browser):
    text_box = TextBox(browser)
    text_box.visit()

    assert text_box.name.get_dom_attribute(name='placeholder')
    assert text_box.name.get_dom_attribute(name='placeholder') == 'Full Name'



