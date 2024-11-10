from pages.demoqa import DemoQa
from conftest import browser

def test_navigation(browser):
    demo_qa_page = DemoQa(browser)

    demo_qa_page.visit()
    assert demo_qa_page.get_title() == 'DEMOQA'