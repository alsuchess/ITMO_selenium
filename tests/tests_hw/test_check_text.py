from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage
from conftest import browser

def test_check_footer(browser):
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    assert demo_qa_page.footer.get_text() == "© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED."

def test_check_text_on_center(browser):
    demo_qa_page = DemoQa(browser)
    el_page = ElementsPage(browser)

    demo_qa_page.visit()
    el_page.btn_elements.click()

    assert el_page.center.get_text() == "Please select an item from left to start practice."

def test_page_elements(browser):
    el_page = ElementsPage(browser)
    el_page.visit()

    assert el_page.icon.exist()
    assert el_page.bnt_sidebar_first.exist()
    assert el_page.bnt_sidebar_first_textbox.exist()










