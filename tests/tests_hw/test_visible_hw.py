from pages.accordion import Accordion
import time
from conftest import browser

def test_visible_accordion(browser):
    accordion = Accordion(browser)
    accordion.visit()

    assert accordion.element1.visible()

    accordion.element2.click()
    time.sleep(2)

    assert not accordion.element1.visible()

def test_visible_accordion_default(browser):
    accordion = Accordion(browser)
    accordion.visit()

    assert not accordion.element3.visible()
    assert not accordion.element4.visible()
    assert not accordion.element5.visible()

