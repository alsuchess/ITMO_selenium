from pages.webtables import WebTables
from conftest import browser
import time

def test_tables(browser):
    page_tables = WebTables(browser)
    page_tables.visit()

    page_tables.add.click()
    time.sleep(2)
    page_tables.submit.click()

    assert page_tables.form.get_dom_attribute(name='class') == 'was-validated'

    page_tables.first_name.send_keys('test')
    page_tables.last_name.send_keys('test')
    page_tables.email.send_keys('test@test.com')
    page_tables.age.send_keys('10')
    page_tables.salary.send_keys('1000')
    page_tables.department.send_keys('test')

    page_tables.submit.click()

    assert not page_tables.form.exist()
    assert 'test\ntest\n10\ntest@test.com\n1000\ntest' in page_tables.table.get_text()

    page_tables.pencil.click()
    assert page_tables.form.exist()

    page_tables.first_name.clear()
    page_tables.first_name.send_keys('tester')

    page_tables.submit.click()

    assert 'tester\ntest\n10\ntest@test.com\n1000\ntest' in page_tables.table.get_text()

    page_tables.btn_delete_row4.click()

    assert not 'tester\ntest\n10\ntest@test.com\n1000\ntest' in page_tables.table.get_text()





