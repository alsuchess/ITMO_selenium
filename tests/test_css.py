from pages.text_box import TextBox
from conftest import browser

def test_text_box_submit(browser):
    text_box = TextBox(browser)
    text_box.visit()

    text_box.submit_btn.check_css('color', 'rgba(255,255,255,1)')
    text_box.submit_btn.check_css('backgroundColor', 'rgb(0 123 255)')
    text_box.submit_btn.check_css('borderColor', 'rgb(0 123 255)')