from pages.demoqa import DemoQa
from conftest import browser

def test_check_text(browser):
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    assert demo_qa_page.footer.get_text() == "© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED."

    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    demo_qa_page.btn_elements2.click()

    assert demo_qa_page.center.get_text() == "Please select an item from left to start practice."






