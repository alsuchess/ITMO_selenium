from pages.modal_dialog import ModalDialog
from pages.demoqa import DemoQa
from conftest import browser

def test_modal_elements(browser):
    modal_dialog = ModalDialog(browser)
    modal_dialog.visit()

    assert modal_dialog.elements.check_count_elements(count=5)

def test_navigation_modal(browser):
    modal_dialog = ModalDialog(browser)
    modal_dialog.visit()

    browser.refresh()
    modal_dialog.icon.click()
    browser.back()
    browser.set_window_size(900, 400)
    browser.forward()

    demoqa_page = DemoQa(browser)
    demoqa_page.equal_url()
    assert demoqa_page.get_title() == 'DEMOQA'

    browser.set_window_size(1000, 1000)

