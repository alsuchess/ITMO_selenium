from pages.demoqa import DemoQa
import time
from conftest import browser

def test_navigation(browser):
    demo_qa_page = DemoQa(browser)

    demo_qa_page.visit()
    browser.set_window_size(1000,300)
    time.sleep(2)
    browser.set_window_size(1000,1000)