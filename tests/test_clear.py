from pages.text_box import TextBox
import time
from conftest import browser

def test_clear(browser):
    text_box = TextBox(browser)
    text_box.visit()
    time.sleep(2)

    text_box.name.send_keys('tester')
    time.sleep(2)

    text_box.name.clear()

    assert text_box.name.get_text() == ''

